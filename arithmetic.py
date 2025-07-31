
num1= float(input("Enter Num1: "))
num2= float(input("Enter Num2: "))
print("-----------------")
print("+, -, *, /, %")
print("-----------------")
operator= input("Choose an operator: ")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)
else:
    print("Invalid operator!")
 

