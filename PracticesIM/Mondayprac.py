# 1. Loop stops when input is zero or below
# while True:
#     z = int(input("Enter Number: "))
#     if z <= 0:
#         break


# 2. Consonant and Vowel (loop stops when input is "0")
# while True:
#     s = input("\nEnter string: ")

#     if s == "0":
#         break

#     for ch in s:
#         match ch:
#             case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
#                 print(f"{ch} Vowel")
#             case _:
#                 print(f"{ch} Consonant")


# # 3. Displays every letter
# s = input("\nEnter a string to display each character: ")
# for i in range(len(s)):
#     print(s[i])


# 4. Prints 10 to 1, decreasing by one each line
# for x in range(1, 11):
#     for y in range(10, x-1, -1):
#         print(y, end=" ")
#     print()
# print("\n\n")


# # 5. Number pattern (16 17 18 ... etc.)
# for x in range(1, 6):
#     for y in range(6, 11):
#         print(f"{x}{y}", end=" ")
#     print()


# # 6. Stars and Zeros Pattern
# n = int(input("\nEnter size for star/zero pattern: "))
# for x in range(n+1):
#     for y in range(1, n+1):
#         if x % 2 == 0:
#             print("*", end=" ")
#         else:
#             print("0", end=" ")
#     print()


# 7. String slicing practice
s = "HelloWorld"
print("\nString slicing examples with 'HelloWorld':")
print(s[:])        # HelloWorld
print(s[2:])       # lloWorld
print(s[::-1])     # dlroWolleH
print(s[1:7:2])    # elWr
print(s[-6:-1:2])  # oWr
print(s[-6:-10:-2])# oW
