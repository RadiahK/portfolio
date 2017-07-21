import random
from random import randint

answerNum = (1,36)
Number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
color = ["red", "black"]
answerColor = random.choice(color)
answerColor = str(answerColor)
oe = ["odd", "even"]
answerOe = random.choice(oe)
answerOe = str(answerOe)

def level1():
    guess = input("Pick a color: red or black")

    if guess == answerColor:
        print("Color:" + str(answerColor))
        print("Your guess:" + str(guess))
        print("Computer's color:" + str(answerColor))
        print("You're correct!")
        print("You move on to the next level.  Now you will bet odd or even")
        level2()
    if guess != answerColor:
        print("Color:" + str(answerColor))
        print("Your guess:" + str(guess))
        print("You're incorrect")
        print("Try again")
        level1()

def level2():
    guess = input("Choose: odd or even")

    if guess == answerOe:
        print("odd or even:" + str(answerOe))
        print("Your guess:" + str(guess))
        print("Computer's choice:" + str(answerOe))
        print("You're correct!")
        print("Congratulations, you move on to the next level!")
    else:
        print("Odd or even" + str(answerOe))
        print("Your guess:" + str(guess))
        print ("Your incorrect")

level1()

def level3():
    guess = input("Choose a number to bet on from 1 to 36")

    if guess == answerNum:
        print("number:" + str(answerNum))
        print("Your guess:" + str(guess))
        print("Computer's choice:" + str(answerNum))
        print("You're correct!")
    else:
        print("number" + str(answerNum))
        print("Your guess:" + str(guess))
        print ("Your incorrect")
