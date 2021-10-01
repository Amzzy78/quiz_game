# ---------------------------------
def new_game():
    
    guesses = [] # list name
    correct_guesses = 0
    question_num = 1 # Current qestion number

    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        # User input and prompt.
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)
        # Fill in the check_answer function and pass the key and guess function.
        correct_guesses += check_answer(qestions.get(key),guess)
        # Increment each question number after each iteration.
        question_num += 1  

# Set up parameters for the check_answer function         
# ---------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CEART!")
        return 1
    else:
        print("Mícheart")
        return 0
# ---------------------------------
def display_score():
    pass
# ---------------------------------
def play_again():
    pass
# ---------------------------------


questions = {
  "Who trained for 20 years in subjects such as law, astronomy, philosophy, poetry, medicine, music, geometry divination, and magic?: ": "A",
  "What is a common ancient Irish beverage used also for ritual where it would be spiked with certain herbs ?: ": "B",
  "In Irish Folklore what was eaten eaten by the Salmon, fished up by the druid, and cooked by young Finn, who, as sorcerer’s apprentice, burns his thumb on the Salmon’s skin, sticks thumb in mouth, and attains all the wisdom in his master’s stead?: ": "C",
  "In Irish Mythology what is the name of the story of the son of a warrior chieftain, who experiences an ‘Isle of intoxicating wine fruits’ during his journey to avenge his father’s death?: ": "A",
}

options = [["A. Druids", "B. Fionn mac Cumhaill", "C. Michael D Higgins", "D. Biddy Early"],
          ["A. Poitin", "B. Mead", "C. Guinness", "D. Whiskey"],
          ["A. Algae", "B. Hazelnuts", "C. Seaweed", "D. Potatoes"],
          ["A. The Voyage of Máel Dúin", "B. Tír na nÓg", "C. The Children of Lir", "D. Táin Bó Cúailnge"]]

# Call the new_game function to begin a new game
new_game() 