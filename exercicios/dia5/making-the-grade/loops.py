import functools


def round_scores(student_scores):

    return [round(rounded) for rounded in student_scores]
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """


def count_failed_students(student_scores):

    count = functools.reduce(lambda acc, grade: acc if grade > 40 else acc+1 , student_scores,0)

    return count
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """


def above_threshold(student_scores, threshold):

    return [grade for grade in student_scores if grade >= threshold]
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """


def letter_grades(highest):

    div = (highest - 40)/4

    groups = [int(41 + (div*(i))) for i in range(4)]

    return groups


    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:
             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """


def student_ranking(student_scores, student_names):

    result = []

    for index,student in enumerate(student_names):

        str = f'{index+1}. {student}: {student_scores[index]}'
        result.append(str)

    return result

    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """



def perfect_score(student_info):

    for student in student_info:

        if student[1] == 100:
            return student

    return []

    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """



