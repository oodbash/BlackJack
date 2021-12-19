import art
import newround
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def calculate(list):
    list.sort()
    count = 0
    for i in list:
        if i == 11:
            count += 11
            if count > 21:
                count += 1
        else:
            count += i
    if count > 21:
        count = 666

    return count

def nextround(list1,list2):

    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        list1.append(random.choice(cards))

        if (calculate(list2)) < 16:
            list2.append(random.choice(cards))

    elif (calculate(list2)) < 16:
        list2.append(random.choice(cards))

    else:
        return False

while newround.ask() == "y":
    print(art.logo)
    mine_cards = []
    dlrs_cards = []
    mine_score = 0
    dlrs_score = 0
    for i in range(2):
        mine_cards.append(random.choice(cards))
        dlrs_cards.append(random.choice(cards))
    mine_score = calculate(mine_cards)
    dlrs_score = calculate(dlrs_cards)
    print(f"Your cards: {mine_cards}, current score: {mine_score}")
    print(f"Computer's first card: {dlrs_cards[0]}")

    
    while nextround(mine_cards,dlrs_cards) != False and calculate(mine_cards) < 21 and calculate(dlrs_cards) < 21:
        print(f"{mine_cards},{calculate(mine_cards)},{dlrs_cards},{calculate(dlrs_cards)}")

    if calculate(mine_cards) == calculate(dlrs_cards):
        print(f"Me - {calculate(mine_cards)}, Dealer - {calculate(dlrs_cards)} so it's Draw")
    elif calculate(mine_cards) == 666:
        print(f"Me - {calculate(mine_cards)}, Dealer - {calculate(dlrs_cards)} so Dealer win")
    elif calculate(dlrs_cards) == 666:
        print(f"Me - {calculate(mine_cards)}, Dealer - {calculate(dlrs_cards)} so I win")
    elif calculate(mine_cards) > calculate(dlrs_cards):
        print(f"Me - {calculate(mine_cards)}, Dealer - {calculate(dlrs_cards)} so I win")
    elif calculate(mine_cards) < calculate(dlrs_cards):
        print(f"Me - {calculate(mine_cards)}, Dealer - {calculate(dlrs_cards)} so Dealer win")