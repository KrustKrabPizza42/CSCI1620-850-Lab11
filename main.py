from tkinter import *
from gui import *

def save_to_file(data_dictionary):

    pass


def main():
    window = Tk()
    window.title('Lab 10')
    window.geometry('240x220')
    window.resizable(False, False)
    new_gui = Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()