num1 = 6
num2 = 7

#Header: if booleanStatement:
if num1 > num2:
    #Body: holds the statements to execute
    #Everythng in the same tab level is in the body
    print("Num1 is Bigger")
#elif: stands for else if. Check the first condition, then check
#them in the order shown.
elif num2 > num1:
    print("Num2 is bigger")
else:
    print("Num1 and Num2 are equal")