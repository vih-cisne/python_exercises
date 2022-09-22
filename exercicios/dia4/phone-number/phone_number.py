import functools
import re

class PhoneNumber:
    def __init__(self, number):
        self.number = self.format_number(number)

    def pretty(self):
        number_pretty = "({})-{}-{}".format( self.area_code, self.exchange, self.subscriber_number)

        return number_pretty

    def format_number(self, number):

        number_clean = re.sub(r"-", " ", number)
        number_clean = re.sub(r"[.+]", " ", number_clean)
        number_clean = re.sub(r"[()]", "", number_clean)
        
        groups = number_clean.split()

        if len(groups) == 4:
            if not groups[0] == '1':
                    raise ValueError("11 digits must start with 1")
            groups = groups[len(groups)-3:]
        if len(groups) == 1:
            if len(groups[0]) == 11:
                if not groups[0].startswith('1'):
                    raise ValueError("11 digits must start with 1")
                groups[0] = groups[0][1:]
        

        number_formated = ''.join(groups)

        self.errors_letters_or_punctuations(number_formated)
        self.handle_errors(groups)

        return number_formated

    def handle_errors(self, number_groups):

        len_words = functools.reduce(lambda acc, group: acc+len(group), number_groups,0)

        if len(number_groups) == 1:
            number_groups = [number_groups[0][0:3],number_groups[0][3:6], number_groups[0][6:10]]

        self.exchange = number_groups[1]
        self.area_code = number_groups[0]
        self.subscriber_number = number_groups[2]

        if len_words < 10:
            raise ValueError("incorrect number of digits")
        if len_words > 11:
            raise ValueError("more than 11 digits")
        else:
            if self.area_code.startswith('0'):
                raise ValueError("area code cannot start with zero")
            if self.area_code.startswith('1'):
                raise ValueError("area code cannot start with one")
            if self.exchange.startswith('0'):
                raise ValueError("exchange code cannot start with zero")
            if self.exchange.startswith('1'):
                raise ValueError("exchange code cannot start with one")

    def errors_letters_or_punctuations(self, number):
        finded_letters = re.search(r"[a-zA-Z]", number)
        finded_punctuations = re.search(r"[?@_:!]", number)

        if finded_letters != None:
            raise ValueError("letters not permitted")
        if finded_punctuations != None:
            raise ValueError("punctuations not permitted")







