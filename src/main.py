import db
import scrapper
import time
import io

if __name__ == '__main__':

    db.init()

    print("Get all muscle groups")
    muscle_group_ids = db.get_muscle_group_ids()

    # exercises = []

    for mgi in muscle_group_ids:

        #get a list of all exercices available for this muscle group
        exercises_ref = scrapper.get_exercises_ref_for_muscle_group(mgi)
        print('muscle group ', mgi)
        print(exercises_ref)
        time.sleep(0.5)

        for ex_ref in exercises_ref:

            #get details about the exercise
            print('exercise ', ex_ref['url'])
            exr = scrapper.get_exercise_details(ex_ref['url'])
            # print(exercise)
            exercise = {**exr, **ex_ref}
            # exercises.append(exercise)
            # print(exercises)

            #save exercise in db
            db.insert_exercise(exercise)

            # break

    
    # print(exercises)

    with io.open('/output/datadump.sql', 'w') as p:
        conn = db.conn()
        for line in conn.iterdump(): 
            p.write('%s\n' % line)
        conn.close()

    print("Database dumped")
