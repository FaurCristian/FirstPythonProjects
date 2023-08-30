print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_names = name1.lower() + name2.lower()

T = combined_names.count("t")
R = combined_names.count("r")
U = combined_names.count("u")
E = combined_names.count("e")

L = combined_names.count("l")
O = combined_names.count("o")
V = combined_names.count("v")
E = combined_names.count("e")

true_love = str(T+R+U+E)+str(L+O+V+E)
love_score = int(true_love)

if love_score < 10 or love_score> 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


