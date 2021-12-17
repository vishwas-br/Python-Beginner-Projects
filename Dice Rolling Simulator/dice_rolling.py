import random
print("Hey there!")
ask = str(input("Do you want to roll a dice? (y/n) : "))
x = random.randint(1,6)
yep = random.randint(1,5)
if ask == "y":
    print("Great! Rolling the dice...")
    print("The number is ..." + str(x))
    if x == 6:
        print("Congrats! Since the number 6 showed up, you get another chance")
        print("Rolling again...")
        print("The number is ..." + str(yep))
else:
    print("No problem. But please do give it a try. ")











