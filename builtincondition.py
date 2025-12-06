online=True
if online:
    print("User is Online")
else:
    print("User is offline")

temp=-25
is_raining=False
if temp >35 or temp <0 or is_raining:
    print("The event is cancelled")
else:
    print("The outdoor event is still scheduled")
# single line iflese
a=8
b=9
age=20
max_num=a if a>b else b
username=input("Enter your Name:")
spacecount=username.find(" ")
isdigit=username.isalpha()
if len(username)<12:
    if spacecount<1:
        if isdigit:
            print(f"The username: {username} is valid")
        else:
            print(isdigit)
            print("The Username contains Digit")
    else:
        print("UserName contain space:")
else:
    print("Username should not be longer than 12 character:")
