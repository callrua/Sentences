
import re


def check_capital_letter(sentence):
    print('Confirming sentence begins with a capital letter...')
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
    print(sentence)


def check_numbers(sentence):
    print(sentence)


if __name__ == '__main__':
    sentence_to_validate = input('Enter string to validate: ')
    check_capital_letter(sentence_to_validate)
    check_period_at_end(sentence_to_validate)
    check_quotation_marks(sentence_to_validate)