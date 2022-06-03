def calculator(num1, oper, num2):
    if oper == "/" and num2== 0 :
        print ("Division By Zero resuls in infinity .")
    else:
        if oper == "+":
            print (num1, oper, num2, "=", num1+num2)
        elif oper == "-":
            print (num1, oper, num2, "=", num1-num2)

        elif oper == "*":
            print (num1, oper, num2, "=", num1*num2)
        elif oper == "/":
            print (num1, oper, num2, "=", num1/num2)
        else:
            print("Wrong input")   

num1 = int (input("Enter the first number "))
oper = (input("Enter the operater "))
num2 = int (input ("enter the second number  "))
calculator(num1, oper, num2)

