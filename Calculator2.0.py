
n = 1

print("Hello This is Simple Calculator App")
print("Made By : Ehsan Separ\n")

while n < 100:
    print("\n\nStart!")
    number1 = input("Type Your First Number : ")
    operation = input("\nSelect One Of This Operation : \n +, -, *, / -> ")
    number2 = input("\nType Your Second Number : ")

    if operation == "+":
        answer1 = float(number1) + float(number2)
        print("\nYour Addition is : (" + str(answer1) + ")")

    elif operation == "-":
        answer2 = float(number1) - float(number2)
        print("\nYour Subtraction is : (" + str(answer2) + ")")

    elif operation == "*":
        answer3 = float(number1) * float(number2)
        print("\nYour Multiplication is : (" + str(answer1) + ")")

    elif operation == "/":
        answer4 = float(number1) / float(number2)
        print("\nYour Division is : (" + str(answer4) + ")")

    else :
      print("\nI cant Calcul!\n Please Try Agin!")