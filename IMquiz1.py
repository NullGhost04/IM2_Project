# Problem 1
while True:
    num = int(input("Enter an integer (0-1000): "))
    if num < 0 or num > 1000:
        print("Bye")
        break
    digit_sum = sum(int(d) for d in str(num))
    print(f"The sum of its digits is {digit_sum}")

# Problem 2
while True:
    num = int(input("Enter number: "))
    if num <= 0:
        print("Bye")
        break
    
    if num % 5 == 0 and num % 6 == 0:
        print(f"{num} is divisible by both 5 and 6")
    elif num % 5 == 0 or num % 6 == 0:
        print(f"{num} is divisible by 5 or 6, but not both")
    else:
        print(f"{num} is not divisible by either 5 or 6")

# Problem 3
count = 0
for i in range(0, 201):
    if i % 5 == 0 or i % 6 == 0:
        print(i, end=" ")
        count += 1
        if count % 10 == 0:
            print()