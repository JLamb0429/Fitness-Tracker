#! python3

'''
This is the GUI of the program I am writing. The program creates a record of you're weight loss progress in an effort
to help you stay motivated to eat healthy and keep exercising.
'''

# import modules needed for the program. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import tkinter as tk
from tkinter import Menu, ttk
import Fitness_Tracker as ft


# Global Variables ~~~~~~~~~~~~~~~~~~~~~~ Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sex = ''
bio = ""
db_p = ''
# tkinter gui layout
win = tk.Tk()


# Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Create_db_profile():
    """ Create a new user profile """
    global db_p
    print("DB profile tester is working")
    print(name.info.get(), sex, height.info.get(), age.info.get())
    db_p = ft.Personal_data(name.info.get(), sex, height.info.get(), age.info.get())
    db_p.create_db()

def open_profile():
    """ open the profile of the current user."""
    global db_p
    print("open DB is working")
    db_p = ft.Personal_data(name.info.get(), sex, height.info.get(), age.info.get())
    print(name.info.get(), sex, height.info.get(), age.info.get())
    db_p.open_db()

def save_profile():
    """ used to write profile information to the database. """
    print("Writing profile")
    global db_p
    db_p.write_profile_to_db()

def write_weight():
    """ Function used to write the weight statistcs to the database.  """
    print("Write weight is working")
    global db_p
    print(f"Weight {weight.info.get()}, body fat {body_fat.info.get()}, bmi {bmi.info.get()}, Waist {waist.info.get()},chest {chest.info.get()}.")
    db_p.weight_stats(weight.info.get(), body_fat.info.get(), bmi.info.get(), waist.info.get(), chest.info.get())
    db_p.write_weight_stats_to_db()
    print("states writen")


def wright_bp():
    """ Function to write the blood pressure statistics to the database. """
    print(" writing to blood pressure")
    print(Systolic_data.info.get(), Dyastolic_data.info.get())
    db_p.Blood_Pressure(Systolic_data.info.get(), Dyastolic_data.info.get())
    db_p.write_blood_pressure_stats_to_db()

def gender_sex():
    global sex
    gend = gender.get()
    if gend:
        sex = "Male"
        print(sex)
    else:
        sex = "Female"
        print(sex)

def plot_Weight_data():
    db_p.plot_weight()

def plot_Fat_data():
    db_p.plot_BodyFat()

def plot_BodyMassIndex():
    db_p.plot_BMI()

def plot_BP():
    db_p.plot_Blood_Pressure()


# Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tabs class
class Tabs():
    """Tabs is intended to craft a series of tabs inside your tkinter main window. All Tabs created inside this class
    share the tabControl variable. They will be placed side by side.
    Inputs for this is var = Tabs( str(Tab name) )"""
    global win
    tabControl = ttk.Notebook(win)

    def __init__(self, tab_label):
        # loads the text into variable
        self.tab_label = tab_label
        # crafts teh tab
        self.tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab, text=self.tab_label)
        self.tabControl.pack(expand=1, fill='both')


class Data_input():
    """ This class is used to place a label and a Entry field in every box.
    var = Data_input(arg1, arg2, arg3)

    arg1 object parent item.tab,
    arg2 str label text,
    arg3 int row set placement,
    arg4 data type: str, int, float only options
    """
    def __init__(self, parent_item, label_text, item_row, data_type):
        self.parent_item, self.label_text, self.item_row, self.data_type = parent_item, label_text, item_row, data_type

        if type(self.data_type) == str:
            self.info = tk.StringVar()
        elif type(self.data_type) == int:
            self.info = tk.IntVar()
        else:
            self.info = tk.DoubleVar()

        self.label = ttk.Label(self.parent_item, text=self.label_text).grid(column=0, row= self.item_row)
        self.info = tk.StringVar()
        self.Entry = ttk.Entry(self.parent_item, width=24, textvariable=self.info).grid(column=1, columnspan=2, row= self.item_row)


