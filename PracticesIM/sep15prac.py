# #LIST FUNCTIONS
# text = "A proper cup of coffee from a proper copper coffee pot."

# # 1. count()
# count = text.count("coffee")
# print("Count of 'coffee':", count)

# # 2. strip
# striptix = "copper"
# cleaned = striptix.strip("*")
# print("After strip:", cleaned)

# # 3. replace()
# replistix = text.replace("coffee", "Milk")
# print("After replace:", replistix)

# # 4. split()
# mlbb = "Nolan,Ling,Brody,Granger"
# Heroes = mlbb.split(",")
# print("Heroes list:", Heroes)

# # 5. join()
# jointix = "  ".join(Heroes)
# print("After join:", jointix)

# # ITERATOR FUNCTIONS

# numbers = [6, 9, 69, 169, 269, 369]

# # 1. sum()
# total = sum(numbers)
# print("Sum of numbers:", total)

# # 2. max()
# maximum = max(numbers)
# print("Maximum number:", maximum)

# # 3. min()
# minimum = min(numbers)
# print("Minimum number:", minimum)


# MATH FUNCTIONS PRACTICE

# import math

# # 1. math.ceil()
# num1 = 68.7
# print("math.ceil:", math.ceil(num1))

# # 2. math.floor()
# num2 = 69.9
# print("math.floor:", math.floor(num2))

# # 3. math.sqrt()
# num3 = 6969
# print("math.sqrt:", math.sqrt(num3))

# # 4. math.pow()
# num4, num5 = 6, 9
# print("math.pow:", math.pow(num4, num5))

#ARBITRARY ARGUMENTS
def getHeroes(*heroes):
    print("Heroes in the team:")
    for hero in heroes:
        print("*", hero)

getHeroes("Chano", "Hou Yi", "Consort Yu")
getHeroes("Daji", "Ao Yin", "Nakoruru", "Shoyue")

#KWARGS
def getblank(**Blank):
    print(f"ID: {Blank['C']}  Name: {Blank ['name']}  Role: {Blank['role']}")

getblank(C="Jesus-101", name="Adrian Tiburan", role="Sakristan")
getblank(C="Buddha-104", name="Josh Pogi", role="Enlightened One")