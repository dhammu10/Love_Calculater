print("Welcome to love Score calculater")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combine_name = name1 + name2
name_lower = combine_name.lower()

t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
true = t+r+u+e

l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
love = l+o+v+e

score = str(true) + str(love)

print(f"Your love score is {score}%")
