from bs4 import BeautifulSoup
from cache import Cache
import requests
import re

pcache = Cache("/output/pages_cache.json")

def get_exercises_ref_for_muscle_group(muscle_group_id):
    url = "https://exrx.net/Lists/ExList/%s" % muscle_group_id 
    # print(url)
    page_data = pcache.get(url)
    if not page_data:
        page_data = requests.get(url).text
        pcache.set(url, page_data, expire_in_days=9999)

    soup = BeautifulSoup(page_data, "html.parser")

    links = soup.select("a")
    rlinks = []

    reg = re.compile('.*WeightExercises\/(.*)\/(.{2})(.*)')

    for link in links:
        rlink = None
        try:
            rlink = link['href']
        except:
            continue

        if "../../WeightExercises" in link['href']:
            rlink = "https://exrx.net/" + str(link['href'])[6:]

        m = reg.match(rlink)
        if m != None:
            # muscles = []
            # muscles.append({'relation':'target','muscle_id':m.group(1)})
            r = {
                'url': rlink,
                'exercise_id': m.group(2) + m.group(3),
                'equipment': m.group(2),
                'target_muscle_group': muscle_group_id
                # 'muscles': muscles
            }
            rlinks.append(r)

    # print(rlinks)
    return rlinks

def get_exercise_details(url):
    page_data = pcache.get(url)
    if not page_data:
        page_data = requests.get(url).text
        pcache.set(url, page_data, expire_in_days=9999)

    page = BeautifulSoup(page_data, "html.parser")

    # print(url)
    # print(page_data)
    name = page.find("h1").text.strip()
    
    utility = "undefined"
    try:
        utility = page.find_all('td')[1].text.strip().lower()
    except:
        print('no utility')

    mechanics = "undefined"
    try:
        mechanics = page.find_all("td")[3].text.strip().lower()
    except IndexError:
        print('no mechanics')

    force = 'undefined'
    try:
        force = page.find_all("td")[5].text.strip().lower()
    except IndexError:
        print('no force')

    preparation = ''
    try:
        preparation = page.find_all("p")[2].text.strip()
    except IndexError:
        print('no preparation')

    execution = ''
    try:
        execution = page.find_all("p")[4].text.strip()
    except IndexError:
        print('no execution')

    comments = ''
    try:
        comments = page.find_all("p")[5].text.strip()
    except IndexError:
        print('no comments')

    media_url = None

    videosrc = page.find("source")
    if videosrc is not None:
        media_url = videosrc.get('src')

    if media_url is None:
        imgsrc = page.find("meta[name=thumbnail]")
        if imgsrc is not None:
            media_url = imgsrc.get('content')

    muscle_targets_regex = '<strong>Target<\/strong><\/a><\/p><ul>(.*?)<\/ul>'
    muscle_synergists_regex = '<strong>Synergists<\/strong><\/a><\/p><ul>(.*?)<\/ul>'
    muscle_dyn_stabilizers_regex = '<strong>Dynamic Stabilizers<\/strong><\/a><\/p><ul>(.*?)<\/ul>'
    muscle_stabilizers_regex = '<strong>Stabilizers<\/strong><\/a><\/p><ul>(.*?)<\/ul>'
    muscle_antagonist_stabilizer_regex = '<strong>Antagonist Stabilizer<\/strong><\/a><\/p><ul>(.*?)<\/ul>'

    muscle_list_regex = '<li><a href=\"..\/..\/Muscles\/(.*?)\".*?<\/a>'

    muscles = []
    # muscles.append({'relation':'target','muscle_id':target_muscle})

    main_data = str(page.find('main')).replace("\n", "")

    #target muscles extract
    muscles_list = extract_muscles(muscle_targets_regex, muscle_list_regex, main_data)
    for m in muscles_list:
        muscles.append({'relation':'target','muscle_id':m})

    muscles_list = extract_muscles(muscle_synergists_regex, muscle_list_regex, main_data)
    for m in muscles_list:
        muscles.append({'relation':'synergist','muscle_id':m})

    muscles_list = extract_muscles(muscle_stabilizers_regex, muscle_list_regex, main_data)
    for m in muscles_list:
        muscles.append({'relation':'stabilizer','muscle_id':m})

    muscles_list = extract_muscles(muscle_dyn_stabilizers_regex, muscle_list_regex, main_data)
    for m in muscles_list:
        muscles.append({'relation':'dynamic_stabilizer','muscle_id':m})

    muscles_list = extract_muscles(muscle_antagonist_stabilizer_regex, muscle_list_regex, main_data)
    for m in muscles_list:
        muscles.append({'relation':'antagonist_stabilizer','muscle_id':m})

    return {
        'name': name,
        'utility': utility,
        'force': force,
        'mechanics': mechanics,
        'preparation': preparation,
        'execution': execution,
        'comments': comments,
        'muscles': muscles,
        'page_url': url,
        'media_url': media_url
    }

def extract_muscles(muscle_section_regex, muscle_list_regex, main_data):
    m = re.findall(muscle_section_regex, main_data)

    result = []
    if len(m)>0:
        muscle_contents = m[0]
        print(muscle_section_regex)
        print(muscle_contents)
        print(muscle_list_regex)
        mm = re.findall(muscle_list_regex, muscle_contents)
        if len(mm) == 0:
            print('no muscle for ', muscle_list_regex, muscle_contents)
        for mmm in mm:
            m = mmm.replace('target="_parent','')
            m = m.replace('"','')
            result.append(m)

    print(result)
    return result
