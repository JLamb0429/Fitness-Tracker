#! python3

import datetime, sqlite3
import matplotlib.pyplot as plt


def get_date():
    """ this function gets the current date and formats it for the database """
    date_time = datetime.datetime.now()
    months_list = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    return "%4d-%02d-%02d" % (date_time.year, date_time.month, date_time.day)


class Personal_data():
    """ This predefines the personal data of the user.
    """
    def __init__(self, name, gender, height, age):
        self.name = name
        self.gender = gender
        self.height = height
        self.age = age
        self.db = str(self.name + "_fitness_data.db")

    def __str__(self):
        return f"Name: {self.name}, \nGender: {self.gender}, \nHeight: {self.height}, \nAge: {self.age}"

    #! ~~~~~~~~~~~ dtat base basic functuions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def open_db(self):
        """ this function opens the data base for us """
        self.conn = sqlite3.connect(self.db)
        print(self.conn, " is open")

    def close_conn(self):
        """ This function saves aka "commits" and closes the database for us."""
        self.conn.close()
        print(self.conn, " is closed")

    def save_conn(self):
        """  This function commits the data to the database. """
        self.conn.commit()
        print (self.conn," is saved")

    #! ~~~~~~~~~ start / write db ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def create_db(self):
        """
        :Purpose is to create a new database to track weight loss information.
        :param name:(User name for the new fitness database)
        :return: nothing but a new SQLite.db file name_fitness_data.db
        """

        self.open_db()

        # cursor is how we interact with our SQLite database
        c = self.conn.cursor()

        # inside the c.execute file in a doc string we will write SQL code
        c.execute("""CREATE TABLE PROFILE (
                    name text,
                    age integer, 
                    gender text,
                    height integer
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
        self.save_conn()

        # finish by closing the data base
        self.close_conn()


    def write_profile_to_db(self):
        """ Write profile values to the sqlite database  """
        self.open_db()
        c = self.conn.cursor()
        c.execute(f"INSERT INTO PROFILE VALUES ('{self.name}',{self.age},'{self.gender}',{self.height})")
        self.save_conn()


    #! ~~~~~~~~~~~~ create weekly weight stats and write to db ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def weight_stats(self, weight, body_fat, bmi, waist,chest):

        """
        This method crates the weigh in stats for input to the database.
        :param weight: insert your weight value in (float) lbs
        :param waist: insert your waist in (float) inches
        :param chest: insert your chest size in (float) inches
        :param body_fat: insert your body fat (float) percent
        :param bmi: insert your BMI (float)
        """
        self.date = get_date()
        self.weight = weight
        self. body_fat = body_fat
        self.bmi = bmi
        self.waist = waist
        self.chest = chest

        self.healthStats = (self.date, self.weight, self.body_fat, self.bmi, self.waist, self.chest)


    def write_weight_stats_to_db(self):
        """ Write weight values to the sqlite database
                    """
        self.open_db()
        c = self.conn.cursor()
        c.execute("INSERT INTO WEIGHT_TRACKER VALUES (?,?,?,?,?,?)", self.healthStats)
        self.save_conn()


    #! ~~~~~~~~~~~~~~~ create blood pressure stats and write to db ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def Blood_Pressure(self, syst, dyas):
        """ Writes your blood pressure statistics to the database. """
        self.syst = syst
        self.dyas = dyas

        #self.date = date

        self.bp = (get_date(), self.syst, self.dyas)

    def write_blood_pressure_stats_to_db(self):
        """ Write blood pressure values to the sqlite database"""
        self.open_db()
        c = self.conn.cursor()
        c.execute("INSERT INTO BLOOD_PRESSURE_TRACKER VALUES (?,?,?)", self.bp)
        self.save_conn()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~ Get data from the db ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get_dates(self):
        c = self.conn.cursor()
        c.execute("SELECT date FROM WEIGHT_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def get_weight(self):
        c = self.conn.cursor()
        c.execute("SELECT weight FROM WEIGHT_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def get_waist(self):
        c = self.conn.cursor()
        c.execute("SELECT waist FROM WEIGHT_TRACKER")
        print(c.fetchall())
        return c.fetchall()

    def get_chest(self):
        c = self.conn.cursor()
        c.execute("SELECT chest FROM WEIGHT_TRACKER")
        print(c.fetchall())
        return c.fetchall()

    def get_fat(self):
        c = self.conn.cursor()
        c.execute("SELECT body_fat FROM WEIGHT_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def get_BMI(self):
        c = self.conn.cursor()
        c.execute("SELECT BMI FROM WEIGHT_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def get_BP_date(self):
        c = self.conn.cursor()
        c.execute("SELECT date FROM BLOOD_PRESSURE_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def get_BP_dyas(self):
        c = self.conn.cursor()
        c.execute("SELECT Dyastolic FROM BLOOD_PRESSURE_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def get_BP_syst(self):
        c = self.conn.cursor()
        c.execute("SELECT Systolic FROM BLOOD_PRESSURE_TRACKER")
        x = self.format_list(c.fetchall())
        print(x)
        return x

    def format_list(self, list):
        """ Sort DB list to remove tupils items and place them in a new list and return them."""
        form = []
        for i in range(0, len(list)):
            form.append(list[i][0])
        return form

    #~~~~~~~~~~ Plot stats ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def plot_weight(self):
        """ Plots weight and date statistics """
        x = self.get_dates()
        y = self.get_weight()
        plt.plot(x, y)
        plt.show()

    def plot_BodyFat(self):
        """ Plots Body fat and date statistics"""
        x = self.get_dates()
        y = self.get_fat()
        plt.plot(x, y)
        plt.show()

    def plot_BMI(self):
        """ Plot BMI and date statistics"""
        x = self.get_dates()
        y = self.get_BMI()
        plt.plot(x, y)
        plt.show()

    def plot_waist(self):
        x = self.get_dates()
        y = self.get_fat()
        plt.plot(x, y)
        plt.show()

    def plot_chest(self):
        x = self.get_dates()
        y = self.get_fat()
        plt.plot(x, y)
        plt.show()

    def plot_Blood_Pressure(self):
        x = self.get_BP_date()
        y = self.get_BP_dyas()
        z = self.get_BP_syst()
        plt.plot(x, y)
        plt.plot(x, z)
        plt.show()
        pass



#Josh = Personal_data("Josh","Male",73, 34)
#Josh.create_db()
#Josh.weight_stats("2019-03-17", 248, 48, 43, 29.6, 32)
#Josh.weight_stats("2019-03-24", 250,48, 43.5, 30,32.6)
#Josh.weight_stats("2019-03-31", 247, 47,45.25, 29.4,32.1)
#Josh.weight_stats("2019-04-07", 243, 47, 44, 28.8, 31.6)

#Josh.write_weight_stats_to_db()

#Josh.Blood_Pressure("2019-04-19", 124, 81)
#Josh.Blood_Pressure("2019-04-19", 133, 73)
#Josh.write_blood_pressure_stats_to_db()
