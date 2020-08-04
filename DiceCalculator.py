import sys

if len(sys.argv) < 1:
    print("No arguments have been passed when this program has been called. Please, instead, enter the required values below \n")
    diceList = (input("Enter a list of dice to roll. \n")).split()
    modifierList = (input("Enter a list of modifiers to add to each roll. \n")).split
    repeats = input("Enter a number of times to perform these rolls")
else:
    repeats = sys.argv[0]
    diceList = splitArguments('d')
    modifierList = splitArguments('m')

for roll in range (0, repeats):
    rollDice(diceList)

def splitArguments(char):
    list = []
    numberOfArgumentsToSplit = len(sys.argv)
    splittingList = []
    for i in range(1, numberOfArgumentsToSplit):
        splittingList = split(sys.argv[i])
        if splittingList[0] == char:
            list.append(int(splittingList[1]))
    return list