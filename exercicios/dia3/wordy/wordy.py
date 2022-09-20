import operator as oper
import re

operations = { "plus": oper.add, "minus": oper.sub, 'multiplied': oper.mul, 'divided': oper.floordiv, 'raised': oper.pow, 'squared': oper.pow, 'square': oper.pow }

def answer(question):
    question_without_marks = getting_str_without_marks(question)
    words = question_without_marks.split()
    result = None
    
    check_non_questions(words)

    for i, word in enumerate(words):
        
        if word == 'squared' or (word == 'square' and words[i+1] == 'root'):
            result = squares(word, result, words, i)
            continue
            
        if is_a_number(word) and not is_the_last(i,words):
            operation = words[i+1]
            if is_a_number(operation):
                raise ValueError("syntax error")
            if  operation not in operations:
                raise ValueError("unknown operation")
        elif is_a_number(word) and is_the_last(i,words):
            if result == None:
                result = float(word)
        if word in operations:
            number_next = get_number_next(words, i, word)  
            number_prev = words[i-1]
            try:
                result = get_result(result, number_prev, float(number_next), word)
            except:
                raise ValueError("syntax error")
    
    if result == None:
        raise ValueError("syntax error")

    return format_result(result)


def getting_str_without_marks(str):
    return  re.sub(r"""[!?'".<>(){}@%&*/[/]""", "", str)

def check_non_questions(words):
    non_accepted_questions = ['who', 'where']

    for question in non_accepted_questions:
        if words[0].lower() == question:
            raise ValueError("unknown operation")

def is_a_number(str):
    return str[-1].isdigit()

def get_result(result, number_prev, number_next, operation):
    if result == None:
        return operations[operation](float(number_prev), number_next)
    else: 
        return operations[operation](result, number_next)

def is_the_last(index, list):
    return index == len(list) - 1 

def squares(word, result, words, i):
    if word == 'squared':
        return get_result(result, words[i-1], 2, word)
    else:
        try:
            number = words[i+3]
            #if words[i+2] == 'of' and is_a_number(number):
            return get_result(result, number, 0.5, word)
        except:
            raise ValueError("syntax error")

def get_number_next(words, i, word):

    if is_the_last(i,words):
        raise ValueError("syntax error")
    try:
        if words[i+1] == 'by':
            return float(words[i+2])
        elif is_a_number(words[i+1]):
            return float(words[i+1])
        elif word == 'raised':
            if is_a_number(words[i+2]):
                return float(words[i+2])
            else:
                return float(words[i+3][:-2])
    except:
        raise ValueError("syntax error")

def format_result(num):
  if num % 1 != 0:
    return num
  else:
    return int(num)

#print(answer("What is the square root of 9?"))


        


