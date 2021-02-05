#Cameron Randall, 000820614
#I, Cameron Randall, student number 000820614, certify that all code submitted is my own work;
#that I have not copied it from any other source.
#I also certify that I have not allowed my work to be copied by others.

import random
playerScore = 0
turnCount = 0
playerDice = [1, 2, 3, 4, 5]
reroll = ["n", "n", "n", "n", "n"]
choiceFlag = "n"
rollsUsed = 0

#roll dice in list
def roll_dice(someList):
    for x in range(0, len(someList)):
        someList[x] = random.randint(1,6)
        
#selectively roll dice in list
def s_roll_dice(diceList, rollList):
    for x in range(0, len(diceList)):
        if rollList[x].lower() == "y":
            diceList[x] = random.randint(1,6)
            
#sum dice in list
def sum_dice(someList):
    diceSum = 0
    for x in range(0, len(someList)):
        diceSum = diceSum + someList[x]
    return diceSum

#prime num checker
def is_prime(k):
    if k == 1:
        return False
    for i in range(1, k-1):
        if k%i == 0 and i != 1:
            return False
    return True

#evaluate patterns, return associated score or False if none
def pattern_check(someList):
    diceSum = 0
    patternCount = [0, 0, 0, 0, 0]
    diceSum = sum_dice(someList)
    for x in range(0, len(someList)):
        for y in range(0, len(someList)):
            if someList[x] == someList[y]:
                patternCount[x] += 1
    if all(k >= 5 for k in patternCount):
        return 100
    elif is_prime(diceSum):
        return 50
    elif any(i >= 3 for i in patternCount):
        return 30
    elif all(z == 1 for z in patternCount):
        return 25
    return False

#return string to associated pattern
def pattern_string(someList):
    pattern = pattern_check(someList)
    if pattern == 100:
        return "all of the values being equal"
    elif pattern == 50:
        return "sum of the values is a prime number"
    elif pattern == 30:
        return "three of the values being equal"
    elif pattern == 25:
        return "all of the values being unique"
    return "pattern string error :("

#called at end of turn, prepare program for next turn
def new_turn():
    global turnCount
    global playerScore
    global rollsUsed
    print("Your score is now " + str(playerScore) +
          " points. Taking points ended your turn.")
    print("End of turn " + str(turnCount) + ".")
    turnCount+=1
    rollsUsed = 0
    if turnCount <= 10:
        print("Turn " + str(turnCount) +":")
        roll_dice(playerDice)
        print("You rolled 5 dice", playerDice)
        patternScore = pattern_check(playerDice)
        sumScore = sum_dice(playerDice)

#prompts if user would like to reroll dice, sets values to be used w/ selective re-roll
def reroll_prompt():
    global rollsUsed
    for x in range (0, len(reroll)):
        reroll[x] = input("Would you like to reroll die" + (str(x+1)) + "? ")
        properInput = (reroll[x].lower() == "y" or reroll[x].lower() == "n")
        while not(properInput):
            print("Sorry, " + reroll[x] + " is not a valid choice, please enter y or n.")
            reroll[x] = input("Would you like to reroll die" + (str(x+1)) + "? ")
            if reroll[x].lower() == "y" or reroll[x].lower() == "n":
                properInput = True
    if all(x.lower() == "n" for x in reroll):
        print("You didn't score any points or reroll any dice, please try again.")
    else:
        s_roll_dice(playerDice, reroll)
        rollsUsed += 1
        print("You rerolled some dice and the new values are", playerDice)

print("Programmng Fundamentals 201935")
userName = input("Welcome to the game! What is your name? ")

#if username is not alpha, keep prompting
while not(userName.isalpha()):
    print("Sorry " + userName + ", names may only contain letters.")
    userName = input("Please re-enter your name: ")
userName = userName.capitalize()

