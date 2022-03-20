# A simple Irish Folklore Quiz game using Python.
# hr
## At the start of the program there is an input to add your name and a welcome message. The game asks a question and gives multiple choice options for the participant to choose from four different answers. The questions are based on Irish Folklore.
## The game tracks the progress of the participant and displays whether the answer is correct or wrong. A displayed score will also be shown at the end of the game.
## There is also an option to play again or quit.


Create a skeleton structure to understand how the game is going to oporate by creating four functions:
def new_game():
    pass
def check_answer():
    pass
def display_score():
    pass
def play_again():
    pass

Seperate functions for readability.

Create a dictionary to hold all the questions and answers.
Create a lists of lists for the answers with the key value pairs(A,B,C,D).

website content credit: https://fantasticfungi.com/the-mush-room/mushroom-folklore-the-mushroom-folklore-of-ireland/
code credit: https://www.youtube.com/watch?v=XKHEtdqhLK8


Call the new_game function to begin a new game.
Create variables for the answers within the new_game function.
    guesses = []
    correct_guesses = 0
    questions_num = 1

 Display all questions within a for loop.
     for key in questions:
        print(key)
Add a new print statement before the print(key) to add some seperation between questions.


Display all the different options for the answers with a nested for loop.
    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

Increment each question number after each iteration.  
          question_num += 1 

User input: 
    guess = input("Enter (A, B, C, D): ") 
Modify for uppercase senario.

Fill in the check_answer function:
      check_answer(qestions.get(key),guess)

Set up parameters for the check_answer function:
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0  

Increment each correct guess by 1:
correct_guesses += check_answer(qestions.get(key),guess)  

Display the final score outside the for loop.
  display_score(correct_guesses, guesses) 

  def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    print("Answers: ", end="")
# Display questions
    for i in questions:
        print(questions.get(i), end="")
    print()

# Display the guesses.
  print("Guesses: ", end="")
     # Display guesses
    for i in guesses:
        print(i, end="")
    print()

# Final score and print
score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: "+str(score)+"%")  

# Option to play again
def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "Yes":
        return True
    else:
        return False       




