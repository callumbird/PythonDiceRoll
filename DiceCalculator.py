dice_string = input("Enter a list of dice to roll \n")
modifier_string = input("Enter a list of modifiers to add to each roll \n")
repeats = input("Enter a value for number of times to repeat this roll \n")
print("\n")

diceList = dice_string.split()
modifierList = modifier_string.split()
numberTest = 0

for i in diceList:
    try:
        numberTest = int(i)
        print(i)
    except ValueError:
        dice_string = input("Enter a list of dice to roll using integers, please \n")

for i in modifierList:
    try: 
        numberTest = int(i)
        print(i)
    except ValueError:
        modifierList = input("Enter a list of modifiers to add to each roll using integers, please \n")



print(diceList)
print(modifierList)
print(__name__)