print("Thank you " + userName + ", you start with 0 points. Let's play!")
turnCount+=1
print("Turn " + str(turnCount) +":")
roll_dice(playerDice)
print("You rolled 5 dice", playerDice)
while turnCount <= 10:
    outputStr = ""
    patternScore = pattern_check(playerDice)
    sumScore = sum_dice(playerDice)
    if rollsUsed == 2:
        if sumScore > patternScore:
            playerScore = playerScore + sumScore
            print("You are out of reroll tries, you score " + str(sumScore) + " points for sum of roll.")
        elif patternScore > sumScore:
            playerScore = playerScore + patternScore
            print("You are out of reroll tries, you score " + str(patternScore) + " points for "
                  + pattern_string(playerDice) + ".")
        new_turn()

    if turnCount <= 10:
        if sumScore > patternScore:
            if patternScore == False:
                outputStr = ("Would you like to score the sum of the dice? (" +
                str(sumScore) + ") [y/n]: ")
                choiceFlag = input(outputStr)
                properInput = (choiceFlag.lower() == "y" or choiceFlag.lower() == "n")
                while not(properInput):
                    print("Sorry, " + choiceFlag + " is not a valid choice, please enter y or n.")
                    choiceFlag = input(outputStr)
                    if choiceFlag.lower() == "y" or choiceFlag.lower() == "n":
                        properInput = True
                if choiceFlag.lower() == "y":
                    playerScore = playerScore + sumScore
                    new_turn()
                elif choiceFlag.lower() == "n":
                    reroll_prompt()
            else:
                outputStr = ("Would you like to score the sum of the dice? (" +
                               str(sumScore) + ") [y/n]: ")
                choiceFlag = input(outputStr)
                properInput = (choiceFlag.lower() == "y" or choiceFlag.lower() == "n")
                while not(properInput):
                    print("Sorry, " + choiceFlag + " is not a valid choice, please enter y or n.")
                    choiceFlag = input(outputStr)
                    if choiceFlag.lower() == "y" or choiceFlag.lower() == "n":
                        properInput = True
                if choiceFlag.lower == "y":
                    playerScore = playerScore + sumScore
                    new_turn()
                else:
                    outputStr = ("Would you like to score the pattern points for " +
                                       pattern_string(playerDice) + "? (" + str(pattern_check(playerDice)) + ") [y/n]: ")
                    choiceFlag = input(outputStr)
                    properInput = (choiceFlag.lower() == "y" or choiceFlag.lower() == "n")
                    while not(properInput):
                        print("Sorry, " + choiceFlag + " is not a valid choice, please enter y or n.")
                        choiceFlag = input(outputStr)
                        if choiceFlag.lower() == "y" or choiceFlag.lower() == "n":
                            properInput = True
                    if choiceFlag.lower == "y":
                        playerScore = playerScore + patternScore
                        new_turn()
                    elif choiceFlag.lower == "n":
                        reroll_prompt()
        elif patternScore > sumScore:
            outputStr = ("Would you like to score the pattern points for " +
                                   pattern_string(playerDice) + "? (" + str(pattern_check(playerDice)) + ") [y/n]: ")
            choiceFlag = input(outputStr)
            properInput = (choiceFlag.lower() == "y" or choiceFlag.lower() == "n")
            while not(properInput):
                    print("Sorry, " + choiceFlag + " is not a valid choice, please enter y or n.")
                    choiceFlag = input(outputStr)
                    if choiceFlag.lower() == "y" or choiceFlag.lower() == "n":
                        properInput = True
            if choiceFlag.lower() == "y":
                playerScore = playerScore + patternScore
                new_turn()
            else:
                outputStr = ("Would you like to score the sum of the dice? (" +
                                   str(sumScore) + ") [y/n]: ")
                choiceFlag = input(outputStr)
                properInput = (choiceFlag.lower() == "y" or choiceFlag.lower() == "n")
                while not(properInput):
                    print("Sorry, " + choiceFlag + " is not a valid choice, please enter y or n.")
                    choiceFlag = input(outputStr)
                    if choiceFlag.lower() == "y" or choiceFlag.lower() == "n":
                        properInput = True
                if choiceFlag.lower() == "y":
                    playerScore = playerScore + sumScore
                    new_turn()
                elif choiceFlag.lower() == "n":
                    reroll_prompt()
    
print("10 turns have passed, your final score is: " + str(playerScore) + " points.")
if playerScore > 400:
    print("Great job! This is an above average score.")
elif playerScore >= 200 and playerScore <= 400:
    print("Congratulations, this is an average score.")
elif playerScore < 200:
    print("You should play again to see if you can do better!")
