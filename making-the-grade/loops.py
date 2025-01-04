"""Functions for organizing and calculating student exam scores."""

import math
def round_scores(student_scores):
    for index, value in enumerate(student_scores):
        student_scores[index] = round(value)
    
    return student_scores


def count_failed_students(student_scores):
    failures = 0
    for _, value in enumerate(student_scores):
        if value <= 40:
            failures+=1
    
    return failures

def above_threshold(student_scores, threshold):
    not_failures = []
    for _, value in enumerate(student_scores):
        if value >= threshold:
            not_failures.append(value)
    
    return not_failures


def letter_grades(highest):
    interval = math.floor((highest - 40)/4)
    grades = []
    for index in range(4):
        grades.append(41 + (interval*index))
    return grades


def student_ranking(student_scores, student_names):
    rankings = []

    for index, value in enumerate(student_names):
        rankings.append(str(index + 1)+". "+ value + ": " + str(student_scores[index]))
    return rankings

def perfect_score(student_info):
    for index, value in enumerate(student_info):
        if value[1] == 100:
            return student_info[index]

    return []
