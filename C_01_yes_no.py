import random


# the instructions
def instructions_text():
    print('''At the start of each round, the user and the computer each roll two dice.
    The initial number of points for each player is the total shown by the dice.Then, taking turns, 
    the user and computer each roll a single die and add the result to their points. 
    The goal is to get 13 points (or slightly less) for a given round. 
    Once you are happy with your number of points, you can ‘pass’.
    -If you go over 13, then you lose the round (and get zero points). If the computer goes over 13, 
    the round ends and your score is the number of points that you have earned.
    -If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays 
    the same).
    -If you get more points than the computer (but less than 14 points), you win and add your points to your 
    score. The computer’s score stays the same.
    -The first roll of your dice is a double, then your score is increased by double the number of points, 
    provided you win. If the computer’s first roll of the dice is a double, 
    then its points are not doubled (this gives the human player a slight advantage).
    -The ultimate winner of the game is the first one to get to the specified score goal.
    calculation or any key to quit.''')
def show_score():
    print("your round score:", player_game_score,"|","ai round score is", ai_game_score)
    print("your game score: ", player_score,"|","ai total game score is", ai_score)

game = True
score_loop = False

# finds the wanted score
while not score_loop:
    try:
        winning_score = int(input("what score would you like to play to?"))
        if winning_score == 0:
            print("score cannot be zero")
        else:
            score_loop = True
    except ValueError:
        print("error")
        score_loop = False

# asks if you wish to read the instructions
instructions = input("type '?' for instructions")
if instructions == "?":
    instructions_text()

# are you ready to play
ask = False
while not ask:
    start = input("are you ready to play roll it 13?")
    y = ["y", "yes", "ok"]
    if start in y:
        game = False
        ask = True
        ai_game_score = 0
        player_game_score = 0
        player_score = 0
        ai_score = 0
    while not game:
        # it says varibles con be undefined... no they cant
        # checks if a anybody wins
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
            if dice == "":
                # dice rolling
                ram_num = random.randint(1, 6)
                player_game_score = ram_num + player_game_score
                print("your roll was ", ram_num)
                print("your score is now", player_game_score)
                if player_game_score > 13:
                    print("you lose this round")
                    print("***  ROUND END  ***")
                    player_game_score = 0
                    ai_score=ai_game_score+ai_score
                    show_score()
                    ai_game_score = 0
                # ai roll
                if ai_game_score < 9:
                    ram_num = random.randint(1, 6)
                    ai_game_score = ram_num + ai_game_score
                else:
                    print("ai has passed")
            elif dice == "13":
                player_game_score = 13
            else:
                # the ai's turns after the player passes
                ai_turn = False
                while not ai_turn:
                    if ai_game_score < 9:
                        ram_num = random.randint(1, 6)
                        ai_game_score = ram_num + ai_game_score
                    else:
                        print("ai has passed")
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

                        elif player_game_score == ai_game_score:
                            print("its a tie")
                            print("***  ROUND END  ***")
                            show_score()
                            player_game_score = 0
                            ai_game_score = 0
                        else:
                            print("***  ROUND END  ***")
                            print("you lose the round")
                        ai_score = ai_score + ai_game_score
                        show_score()
                        player_game_score = 0
                        ai_game_score = 0
print("")
print("")
# shows scores post game
print("the scores were:")
print("ai: ", ai_score,"|","player: ", player_score)
