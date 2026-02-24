print("Welcome to the Python Pizza Deliveries: \n")
size= input("What size pizza do you want S , M , L: \n").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").lower()
extra_cheese= input("Do you want extra cheese? Y or N: \n" ).lower()

total_bill= 0

if size == "s":
    total_bill +=  15
    if pepperoni == "y":
        total_bill+= 2
    if extra_cheese == "y":
        total_bill+= 1
elif size == "m":
    total_bill += 20
    if pepperoni == "y":
        total_bill+= 3
    if extra_cheese == "y":
        total_bill+= 1
elif size == "l":
    total_bill += 25
    if pepperoni == "y":
        total_bill+= 3
    if extra_cheese == "y":
        total_bill+= 1
else:
    print("Invalid input please try again")
print(f"your total bill is {total_bill}")
