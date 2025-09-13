rows = int(input("Enter row: "))
cols = int(input("Enter column: "))

myList = {}

for x in range(rows):
    print(f"\nRow {x+1}")
    for y in range(cols):
        num = float(input(f"Enter number for column {y+1}: "))
        myList[(x+1, y+1)] = num

print("\nOutput Matrix:")
for i in range(1, rows+1):
    for j in range(1, cols+1):
        print(myList[(i, j)], end=" ")
    print()

search_val = float(input("\nSearch: "))

for key, value in myList.items():
    if value == search_val:
        print(f"Number {search_val} found at Row {key[0]}, Col {key[1]}")