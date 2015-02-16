'''
Created on 21.5.2014

@author: Morzeux
'''

import os
import re

_CARDS = os.path.join('Problems', 'poker.txt')

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIRS = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10

VALUE_SCORES = {'T': 10,
                'J': 11,
                'Q': 12,
                'K': 13,
                'A': 14}

def score_value(value):
    """ Returns score of value. """
    if value in VALUE_SCORES:
        return VALUE_SCORES[value]
    else:
        return int(value)

def sort_cards(cards):
    """ Sorts cards by its value. """
    numbers = []
    tens = []
    jacks = []
    queens = []
    kings = []
    aces = []

    while cards:
        card = cards.pop()
        if re.match('[1-9]', card[0]):
            numbers.append(card)
        elif card[0].lower() == 't':
            tens.append(card)
        elif card[0].lower() == 'j':
            jacks.append(card)
        elif card[0].lower() == 'q':
            queens.append(card)
        elif card[0].lower() == 'k':
            kings.append(card)
        elif card[0].lower() == 'a':
            aces.append(card)

    cards = sorted(numbers, key=lambda x: x[0]) \
    + tens + jacks + queens + kings + aces

    return ''.join(cards)

def is_pair(cards):
    """ Checks if player got one pair. """
    if re.match('.*(.)\\1{1,}.*', cards[::2]):
        return re.match('.*(.)\\1{1,}.*', cards[::2]).groups()[0]
    else:
        return False

def is_two_pairs(cards):
    """ Checks if player got two pairs. """
    if re.match('.*(.)\\1{1,}.*(.)\\2{1,}.*', cards[::2]):
        return re.match('.*(.)\\1{1,}.*(.)\\2{1,}.*', cards[::2]).groups()
    else:
        return False

def is_three_of_a_kind(cards):
    """ Checks if player got three of a kind. """
    if re.match('.*(.)\\1{2,}.*', cards[::2]):
        return re.match('.*(.)\\1{2,}.*', cards[::2]).groups()[0]
    else:
        return False

def is_straight(cards):
    """ Checks if player got straight flush. """
    if cards[::2] in '123456789TJQKA':
        return True
    else:
        return False

def is_flush(cards):
    """ Checks if player got flush. """
    if re.match('.C.C.C.C.C', cards):
        return True
    elif re.match('.D.D.D.D.D', cards):
        return True
    elif re.match('.S.S.S.S.S', cards):
        return True
    elif re.match('.H.H.H.H.H', cards):
        return True
    else:
        return False

def is_full_house(cards):
    """ Checks if player got full house. """
    if re.match('(.)\\1{2,}(.)\\2{1,}', cards[::2]):
        return cards[0]
    elif re.match('(.)\\1{1,}(.)\\2{2,}', cards[::2]):
        return cards[-2]
    else:
        return False

def is_four_of_a_kind(cards):
    """ Checks if player got four of a kinf. """
    if re.match('(.)\\1{3,}.*', cards[::2]):
        return cards[0]
    elif re.match('.*(.)\\1{3,}', cards[::2]):
        return cards[-2]
    else:
        return False

def is_straight_flush(cards):
    """ Checks if player got straight flush. """
    if is_straight(cards) and is_flush(cards):
        return True
    else:
        return False

def is_royal_flush(cards):
    """ Checks if player got royal flush. """
    if re.match('T.J.Q.K.A', cards) and is_flush(cards):
        return True
    else:
        return False

def get_second_highest(cards):
    """ Gets second highest card. """
    return sorted(list(set([score_value(value) for value in cards[::2]])))

