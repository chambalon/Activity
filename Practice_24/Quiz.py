



def intro():
    print("\nWelcome to the Quiz about Australia!")
    play=input("Would you like to play?: \n")
    if play.lower() == "yes":
        print("okay lets play!\n")  
    else:
        quit()
intro()
    
def qanda():
    score=0
    answer = input("Question: What is Australia also called?\n")
    if answer.lower() != "the land down under":
        print("Incorrect answer\n")
    else:
        print("Correct answer\n")
        score+= 1

    answer = input("Question: Australia is the only country that is also a continent. True ot False ?\n")
    if answer.lower() != "true":
        print("Incorrect answer\n")
    else:
        print("Correct answer\n")
        score+= 1

    answer = input("Question: Which Australian city is called the city of lights\n")
    if answer.lower() != "perth":
        print("Incorrect answer\n")
    else:
        print("Correct answer\n")
        score+= 1

    print("You have got " + str(score) + " answers correct")
    print("You have got "+ str(score/3*100) + " %\n")

qanda()