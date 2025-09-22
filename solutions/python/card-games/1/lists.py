"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds = [number, number + 1, number + 2]
    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    list = rounds_1 + rounds_2
    return list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    
    true_average = sum(hand) / len(hand)
    average1 = (max(hand) + min(hand)) / 2
    lista_ordenada = sorted(hand)
    n = len(lista_ordenada)
    if n % 2 == 1:
        average2 = lista_ordenada[n // 2]
    else:
        meio1 = lista_ordenada[n // 2 - 1]
        meio2 = lista_ordenada[n // 2]
        average2 = (meio1 + meio2) / 2
    if true_average == average1 or true_average == average2:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_list = []
    odd_list = []
    for number in range(0, len(hand)):
        if number % 2 == 0:
            odd_list.append(hand[number])
        else:
            even_list.append(hand[number])
    average_even = sum(even_list) / len(even_list)
    average_odd = sum(odd_list) / len (odd_list)
    if average_even == average_odd:
        return True
    else:
        return False

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand
