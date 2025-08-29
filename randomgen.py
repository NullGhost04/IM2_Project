import random

while True:
    number = random.randint(1, 60)
    print("\nYour random number is:", number)

    choice = input("Do you want to generate again? (yessir/babye): ").lower()

    if choice != 'yessir':
        print("Exiting... Goodbye!")
        break