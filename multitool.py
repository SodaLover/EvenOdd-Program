def program():
    print("EvenOddProgram v1.1. Check out the repository!")
    evenodd = input("Type even, odd, or calculate ")
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
    elif evenodd == "git5647382910":
        print("Wow, this is precise.")
    elif evenodd == "calculate":
        def mart():
            input1 = int(input("Input a number."))
            oper = input("Input a operator in text.")
            input2 = int(input("Input a second number."))
            if oper == "add":
                print(input1 + input2)
            elif oper == "subtract":
                print(input1 - input2)
            elif oper == "multiply":
                print(input1 * input2)
            elif oper == "divide":
                print(input1 / input2)
            mart()

        mart()

    else:
        print("I don't understand that.")
    program()
program()