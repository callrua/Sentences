
def check_capital_letter(sentence):
    print('Confirming sentence begins with a capital letter...')
    if sentence[0].isupper():
        print('PASS')
    else:
        print('FAIL: Sentence does not begin with a capital letter!')


def check_quotation_marks(sentence):
    print(sentence)


def check_period(sentence):
    print(sentence)


def check_no_other_period(sentence):
    print(sentence)


def check_numbers(sentence):
    print(sentence)


if __name__ == '__main__':
    sentence_to_validate = input('Enter string to validate: ')
    check_capital_letter(sentence_to_validate)