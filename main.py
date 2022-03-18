import random

def get_tof_statements():

    statements = []
    statements.append(["Tigers have stripes", "T"])
    statements.append(["The capital of France is Madrid", "F"])
    statements.append(["The Queen owns one sixth of the land on Earth", "T"])

    return statements

def play_tof_quiz():

    # Get true  or false statements
    tof_statements = get_tof_statements()

    # Randomise tof statements
    random.shuffle(tof_statements)

    # Set player score to 0
    score = 0


    # Show tof statements using a loop
    for s in tof_statements:


        # present statement
        print("True or false " + s[0])
        # user enter guess
        guess = input("Enter T or F: ")
        # check if guess is correct
        if guess == s[1]:
            print("Correct!")
            # update score
            score = score + 1
        else:
            print("Incorrect :(")    

    # Show final score
    print("Your final score is: " + str(score))

def main_menu():

    print("+-------------------------------+")
    print("| Welcome to Quiz Master 3000!  |")
    print("+-------------------------------+")
    print("| Please select an option:      |")
    print("|                               |")
    print("| 1. Play True or False quiz    |")
    print("| 2. Play General Knowledge quiz|")
    print("| 3. Quit                       |")
    print("+-------------------------------+")
    choice = input("Enter 1, 2 or 0: ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "0":
        print("Thanks for playing!")
        quit()

main_menu()