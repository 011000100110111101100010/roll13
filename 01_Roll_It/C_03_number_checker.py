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

winning_score = int_check("enter the winning score that you want to play to")

