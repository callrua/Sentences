from tkinter import *

import main as validator

#C:\Users\Roo\Desktop\valid_sentences.txt
class ValidateGUI:

    def __init__(self, master):

        top_frame = Frame(master)
        top_frame.pack(pady=20)
        bottom_frame = Frame(master)
        bottom_frame.pack(pady=20, side=BOTTOM)

        self.entry_id = StringVar()
        #entry = Entry(top_frame, textvariable=self.entry_id)
        self.entry = Entry(top_frame)
        self.entry.pack(side=LEFT)
        validate_button = Button(top_frame, text="Validate sentence")
        validate_button.bind("<Button-1>", self.validate_entry)
        validate_button.pack(side=RIGHT, )

        self.label_one = Label(bottom_frame, text="String starts with a capital letter", justify=LEFT)
        self.label_one.pack()

        self.label_two = Label(bottom_frame, text="String has an even number of quotation marks", justify=LEFT)
        self.label_two.pack()

        self.label_three = Label(bottom_frame, text="String ends with a period character \".\"", justify=LEFT)
        self.label_three.pack()

        self.label_four = Label(bottom_frame, text="String has no period characters other than the last character", justify=LEFT)
        self.label_four.pack()

        self.label_five = Label(bottom_frame, text="Any numbers below 13 are spelled out.", justify=LEFT)
        self.label_five.pack()

    def validate_entry(self, event):
        if validator.check_capital_letter(self.entry.get()):
            self.label_one.config(bg="green")
        else:
            self.label_one.config(bg="red")

        if validator.check_quotation_marks(self.entry_id.get()):
            self.label_two.config(bg="green")
        else:
            self.label_two.config(bg="red")

        if validator.check_period_at_end(self.entry.get()):
            self.label_three.config(bg="green")
        else:
            self.label_three.config(bg="red")

        if validator.check_no_other_period(self.entry.get()):
            self.label_four.config(bg="green")
        else:
            self.label_four.config(bg="red")

        if validator.check_numbers(self.entry.get()):
            self.label_five.config(bg="green")
        else:
            self.label_five.config(bg="red")
