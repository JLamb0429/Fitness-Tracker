
import sqlite3, datetime

conn = ""

def create_SQLITE_db(name):
    """
    :Purpose is to create a new database to track weight loss information.
    :param name:(User name for the new fitness database)
    :return: nothing but a new SQLite.db file name_fitness_data.db
    """

    data_base_name = str(name+"_fitness_data.db")
    conn = sqlite3.connect(data_base_name)

    # cursor is how we interact with our SQLite database
    c = conn.cursor()

    # inside the c.execute file in a doc string we will write SQL code
    c.execute("""CREATE TABLE PROFILE (
                name text,
                height integer,
                gender text
                )""")

    c.execute("""CREATE TABLE WEIGHT_TRACKER (
                date text,
                weight real,
                body_fat real,
                BMI real,
                waist real,
                chest real
                )""")

    c.execute("""CREATE TABLE BLOOD_PRESSURE_TRACKER (
                    date text,
                    Systolic integer,
                    Dyastolic integer
                    )""")

    # commit completes the current transaction nothing is written until you commit.
    conn.commit()

    # finish by closing the data base
    conn.close()

def open_db(name):
    """ this function opens the data base for us """
    return sqlite3.connect(str(name+"_fitness_data.db"))

def open_conn(name):
    global conn
    conn = open_db(name)

def save_conn():
    with conn:
        conn.commit()

def close_conn():
    """ This function saves aka "commits" and closes the database for us."""
    with conn:
        conn.close()

def write_profile_to_db(name, height, gender):
    """ Write profile values to the sqlite database  """
    with conn:
        c = conn.cursor()
        c.execute(f"INSERT INTO PROFILE VALUES ('{name}',{height}, '{gender}')")
        save_conn()

def write_weekly_stats_to_db(date, weight, body_fat, BMI, waist, chest):
    """ Write values to the sqlite database
                """
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO WEIGHT_TRACKER VALUES (?,?,?,?,?,?)",(date, weight, body_fat, BMI, waist, chest))
        save_conn()

def write_blood_pressure_stats_to_db(date, syst, dyas):
    """ Write values to the sqlite database
                """
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO BLOOD_PRESSURE_TRACKER VALUES (?,?,?)",(date, syst, dyas))
        save_conn()

def get_current_date():
    current_time = datetime.datetime.now()
    return f"{current_time.year}-{current_time.month}-{current_time.day}"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Recall / read the database functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_weight():
    with conn:
        c = conn.cursor()
        c.execute("SELECT date, weight FROM WEIGHT_TRACKER")
        print(c.fetchall())

def get_waist():
    with conn:
        c = conn.cursor()
        c.execute("SELECT date, waist FROM WEIGHT_TRACKER")
        print(c.fetchall())


def get_chest():
    with conn:
        c = conn.cursor()
        c.execute("SELECT date, chest FROM WEIGHT_TRACKER")
        print(c.fetchall())

def get_fat():
    with conn:
        c = conn.cursor()
        c.execute("SELECT date, body_fat FROM WEIGHT_TRACKER")
        print(c.fetchall())

def get_BMI():
    with conn:
        c = conn.cursor()
        c.execute("SELECT date, BMI FROM WEIGHT_TRACKER")
        print(c.fetchall())




'''
create_SQLITE_db("Josh")
write_profile_to_db("Josh", 73, "Male")
write_weekly_stats_to_db("Josh", "2019-03-17", 248, 29.6, 32, 48, 43)
write_weekly_stats_to_db("Josh", "2019-03-24", 250, 30,32.6,48,43.5)
write_blood_pressure_stats_to_db("Josh", "2019-04-2019", 124, 81)
write_blood_pressure_stats_to_db("Josh", "2019-04-2019", 133, 73)
write_weekly_stats_to_db("2019-03-31", 247, 29.4,32.1,47,45.25)
'''