class action_button():
    """
    This is used to make tkinter buttons. quickly and easily.
    """
    def __init__(self, button_title, parent, function, col=0, row=0,):
        self.button_title, self.parent, self.function, self.col, self.row = button_title, parent, function, col, row
        ttk.Button(self.parent, text=self.button_title, command=self.function).grid(column=self.col, row=self.row)





win.title("Health stats tracker")
# Button Functions. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Menu bar layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
menuBar = Menu(win)
win.config(menu=menuBar)

'''
# File menu cascading menu button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fileMenu = Menu(menuBar, tearoff=0) # configures the file button settings
fileMenu.add_command(label="New") # this is the first command in the cascading file menu.
fileMenu.add_separator() # this text adds a line separating the commands below.
fileMenu.add_command(label="Open Progress tracker")
fileMenu.add_separator()
fileMenu.add_command(label="Save Progress tracker")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menuBar.add_cascade(label='File', menu=fileMenu)


# Help menu cascading button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label='Help', menu=helpMenu)
'''





#(Start)~~~~~~~~~~~ tabs layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

personal_info = Tabs('Personal info')
Weekly_data = Tabs('Weekly data entry')
Blood_pressure = Tabs('Blood Pressure')
progress_charts = Tabs('progress charts')

#(End)~~~~~~~~~~~ tabs layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






#(Start)~~~~~~~~~~~ personal data tab layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Personal Info fields ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name = Data_input(personal_info.tab, "Name", 1, "")
height = Data_input(personal_info.tab, "height inches", 2, 0)
age = Data_input(personal_info.tab, "Age", 3, 0)

gender = tk.BooleanVar()
male_check = ttk.Radiobutton(personal_info.tab, text="Male", variable=gender, value=True, command=gender_sex).grid(row=4,column=0)
female_check = ttk.Radiobutton(personal_info.tab, text="Female", variable=gender, value=False, command=gender_sex ).grid(row=4,column=1)


# Personal data buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
new_profile = action_button("New_profile", personal_info.tab, Create_db_profile, 0, 5)
write_profile = action_button("Write_profile", personal_info.tab, save_profile, 1, 5)
open_profile = action_button("open_profile", personal_info.tab, open_profile, 2, 5)


#(End)~~~~~~~~~~~ personal data tab layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#(Start)~~~~~~~~~~~ Weekly data tab layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Weekly data Fields ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

weight = Data_input(Weekly_data.tab, "Weight lbs", 1, 0.0)
body_fat = Data_input(Weekly_data.tab, "Body fat %", 2, 0.0)
bmi = Data_input(Weekly_data.tab, "BMI", 3, 0.0)
waist = Data_input(Weekly_data.tab, "waist size", 4, 0.0)
chest = Data_input(Weekly_data.tab, "chest size", 5, 0.0)

# Weekly stats buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submit_Data = action_button("Submit Data", Weekly_data.tab, write_weight, 0, 6)


#(End)~~~~~~~~~~~ Weekly data tab layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#(Start)~~~~~~~~~~~ blood pressure personal data tab layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Systolic_data = Data_input(Blood_pressure.tab, "Systolic Data (top number)", 1, "")
Dyastolic_data = Data_input(Blood_pressure.tab, "Dyastolic Data (bottom number)", 2, "")

Submit_Data = action_button("Submit Data", Blood_pressure.tab, wright_bp, 0, 5)

#(End)~~~~~~~~~~~ blood pressure personal data tab layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#(Start)~~~~~~~~~~ Progress charts data tablayout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt_Weight = action_button("Plot Weight", progress_charts.tab, plot_Weight_data, 0, 0)
plt_bodyFat = action_button("Plot Body Fat", progress_charts.tab, plot_Fat_data, 1, 0)
plt_BMI = action_button("Plot BMI", progress_charts.tab, plot_BodyMassIndex, 0, 1)
plt_BMI = action_button("Plot Blood", progress_charts.tab, plot_BP, 1, 1)



#(End)~~~~~~~~~~ Progress charts data tablayout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Run the main loop allowing the tk window to open and stay open unless the close button is pressed. ~~~~~~~~~~~~
win.mainloop()
