print("Welcome to Irish Folklore Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play : ")
score = 0

answer = input("What does cpu stand for? ")
if answer == "Central Processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%. ")