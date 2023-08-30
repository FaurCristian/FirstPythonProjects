import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_length = len(names)
random_number = random.randint(0, names_length - 1)
meal_pay = names[random_number]

print(f"{meal_pay} is going to buy the meal today!")
