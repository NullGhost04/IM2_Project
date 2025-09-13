rows = int(input("Enter row: "))
cols = int(input("Enter column: "))

myList = []

for x in range(rows):
    row_data = []
    print(f"\nRow {x+1}")
    for y in range(cols):
        num = float(input(f"Enter number for column {y+1}: "))
        row_data.append(num)
    myList.append(tuple(row_data))

print("\nOutput Matrix:")
for i in range(rows):
    for j in range(cols):
        print(myList[i][j], end=" ")
    print()

search_val = float(input("\nSearch: "))

for i in range(rows):
    for j in range(cols):
        if myList[i][j] == search_val:
            print(f"Number {search_val} found at Row {i+1}, Col {j+1}")