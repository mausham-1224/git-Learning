# Python weight converter



while True:
    weight= float(input("Enter the Weight:"))
    unit=input("kilogram or Pounds? ( K or L):")
    if unit=="k":
        weight=weight*2.205
        unit="LBS."
        print(f"{weight} {unit}")
    elif unit=="l":
        weight=weight/2.205
        units="KG"
        print(f"{weight} {unit}")
    else:
        print(f"{unit} is not valid")

    answer=input("Do you want again:yes or no")
    if answer== "no":
        break