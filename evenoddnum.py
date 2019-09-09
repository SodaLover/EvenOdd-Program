def program():
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
    else:
        print("I don't understand that.")
    program()
program()
