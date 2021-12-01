import db
import scrapper
import time

if __name__ == '__main__':

    db.create_tables()

    print("Get all muscle groups")
    muscle_group_ids = db.get_muscle_group_ids()
    print(muscle_group_ids)

    for mgi in muscle_group_ids:
        links = scrapper.get_exercise_links_for_muscle_group(mgi)
        print(links)
        time.sleep(0.5)
        break

    #load main index

    # db.create_all()
    # if not Exercise.query.first():
    #     exercises_list= get_data(get_exercise_links(obj))
    #     for ex in exercises_list:
    #         utility = get_or_create_utility(ex.utility,ex.mechanics)
    #         force = get_or_create_force(ex.force)
    #         mechanics = get_or_create_mech(ex.mechanics)
    #         muscle = get_or_create_muscle(ex.target_muscle)
    #         get_or_create_exercise(ex.name,utility.id, force.id, mechanics.id,ex.instructions, muscle.id)
