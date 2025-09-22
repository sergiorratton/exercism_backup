"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    for score in student_scores:
        if type(score) == int:
            continue
        else:
            student_scores[student_scores.index(score)] = round(score, 0)
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    contador = 0
    for contagem in student_scores:
        if contagem <= 40:
            contador += 1
        else:
            continue
    return contador

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    lista_melhores = []
    for contagem in student_scores:
        if contagem >= threshold:
            lista_melhores.append(contagem)
        else:
            continue
    return lista_melhores

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    intervalo = highest - 40
    pulo = intervalo // 4
    lista_intervalos = []
    for resultado in range(40, highest, pulo):
        valor = resultado + 1
        if valor == highest:
            continue
        else:
            lista_intervalos.append(valor)
    return lista_intervalos


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    comprimento_scores = len(student_scores)
    comprimento_names = len(student_names)
    if comprimento_names != comprimento_scores:
        raise ValueError("Different size lists.")
    lista_final = []
    for indice, valor in enumerate(student_scores):
        ranking = indice + 1
        nome = student_names[indice]
        valor_lista_final = f"{ranking}. {nome}: {valor}"
        lista_final.append(valor_lista_final)
    return lista_final

    
def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    lista_final = []
    for sublista in student_info:
        if 100 in sublista:
            return sublista
    return lista_final