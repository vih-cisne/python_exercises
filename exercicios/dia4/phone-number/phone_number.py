import functools
import re

class PhoneNumber:
    def __init__(self, number):
        self.number = self.format_number(number)

    def format_number(self, number):

        number_clean = re.sub(r"-", " ", number)
        number_clean = re.sub(r"""[.+]""", " ", number_clean)
        number_clean = re.sub(r"""[()]""", "", number_clean)
        
        groups = number_clean.split()
        self.handle_errors(groups)

        if len(groups) > 3:
            groups = groups[len(groups)-3:]
        

        number_formated = ''.join(groups)
        return number_formated

    def handle_errors(self, number_groups):

        len_words = functools.reduce(lambda acc, group: acc+len(group), number_groups,0)

        if len(number_groups) == 1:
            if len(number_groups[0]) == 11:
                exchange = number_groups[0][1]
                area = number_groups[0][4]
            else:
                exchange = number_groups[0][0]
                area = number_groups[0][3]

        else:
            exchange = number_groups[0]
            area = number_groups[1]

        if len_words < 10:
            raise ValueError("incorrect number of digits")
        if len_words > 11:
            raise ValueError("more than 11 digits")
        if len_words == 11 and not number_groups[0].startswith('1'):
            raise ValueError("11 digits must start with 1")
        else:
            if exchange.startswith('0'):
                raise ValueError("area code cannot start with zero")
            if exchange.startswith('1'):
                raise ValueError("area code cannot start with one")
            if area.startswith('0'):
                raise ValueError("exchange code cannot start with zero")
            if area.startswith('1'):
                raise ValueError("exchange code cannot start with one")





# if a phone number has punctuation in place of some digits.
#raise ValueError("punctuations not permitted")
# if a phone number has letters in place of some digits.
#raise ValueError("letters not permitted")


