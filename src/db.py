import sqlite3

def conn():
    return sqlite3.connect('/output/sqlite.db')

def init():
    con = conn()
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS muscle_group(
                    id text NOT NULL, 
                    name text NOT NULL,
                    PRIMARY KEY (id)
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS muscle(
                    id text NOT NULL,
                    muscle_group_id text NOT NULL, 
                    name text NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY (muscle_group_id)
                        REFERENCES muscle_group(id)
                        ON DELETE CASCADE
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS equipment(
                    id text NOT NULL, 
                    name text NOT NULL,
                    PRIMARY KEY (id)
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS exercise(
                    id text NOT NULL,
                    equipment_id text NOT NULL,
                    name text NOT NULL,
                    utility text NOT NULL,
                    mechanics text NOT NULL,
                    force text NOT NULL,
                    preparation text NOT NULL,
                    execution text NOT NULL,
                    comments text NOT NULL,
                    muscle_group_id text NOT NULL, 
                    media_url text NOT NULL, 
                    page_url text NOT NULL, 
                    PRIMARY KEY (id),
                    FOREIGN KEY (equipment_id)
                        REFERENCES equipment(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (muscle_group_id)
                        REFERENCES muscle_group(id)
                        ON DELETE CASCADE
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS muscle_exercise_relation(
                    id text NOT NULL,
                    PRIMARY KEY (id)
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS muscle_exercise(
                    exercise_id text NOT NULL,
                    muscle_id text NOT NULL,
                    muscle_group_id text NOT NULL, 
                    relation text NOT NULL,
                    PRIMARY KEY (exercise_id, muscle_id, muscle_group_id, relation),
                    FOREIGN KEY (exercise_id)
                        REFERENCES exercise(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (muscle_id)
                        REFERENCES muscle(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (muscle_group_id)
                        REFERENCES muscle_group(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (relation)
                        REFERENCES muscle_exercise_relation(id)
                        ON DELETE CASCADE
                )''')

    print("Tables created")

    print("Adding static values")

    cur.execute('''INSERT INTO muscle_exercise_relation VALUES ("target")''')
    cur.execute('''INSERT INTO muscle_exercise_relation VALUES ("synergist")''')
    cur.execute('''INSERT INTO muscle_exercise_relation VALUES ("stabilizer")''')
    cur.execute('''INSERT INTO muscle_exercise_relation VALUES ("dynamic_stabilizer")''')
    cur.execute('''INSERT INTO muscle_exercise_relation VALUES ("oblique_statbilizer")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("NeckWt","Neck")''')
    cur.execute('''INSERT INTO muscle VALUES ("Sternocleidomastoid","NeckWt","Sternocleidomastoid")''')
    cur.execute('''INSERT INTO muscle VALUES ("Splenius","NeckWt","Splenius")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("ShouldWt","Shoulders")''')
    cur.execute('''INSERT INTO muscle VALUES ("DeltoidAnterior","ShouldWt","Deltoid Anterior")''')
    cur.execute('''INSERT INTO muscle VALUES ("DeltoidLateral","ShouldWt","Deltoid Lateral")''')
    cur.execute('''INSERT INTO muscle VALUES ("DeltoidPosterior","ShouldWt","Deltoid Posterior")''')
    cur.execute('''INSERT INTO muscle VALUES ("Supraspinatus","ShouldWt","Supraspinatus")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("ArmWt","Upper Arms")''')
    cur.execute('''INSERT INTO muscle VALUES ("Triceps","ArmWt","Triceps Brachii")''')
    cur.execute('''INSERT INTO muscle VALUES ("Biceps","ArmWt","Biceps Brachii")''')
    cur.execute('''INSERT INTO muscle VALUES ("brachialis","ArmWt","Brachiallis")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("ForeArmWt","Forearms")''')
    cur.execute('''INSERT INTO muscle VALUES ("Brachioradialis","ForeArmWt","Brachioradialis")''')
    cur.execute('''INSERT INTO muscle VALUES ("WristFlexors","ForeArmWt","Wrist Flexors")''')
    cur.execute('''INSERT INTO muscle VALUES ("WristExtensors","ForeArmWt","Wrist Extensors")''')
    cur.execute('''INSERT INTO muscle VALUES ("Pronators","ForeArmWt","Pronators")''')
    cur.execute('''INSERT INTO muscle VALUES ("Supinators","ForeArmWt","Supinators")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("BackWt","Back")''')
    cur.execute('''INSERT INTO muscle VALUES ("BackGeneral","BackWt","General Back")''')
    cur.execute('''INSERT INTO muscle VALUES ("LatissimusDorsi","BackWt","Latissimus Dorsi")''')
    cur.execute('''INSERT INTO muscle VALUES ("TrapeziusUpper","BackWt","Trapezius Upper")''')
    cur.execute('''INSERT INTO muscle VALUES ("TrapeziusMiddle","BackWt","Trapezius Middle")''')
    cur.execute('''INSERT INTO muscle VALUES ("TrapeziusLower","BackWt","Trapezius Lower")''')
    cur.execute('''INSERT INTO muscle VALUES ("Rhomboids","BackWt","Rhomboids")''')
    cur.execute('''INSERT INTO muscle VALUES ("Infraspinatus","BackWt","Infraspinatus")''')
    cur.execute('''INSERT INTO muscle VALUES ("Subscapularis","BackWt","Subscapularis")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("ChestWt","Chest")''')
    cur.execute('''INSERT INTO muscle VALUES ("PectoralSternal","ChestWt","Pectoralis Major, Sternal")''')
    cur.execute('''INSERT INTO muscle VALUES ("PectoralClavicular","ChestWt","Pectoralis Major, Clavicular")''')
    cur.execute('''INSERT INTO muscle VALUES ("PectoralMinor","ChestWt","Pectoralis Minor")''')
    cur.execute('''INSERT INTO muscle VALUES ("SerratusAnterior","ChestWt","Serratus Anterior")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("WaistWt","Waist")''')
    cur.execute('''INSERT INTO muscle VALUES ("RectusAbdominis","WaistWt","Rectus Abdominis")''')
    cur.execute('''INSERT INTO muscle VALUES ("TraverseAbdominus","WaistWt","Traverse Abdominis")''')
    cur.execute('''INSERT INTO muscle VALUES ("Obliques","WaistWt","Obliques")''')
    cur.execute('''INSERT INTO muscle VALUES ("ErectorSpinae","WaistWt","Erector Spinae")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("HipsWt","Hips")''')
    cur.execute('''INSERT INTO muscle VALUES ("GluteusMaximus","HipsWt","Gluteus Maximus")''')
    cur.execute('''INSERT INTO muscle VALUES ("HipAbductor","HipsWt","Hip Abductor")''')
    cur.execute('''INSERT INTO muscle VALUES ("HipFlexors","HipsWt","Hip Flexors")''')
    cur.execute('''INSERT INTO muscle VALUES ("HipExternalRotator","HipsWt","Hip External Rotator")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("ThighWt","Thighs")''')
    cur.execute('''INSERT INTO muscle VALUES ("Quadriceps","ThighWt","Quadriceps")''')
    cur.execute('''INSERT INTO muscle VALUES ("Hamstrings","ThighWt","Hamstrings")''')
    cur.execute('''INSERT INTO muscle VALUES ("HipAdductors","ThighWt","Hip Adductors")''')

    cur.execute('''INSERT INTO muscle_group VALUES ("CalfWt","Calves")''')
    cur.execute('''INSERT INTO muscle VALUES ("Gastrocnemius","CalfWt","Gastrocnemius")''')
    cur.execute('''INSERT INTO muscle VALUES ("Soleus","CalfWt","Soleus")''')
    cur.execute('''INSERT INTO muscle VALUES ("TibialisAnterior","CalfWt","Tibialis Anterior")''')
    cur.execute('''INSERT INTO muscle VALUES ("Propliteus","CalfWt","Propliteus")''')

    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)

    con.commit()
    con.close()

    print("Initial db creation done")

def get_muscle_group_ids():
    con = conn()
    cur = con.cursor()
    cur.execute('''SELECT * FROM muscle_group''')
    rows = cur.fetchall()
    muscle_group_ids = [x[0] for x in rows]
    con.close()
    return muscle_group_ids

def insert_exercise(exercise):
    con = conn()
    cur = con.cursor()

    print('\n\n\nEXERCISE ', exercise['page_url'])

    exercise['name'] = exercise['name'].replace('\"','\'')
    exercise['preparation'] = exercise['preparation'].replace('\"','\'')
    exercise['execution'] = exercise['execution'].replace('\"','\'')
    exercise['comments'] = exercise['comments'].replace('\"','\'')

    s = '''INSERT INTO exercise VALUES (
                    "{exercise_id}",
                    "{equipment}",
                    "{name}",
                    "{utility}",
                    "{mechanics}",
                    "{force}",
                    "{preparation}",
                    "{execution}",
                    "{comments}",
                    "{target_muscle_group}",
                    "{media_url}",
                    "{page_url}"
                )'''.format(**exercise)
    print(s)

    try:
        cur.execute(s)
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            print('Ignoring duplicate. Known problems in website contents. ,e=', e)
        else:
            raise e

    print(exercise['muscles'])

    for em in exercise['muscles']:
        ea = {**exercise, **em}
        s = '''INSERT INTO muscle_exercise VALUES (
                        "{exercise_id}",
                        "{muscle_id}",
                        "{target_muscle_group}",
                        "{relation}"
                    )'''.format(**ea)
        print(s)
        try:
            cur.execute(s)
        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                print('Ignoring duplicate. Known problems in website contents. ,e=', e)
            else:
                raise e

    con.commit()
    con.close()

