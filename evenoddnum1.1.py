def program():
    print("EvenOddProgram v1.1. Check out the repository!")
    evenodd = input("Would you like to see even numbers or odd numbers. ")
    if evenodd == "even":
        rangevar = int(input("Input a integer that you would like to see the even range to. "))
        rangevar2 = range(0, rangevar, 2)
        for i in rangevar2:
            print(i)
    elif evenodd == "odd":
        rangevar = int(input("Input a integer that you would like to see the odd range to. "))
        rangevar2 = range(1, rangevar, 2)
        for i in rangevar2:
            print(i)
    elif evenodd == "c0deread":
        print("Thanks for checking out my code! You should make a pull request if you spot any bugs.")
    elif evenodd == "git5647382910"
        print("Wow, this is precise.")
    else:
        print("I don't understand that.")
    program()
program()