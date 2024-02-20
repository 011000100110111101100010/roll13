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

want_instructions = yes_no("Do you want to read the instructions ? ")

if want_instructions == "yes":
    print("intructions go here")

print("program continues")