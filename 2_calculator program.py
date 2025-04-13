print("hey there welcome to my playground to practice while and for")
print("this program can do 4 main arithmetic operations")
print("if you don't want to participate type \"exit\"")

while True:
    num1 = input("enter the number 1 value to do math ")
    if num1 == "exit":
        break
    num2 = input("enter the number 2 value to do math ")
    if num2 == "exit":
        break
    op = input("enter the operator among these \"+, -, /, *\" ")
    if op == "exit":
        break

#converting the numbers to float to do the math efficiently
    num1= float(num1)
    num2= float(num2)

    if op == "+":
        results = num1 + num2
        print("The additions of the numbers is: ", results)
    if op == "-":
        results =num1-num2
        print("The subtraction fo the numbers is: ", results)
    if op== "*":
        results = num1*num2
        print("the multiplication of the numbers is: ", results)
    if op== "/":
        if num1== "0" or num2 == "0":
            print("zero is not dividable option")
        else:
            results = num1/num2
            print("the division of the numbers is: ", results)
    if op not in ["+", "-", "*" , "/"]:
        print("the operator is invalid")
        break
    break #to break the while loop the final break is 
