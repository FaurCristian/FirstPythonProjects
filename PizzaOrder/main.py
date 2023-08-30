print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        add_pepperoni = 2
        bill += add_pepperoni
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        add_pepperoni = 3
        bill += add_pepperoni
if size == "L":
    bill = 25
    if add_pepperoni == "Y" :
        add_pepperoni = 3
        bill += add_pepperoni
if extra_cheese == "Y":
    extra_cheese = 1
    bill += extra_cheese
print(f"Your final bill is: ${bill}.")
