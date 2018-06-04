import re
import argparse
import sys

def check_capital_letter(sentence):
    #print('Confirming sentence begins with a capital letter...')
    if sentence[0].isupper():
        print('PASS: Sentence begins with a capital letter.')
    else:
        print('FAIL: Sentence does not begin with a capital letter!')


def check_quotation_marks(sentence):
    if sentence.count('"') % 2 == 0:
        print('PASS: Sentence has an even number of quotation marks.')
    else:
        print('FAIL: Sentence has an odd number of quotation marks!')


def check_period_at_end(sentence):
    if sentence[-1] == '.':
        print('PASS: Sentence ends with a period.')
    else:
        print('FAIL: Sentence does not end with a period!')


def check_no_other_period(sentence):
    period = sentence.find('.')
    if period == len(sentence)-1:
        print('PASS: Sentence has no other periods aside from ending character.')
    elif period == -1:
        print('FAIL: Sentence contains no period at all!')
    else:
        print('FAIL: Sentence contains a period out of place!')


def check_numbers(sentence):
    """ Numbers below 13 are spelled out (”one”, “two”, &quot;three”, etc…)"""
    numbers = re.findall(r'\d+', sentence)
    fail = False
    for number in numbers:
        if int(number) < 13:
            fail = True
            print('FAIL: Sentence contains numbers less than 13 not spelled out!')
            break

    if not fail:
        print('PASS: Numbers spelled correctly')


def run_all_checks(sentence):
    print("\nChecking the following sentence: " + sentence)
    check_capital_letter(sentence)
    check_period_at_end(sentence)
    check_quotation_marks(sentence)
    check_no_other_period(sentence)
    check_numbers(sentence)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        sentence_to_validate = input('Enter string to validate: ')
        run_all_checks(sentence_to_validate.strip())
    else:
        file_to_validate = sys.argv[1]
        try:
            f = open(file_to_validate)
            sentence_to_validate = f.readline()
            while sentence_to_validate:
            #print("\nChecking the following sentence: " + sentence_to_validate)
                run_all_checks(sentence_to_validate.strip())
                sentence_to_validate = f.readline()
            f.close()
        except OSError as e:
            print("Exception occurred as file " + file_to_validate + " does not exist!")


    #sentence_to_validate = input('Enter string to validate: ')
    #check_capital_letter(sentence_to_validate)
    #check_period_at_end(sentence_to_validate)
    #check_quotation_marks(sentence_to_validate)
    #check_no_other_period(sentence_to_validate)
    #check_numbers(sentence_to_validate)
