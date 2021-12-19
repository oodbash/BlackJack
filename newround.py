def ask():
    answer = None
    while answer != "y" and answer != "n":
        answer = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
        if answer == "y":
            play_more = True
        elif answer == "n":
            play_more = False
        else:
            print("Please provide a walid answer.")
    return answer