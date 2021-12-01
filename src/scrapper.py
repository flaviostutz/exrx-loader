from bs4 import BeautifulSoup
from cache import Cache
import requests

pcache = Cache("./pages_cache.json")

def get_exercise_links_for_muscle_group(muscle_group_id):
    url = "https://exrx.net/Lists/ExList/%s" % muscle_group_id 
    # print(url)
    page_data = pcache.get(url)
    if not page_data:
        page_data = requests.get(url).text
        pcache.set(url, page_data, expire_in_days=9999)

    soup = BeautifulSoup(page_data, "html.parser")

    links = soup.select("a")
    rlinks = []

    for link in links:
        rlink = None
        try:
            rlink = link['href']
        except:
            continue

        if "../../WeightExercises" in link['href']:
            rlink = "https://exrx.net/" + str(link['href'])[6:]

        if "WeightExercises" in rlink: 
            rlinks.append(rlink)
        
    print(rlinks)

