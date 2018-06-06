from tkinter import *
import re

import sys
import GUI


def check_capital_letter(sentence):
    if sentence[0].isupper():
        return True
    else:
        return False


def check_quotation_marks(sentence):
    if sentence.count('"') % 2 == 0:
        return True
    else:
        return False


def check_period_at_end(sentence):
    if sentence[-1] == '.':
        return True
    else:
        return False


def check_no_other_period(sentence):
    period = sentence.find('.')
    if period == len(sentence)-1:
        return True
    else:
        return False


def check_numbers(sentence):
    """ Numbers below 13 are spelled out (”one”, “two”, &quot;three”, etc…)"""
    numbers = re.findall(r'\d+', sentence)
    fail = False
    for number in numbers:
        if int(number) < 13:
            fail = True
            break

    if not fail:
        return True
    else:
        return False


def run_all_checks(sentence):
    print("\nChecking the following sentence: " + sentence)
    if check_capital_letter(sentence):
        print('PASS: Sentence begins with a capital letter.')
    else:
        print('FAIL: Sentence does not begin with a capital letter!')

    if check_period_at_end(sentence):
        print('PASS: Sentence ends with a period.')
    else:
        print('FAIL: Sentence does not end with a period!')

    if check_quotation_marks(sentence):
        print('PASS: Sentence has an even number of quotation marks.')
    else:
        print('FAIL: Sentence has an odd number of quotation marks!')

    if check_no_other_period(sentence):
        print('PASS: Sentence has no other periods aside from ending character.')
    else:
        print('FAIL: Sentence contains a period out of place, or no period at all!')

    if check_numbers(sentence):
        print('PASS: Numbers spelled correctly')
    else:
        print('FAIL: Sentence contains numbers less than 13 not spelled out!')


def validate_file(file_to_validate):
    try:
        f = open(file_to_validate)
        sentence_to_validate = f.readline()
        while sentence_to_validate:
            # print("\nChecking the following sentence: " + sentence_to_validate)
            run_all_checks(sentence_to_validate.strip())
            sentence_to_validate = f.readline()
        f.close()
    except OSError as e:
        print("Exception occurred as file " + file_to_validate + " does not exist!")


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        root = Tk()
        gui = GUI.ValidateGUI(root)
        root.mainloop()
    else:
        validate_file(sys.argv[1])

















    #sentence_to_validate = input('Enter string to validate: ')
    #check_capital_letter(sentence_to_validate)
    #check_period_at_end(sentence_to_validate)
    #check_quotation_marks(sentence_to_validate)
    #check_no_other_period(sentence_to_validate)
    #check_numbers(sentence_to_validate)
