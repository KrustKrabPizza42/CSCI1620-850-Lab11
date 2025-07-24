from tkinter import *
import csv
import os.path

#class to make a window for the data input
class Gui:

    def __init__(self, window):
        self.window = window
        
        self.frame_one = Frame(self.window)
        self.one_subframe_one = Frame(self.window)
        self.input_name = Entry(self.frame_one)
        self.name_label = Label(self.frame_one, text='Name: ', width=5)
        self.name_label.pack(side='left')
        self.input_name.pack(side='left')
        self.frame_one.pack(padx=10, pady=10, fill=BOTH)

        self.frame_two = Frame(self.window)
        self.input_age = Entry(self.frame_two)
        self.age_label = Label(self.frame_two, text='Age: ', width=5)
        self.age_label.pack(side='left')
        self.input_age.pack(side='left')
        self.frame_two.pack(padx=10, pady=10, fill=BOTH)

        self.frame_three = Frame(self.window)
        self.radio_value = IntVar()
        self.radio_value.set(0)
        self.status_label = Label(self.frame_three, text='Status')
        self.radio_student = Radiobutton(self.frame_three, text='Student', variable=self.radio_value, value=1)
        self.radio_staff = Radiobutton(self.frame_three, text='Staff', variable=self.radio_value, value=2)
        self.radio_both = Radiobutton(self.frame_three, text='Both', variable=self.radio_value, value=3)
        self.status_label.pack(side='left')
        self.radio_student.pack(side='left')
        self.radio_staff.pack(side='left')
        self.radio_both.pack(side='left')
        self.frame_three.pack(padx=5, pady=5)

        self.frame_four = Frame(self.window)
        self.save_button = Button(self.frame_four, text='Save', command = self.submit)
        self.save_button.pack()
        self.frame_four.pack(padx=5, pady=5)

        self.frame_five = Frame(self.window)
        self.form_label = Label(self.frame_five, text='Please fill out all values')
        self.form_label.pack()
        self.frame_five.pack(padx=5, pady=5)
    
    def submit(self):

        #Section to get name input
        self.__name = self.input_name.get().strip()

        if self.__name == '':
            self.__name = 'Anonymous'

        
        #section to set value of status based on which radio button is selected
        if self.radio_value.get() == 1:

            self.__status = 'Student'
        
        elif self.radio_value.get() == 2:
            
            self.__status = 'Staff'

        elif self.radio_value.get() == 3:

            self.__status = 'Both'
    
        else:
        
            self.__status = 'N/A'

        #try catch to catch a value error when converting to int
        try:
            self.__age = int(self.input_age.get().strip())

            if self.__age < 0:
                raise ValueError
        
        except ValueError:
            
            self.form_label.config(text='Enter correct age value')

        #only attempts to save data if not value error is raised
        else:

            self.get_data_dict()

            self.save_to_file()

            self.input_name.delete(0, END)
            self.input_age.delete(0, END)
            self.radio_value = 0
            self.form_label.config(text='')

    #method just to fill out a dictionary
    def get_data_dict(self):

        self.__data_dictionary = {'Name': self.__name, 'Age': self.__age, 'Status': self.__status}

    
    #method to save the dictionary to a csv file using a dictwriter
    def save_to_file(self):

        

        if os.path.isfile('data.csv'):

            with open('data.csv', 'a', newline='') as csvfile:

                writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Age', 'Status'])

                writer.writerow(self.__data_dictionary)
        
        else:

            with open('data.csv', 'w', newline='') as csvfile:

                writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Age', 'Status'])

                writer.writeheader()

                writer.writerow(self.__data_dictionary)