"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_dict = {'J' : 10,
                'Q' : 10,
                'K' : 10,
                'A' : 1}
    if card in card_dict:
        return card_dict[card]
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_dict = {'J' : 10,
            'Q' : 10,
            'K' : 10,
            'A' : 1}
    if card_one in card_dict:
        valor1 = card_dict[card_one]
    else:
        valor1 = int(card_one)

    if card_two in card_dict:
        valor2 = card_dict[card_two]
    else:
        valor2 = int(card_two)

    if valor1 == valor2:
        return card_one, card_two
    elif valor1 > valor2:
        return card_one
    else:
        return card_two
        

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_dict = {'J' : 10,
            'Q' : 10,
            'K' : 10}
    
    if card_one in card_dict:
        valor1 = card_dict[card_one]
    elif card_one == 'A':
        valor1 = 11
    else:
        valor1 = int(card_one)

    if card_two in card_dict:
        valor2 = card_dict[card_two]
    elif card_two == 'A':
        if card_one =='A':
            valor2 = 1
        else:
            valor2 = 11
    else:
        valor2 = int(card_two)

    if valor1 + valor2 <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_dict = {'J' : 10,
            'Q' : 10,
            'K' : 10}
    
    if card_one in card_dict:
        valor1 = card_dict[card_one]
    elif card_one == 'A':
        valor1 = 11
    else:
        valor1 = int(card_one)

    if card_two in card_dict:
        valor2 = card_dict[card_two]
    elif card_two == 'A':
        if card_one =='A':
            valor2 = 1
        else:
            valor2 = 11
    else:
        valor2 = int(card_two)
        
    if valor1 + valor2 == 21:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    card_dict = {'J' : 10,
            'Q' : 10,
            'K' : 10}
    
    if card_one in card_dict:
        valor1 = card_dict[card_one]
    elif card_one == 'A':
        valor1 = 11
    else:
        valor1 = int(card_one)

    if card_two in card_dict:
        valor2 = card_dict[card_two]
    elif card_two == 'A':
        if card_one =='A':
            valor2 = 1
        else:
            valor2 = 11
    else:
        valor2 = int(card_two)
        
    if card_one == card_two or valor1 == valor2:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card_dict = {'J' : 10,
            'Q' : 10,
            'K' : 10}
    
    if card_one in card_dict:
        valor1 = card_dict[card_one]
    elif card_one == 'A':
        valor1 = 11
    else:
        valor1 = int(card_one)

    if card_two in card_dict:
        valor2 = card_dict[card_two]
    elif card_two == 'A':
        if valor1 >= 8:
            valor2 = 1
        else:
            valor2 = 11
    else:
        valor2 = int(card_two)

    if card_one == 'A' and valor2 in (8, 9, 10):
        valor1 = 1
    else:
        pass

    if valor1 + valor2 in (9, 10, 11):
        return True
    else:
        return False
