sum=0
while(True):
    userinput= input("Enter the Item price or press q to quit: \n")
    if (userinput!='q'):
        sum = sum + eval(userinput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Your Bill Total is {sum} Thanks for shopping with us!\nHave a nice Day")
        break