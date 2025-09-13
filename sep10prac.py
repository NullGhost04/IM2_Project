# ------------------ LIST EXAMPLES ------------------

# Example lists
myList = []
myList = ["Mike", "Acosta", "Esteron"]
myList = ["Mike", 90.50, "Emerson", 80.20, "Naniong", 80.20]

# Accessing elements
print(myList[1])
print(myList[:5])
print(myList[::-1])

# Updating elements
myList[0] = "Michael"
# myList[:2] = "James"   # Example of slice assignment
print(myList)

# Adding elements
myList.append("Berbon")
myList.insert(0, "Pico")
print(myList)

# Removing elements
myList.pop(0)            # Using index
myList.remove("Naniong") # Using value
print(myList)

# Loop through list
for x in myList:
    print(f"{x}", end=" ")

print()
for x in range(len(myList)):
    print(f"{myList[x]}", end=" ")


# ------------------ SORTING ------------------
print()
srtList = ["Name 2", "Name 1", "Name 3"]

srtList.sort()
print(srtList)
srtList.reverse()
print(srtList)


# ------------------ NESTED LIST ------------------
"""
print("\n")
myList = [[1, 4, 10, 2], [5, 1, 11, 6]]
print(myList[0][2])

for x in range(len(myList)): 
    print(f"Row {x}")
    myList[x].sort()
    myList[x].reverse()
    for y in range(len(myList[x])): 
        print(f"{myList[x][y]}", end=" ")
    print()
"""


# ------------------ USER INPUT NESTED LIST ------------------
'''
nestedList = []
Row = int(input("Row: "))
Col = int(input("Col: "))

for x in range(Row):
    print(f"Row {x+1}")
    innerList = []

    for y in range(Col):
        print(f"Enter Score {y+1}: ")
        score = float(input())
        innerList.append(score)
    nestedList.append(innerList)

# Output
for x in range(len(nestedList)):
    for y in range(len(nestedList[x])):
        print(nestedList[x][y], end=" ")
    print()

# Search in nested list
num = float(input("Search: "))
for x in range(len(nestedList)):
    for y in range(len(nestedList[x])):
        if nestedList[x][y] == num:
            print(f"Found at Row {x+1} and Col {y+1}")
'''


# ------------------ TUPLE EXAMPLE ------------------
'''
myTuple = ("Mike", "Esteron", "Acosta")
tupleList = list(myTuple)

tupleList[0] = "Michael"
tupleList.append("Naniong")
tupleList.pop()
myTupleList = tuple(tupleList)
print(myTupleList)
'''


# ------------------ DICTIONARY EXAMPLE ------------------
myDict = {"id": "UR-0551", "name": "Mike Acosta", "salary": 15000.00}
print(myDict["name"])

# Update value
myDict["name"] = "James Luzan"
print(myDict["name"])

# Add new key-value pair
myDict["age"] = 69

# Display dictionary contents
print(myDict.keys())
print(myDict.values())

for x, y in myDict.items():
    print(f"Key: {x}, Value: {y}", end=" ")

print("\n\n")

# Dictionary with user input
nameDict = {}
for x in range(2):
    nameDict[x] = input("Name: ")

print(nameDict)