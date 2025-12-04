from functioncall import calculate_sum,fullname
import  math
age=int(input("Enter your age:"))
if age>=18:
    print("you are elgible")
else:
    print("not elogible")

operator=input("enter your operation (+,_,*,/):")
num1=float(input("enter the number 1:"))
num2=float(input("enter the second number"))
if operator=="+":
    print(f"sum of number is: {num1+num2}")
elif operator=="-":
    print(f"sum of number is: {num1-num2}")
elif operator=="*":
    print(f"sum of number is: {num1*num2}")
elif operator=="/":
    print(f"the did:{round( num1/num2)}")
else:
    print(f"operator is not valid :{operator}")