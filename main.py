game=True
score_loop=False
while not score_loop:
    try:
        winning_score=int(input("what score would you like to play to?"))
        score_loop=True
    except ValueError:
        print("error")
        score_lopp=False
instructions=input("type '?' for instructions")
if instructions=="?":
    print("")
ask=False
while not ask:
    start=input("are you ready to play roll it 13?")
    y=["y","yes","ok"]
    if start in y:
        game=False
        ask=True
    while not game:
        dice=input("press enter to roll")
        if dice=="":
            ram_num= randint(1,6)
            print(ram_num)

