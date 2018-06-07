from tkinter import *

import validator


class ValidateGUI:

    def __init__(self, master):

        top_frame = Frame(master)
        top_frame.pack(pady=20)
        bottom_frame = Frame(master)
        bottom_frame.pack(pady=20, side=BOTTOM)

        self.entry_id = StringVar()
        self.entry = Entry(top_frame, width=40)
        self.entry.insert(END, "Enter sentence & click button to validate")
        self.entry.pack(side=LEFT)

        validate_button = Button(top_frame, text="Validate sentence")
        validate_button.bind("<Button-1>", self.validate_entry)
        validate_button.pack(side=RIGHT)

        self.capitals_label = Label(bottom_frame, text="String starts with a capital letter", justify=LEFT)
        self.capitals_label.pack(padx=20)

        self.quotes_label = Label(bottom_frame, text="String has an even number of quotation marks", justify=LEFT)
        self.quotes_label.pack(padx=20)

        self.end_period_label = Label(bottom_frame, text="String ends with a period character \".\"", justify=LEFT)
        self.end_period_label.pack(padx=20)

        self.misplaced_period_label = Label(bottom_frame,
                                            text="String has no period characters other than the last character",
                                            justify=LEFT)
        self.misplaced_period_label.pack(padx=20)

        self.numbers_label = Label(bottom_frame, text="Any numbers below 13 are spelled out.", justify=LEFT)
        self.numbers_label.pack(padx=20)

    def validate_entry(self, event):
        if validator.check_capital_letter(self.entry.get()):
            self.capitals_label.config(bg="green")
        else:
            self.capitals_label.config(bg="red")

        if validator.check_quotation_marks(self.entry.get()):
            self.quotes_label.config(bg="green")
        else:
            self.quotes_label.config(bg="red")

        if validator.check_period_at_end(self.entry.get()):
            self.end_period_label.config(bg="green")
        else:
            self.end_period_label.config(bg="red")

        if validator.check_no_other_period(self.entry.get()):
            self.misplaced_period_label.config(bg="green")
        else:
            self.misplaced_period_label.config(bg="red")

        if validator.check_numbers(self.entry.get()):
            self.numbers_label.config(bg="green")
        else:
            self.numbers_label.config(bg="red")


if __name__ == '__main__':
    root = Tk()
    root.title("Sentence Validator")
    root.geometry("400x210")
    gui = ValidateGUI(root)
    root.mainloop()
