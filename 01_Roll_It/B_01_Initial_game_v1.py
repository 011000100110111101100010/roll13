import random


# Checks user enters yes / no (returns 'yes' / 'no')
def yes_no(question):
    error = "Please enter yes or no"

    while True:

        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)


# Displays the instructions
def instructions_text():
    print('''At the start of each round, the user and the computer each roll a die.
    The initial number of points for each player is the total shown by the die.Then, taking turns,
    the user and computer each roll a single die and add the result to their points.
    The goal is to get 13 points (or slightly less) for a given round.
    Once you are happy with your number of points, you can ‘pass’.
    -If you go over 13, then you lose the round (and get zero points). If the computer goes over 13,
    the round ends and your score is the number of points that you have earned.
    -If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays
    the same).
    -If you get more points than the computer (but less than 14 points), you win and add your points to your
    score. The computer’s score stays the same.
    -The ultimate winner of the game is the first one to get to the specified score goal.
    .''')


def space():
    print("")


# Checks users enter an integer more than / equal to 1
def int_check(question):
    error = "must be a positive integer"
    while True:
        try:
            response = int(input(question))
            if response < 1:
                print("score must be a positive integer")
            else:
                return response
        except ValueError:
            print(error)


# to make it simpler to shw the same score
def show_score():
    print("your round score:", player_game_score, "| ai round score is", ai_game_score)
    print("your game score: ", player_score, "| ai total game score is", ai_score)


# main routine starts here

# initialise initial game values
game = True
score_loop = False

ai_game_score = 0
player_game_score = 0
player_score = 0
ai_score = 0
winning_score = 0
no_play = ""

# finds the wanted score using try

winning_score = int_check("enter the winning score that you want to play to")

# asks if you wish to read the instructions
instructions = input("type '?' for instructions")
if instructions == "?":
    instructions_text()
else:

    # are you ready to play
    start = yes_no("are you ready to play roll it 13 yes or no?")
    if start == "yes":
        game = False
    else:
        no_play = "no"
    while not game:
        # checks if anybody wins the game at the beginning of the round
        if player_score >= winning_score:
            print("***  GAME END  ***")
            print("you win the game")
            game = True
        elif ai_score >= winning_score:
            print("***  GAME END  ***")
            print("you lose the game")
            game = True
        if not game:
            dice = input("press enter to roll")
            space()
            if dice == "":
                # dice rolling
                ram_num = random.randint(1, 6)
                player_game_score = ram_num + player_game_score
                print("your roll was ", ram_num)
                print("your score is now", player_game_score)
                space()
                if player_game_score > 13:
                    print("you lose this round")
                    print("***  ROUND END  ***")
                    player_game_score = 0
                    ai_score = ai_game_score + ai_score
                    show_score()
                    ai_game_score = 0
                # ai roll
                if ai_game_score < 10:
                    ram_num = random.randint(1, 6)
                    ai_game_score = ram_num + ai_game_score
                    print("ai score is:", ai_game_score)
                    space()
                else:
                    print("ai has passed")
                    print("ai score is:", ai_game_score)
            else:
                # the ai's turns after the player passes
                # the ai's turns after the player passes
                ai_turn = False
                while not ai_turn:
                    if ai_game_score < 10:
                        ram_num = random.randint(1, 6)
                        ai_game_score = ram_num + ai_game_score
                        print("ai score is:", ai_game_score)
                        space()
                    else:
                        print("ai has passed")
                        print("ai score is:", ai_game_score)
                        space()
                        # resets the score if the ai looses
                        if ai_game_score > 13:
                            ai_game_score = 0
                        ai_turn = True
                        # this tells you who won the round
                        if player_game_score > ai_game_score:
                            print("you win the round")
                            print("***  ROUND END  ***")
                            ai_game_score = 0
                            player_score = player_game_score + player_score
                            show_score()
                            space()
                        # this code checks if the round was a tie
                        elif player_game_score == ai_game_score:
                            print("its a tie")
                            print("***  ROUND END  ***")
                            show_score()
                            space()
                            player_game_score = 0
                            ai_game_score = 0
                        # checks if you lost the round
                        else:
                            print("***  ROUND END  ***")
                            print("you lose the round")
                        # displays then resets the score
                        ai_score = ai_score + ai_game_score
                        player_game_score = 0
                        show_score()
                        ai_game_score = 0
if not no_play == "no":
    print("")
    print("")
    # shows scores post game
    print("the scores were:")
    print("ai: ", ai_score, "|", "player: ", player_score)