def evaluate_player(cards):
    """ Evaluates player and returns his score. """
    cards = sort_cards(cards[:])

    if is_royal_flush(cards):
        score = (ROYAL_FLUSH, 0, 0)

    elif is_straight_flush(cards):
        score = (STRAIGHT_FLUSH, score_value(cards[-1][0]),
                 get_second_highest(cards))

    elif is_four_of_a_kind(cards):
        score = (FOUR_OF_A_KIND, score_value(is_four_of_a_kind(cards)),
                 get_second_highest(cards))

    elif is_full_house(cards):
        score = (FULL_HOUSE, score_value(is_full_house(cards)),
                 get_second_highest(cards))

    elif is_flush(cards):
        score = (FLUSH, score_value(cards[-2]), get_second_highest(cards))

    elif is_straight(cards):
        score = (STRAIGHT, score_value(cards[-2]), get_second_highest(cards))

    elif is_three_of_a_kind(cards):
        score = (THREE_OF_A_KIND, score_value(is_three_of_a_kind(cards)),
                 get_second_highest(cards))

    elif is_two_pairs(cards):
        res = sorted([score_value(val) for val in is_two_pairs(cards)])[-1]
        score = (TWO_PAIRS, res, get_second_highest(cards))

    elif is_pair(cards):
        score = (ONE_PAIR, score_value(is_pair(cards)),
                 get_second_highest(cards))

    else:
        score = (HIGH_CARD, score_value(cards[-2]), get_second_highest(cards))

    return score

def compare_values(player1, player2, scores1, scores2):
    """ Compares two values. """
    if len(scores1) != 1:
        score1 = scores1.pop(0)
        score2 = scores2.pop(0)
        if score1 > score2:
            return 1
        elif score1 == score2:
            return compare_values(player1, player2, scores1, scores2)
        elif score1 < score2:
            return -1
    else:
        while scores1[0] and scores2[0]:
            score1 = scores1[0].pop()
            score2 = scores2[0].pop()
            if score1 > score2:
                return 1
            elif score1 < score2:
                return -1

        return 0

def compare_players(player1, player2):
    """ Compares two players. """
    return compare_values(player1, player2, list(evaluate_player(player1)),
                          list(evaluate_player(player2)))

def problem():
    """
    In the card game poker, a hand consists of five cards and are ranked,
    from lowest to highest, in the following way:

        High Card: Highest value card.
        One Pair: Two cards of the same value.
        Two Pairs: Two different pairs.
        Three of a Kind: Three cards of the same value.
        Straight: All cards are consecutive values.
        Flush: All cards of the same suit.
        Full House: Three of a kind and a pair.
        Four of a Kind: Four cards of the same value.
        Straight Flush: All cards are consecutive values of same suit.
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

        The cards are valued in the order:
        2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the
    highest value wins; for example, a pair of eights beats a pair of fives
    (see example 1 below). But if two ranks tie, for example, both players
    have a pair of queens, then highest cards in each hand are compared
    (see example 4 below); if the highest cards tie then the next highest
    cards are compared, and so on.

    Consider the following five hands dealt to two players:

        Hand         Player 1            Player 2         Winner
        1         5H 5C 6S 7S KD      2C 3S 8S 8D TD     Player 2
                   Pair of Fives      Pair of Eights

        2         5D 8C 9S JS AC      2C 5C 7D 8S QH     Player 1
                Highest card Ace    Highest card Queen

        3         2D 9C AS AH AC      3D 6D 7D TD QD     Player 2
                    Three Aces     Flush with Diamonds

        4         4D 6S 9H QH QC      3D 6D 7H QD QS     Player 1
                  Pair of Queens      Pair of Queens
                Highest card Nine   Highest card Seven

        5         2H 2D 4C 4D 4S      3C 3D 3S 9S 9D     Player 1
                    Full House           Full House
                With Three Fours     with Three Threes

    The file, poker.txt, contains one-thousand random hands dealt to two
    players. Each line of the file contains ten cards (separated by a
    single space): the first five are Player 1's cards and the last five
    are Player 2's cards. You can assume that all hands are valid (no
    invalid characters or repeated cards), each player's hand is in no
    specific order, and in each hand there is a clear winner.

    How many hands does Player 1 win?
    """

    with open(_CARDS, 'r') as flr:
        raw_game = flr.readlines()

    game = []
    for rnd in raw_game:
        rnd = rnd.strip().split(' ')
        game.append((rnd[:5], rnd[5:]))

    count = 0
    for rnd in game:
        if compare_players(rnd[0], rnd[1]) == 1:
            count += 1

    return count
