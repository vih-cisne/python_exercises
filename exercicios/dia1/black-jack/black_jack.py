

def value_of_card( card ):
    ace = 'A'
    facials = ['K', 'Q', 'J']

    for face in facials:
        if card == face:
            return 10
    if card == ace:
        return 1
    else:
        return int(card)


def higher_card( card_1, card_2 ):
    value_card_1 = value_of_card(card_1)
    value_card_2 = value_of_card(card_2)

    if value_card_1 > value_card_2:
        return card_1
    elif value_card_1 < value_card_2:
        return card_2
    else: 
        return card_1, card_2


def value_in_hand( *args ):
    ace = 'A'
    facials = ['K', 'Q', 'J']
    amount = 0

    for card in args:
        for face in facials:
            if card == face:
                amount += 10
        if card == ace:
            amount += 11
        elif card.isdigit():
            amount += int(card)
    
    return amount


def value_of_ace(card_1, card_2):
    hand = value_in_hand(card_1, card_2)

    if hand < 11 :
        return 11
    else:
        return 1

def is_blackjack(card_1, card_2):
    tens = ['K', 'Q', 'J', '10']
    ace = 'A'

    for ten in tens:
        if card_1 == ten:
            if(card_2 == ace):
                return True
        elif card_2 == ten:
            if(card_1 == ace):
                return True
    
    return False

def can_split_pairs(card_1, card_2):
    value_card_1 = value_of_card(card_1)
    value_card_2 = value_of_card(card_2)
    # ace have value equal 1 or 11 in this case?

    return value_card_1 == value_card_2


def can_double_down(card_1, card_2):
    value_card_1 = value_of_card(card_1)
    value_card_2 = value_of_card(card_2)
    hand = value_card_1 + value_card_2
    # ace have value equal 1 or 11 in this case?

    values_to_double_down = [9,10,11]

    for value in values_to_double_down:
        if hand == value:
            return True
    return False









