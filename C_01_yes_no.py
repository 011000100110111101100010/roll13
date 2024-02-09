import random

game = True
score_loop = False
#finds the wanted score
while not score_loop:
    try:
        winning_score = int(input("what score would you like to play to?"))
        score_loop = True
    except ValueError:
        print("error")
        score_loop = False
#asks if you wish to read the instructions
instructions = input("type '?' for instructions")
if instructions == "?":
    print("")
#are you ready to play
ask = False
while not ask:
    start = input("are you ready to play roll it 13?")
    y = ["y", "yes", "ok"]
    if start in y:
        game = False
        ask = True
        ai_game_score=0
        player_game_score=0
        player_score=0
        ai_score=0
    while not game:
        dice = input("press enter to roll")
        if dice == "":
#dice rolling
            ram_num = random.randint(1, 6)
            player_score=ram_num+player_score
            print("your roll was ",ram_num)
            print("your score is now",player_score)
            if player_score>13:
                print("you lose this round")
                print("your score is",player_score)
                ai_score=ai_score+ai_game_score
                print("ai score is",ai_score)
                player_game_score=0
                ai_game_score=0
                if player_score >= winning_score:
                    print("you win the game")
                if ai_score>= winning_score:
                    print("you lose")
                    game=True
#ai roll
            if ai_game_score<9:
                ram_num = random.randint(1, 6)
                ai_game_score=ram_num+ai_game_score
            else:
                print("ai has passed")
        else:
            ai_turn=False
            while not ai_turn:
                if ai_game_score<9:
                    ram_num = random.randint(1, 6)
                    ai_game_score=ram_num+ai_game_score
                else:
                    print("ai has passed")
                    ai_turn=True
                    if player_game_score>ai_game_score:
                        print("you win")
                    elif player_game_score==ai_game_score:
                        print("its a tie")
                    else:
                        print("you lose the round")
                    print("your score is", player_score)
                    ai_score = ai_score + ai_game_score
                    print("ai score is", ai_score)
                    player_game_score = 0
                    ai_game_score = 0

print("the scores were:")
print("ai: ",ai_score)
print("player: ",player_score)

