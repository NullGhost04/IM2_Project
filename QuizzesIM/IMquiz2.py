# num = float(input("Num:"))

# remainders = []

# loop = True
# while(loop):
#     remain = num/8

#     if remain % 8 != 0:
#         remainders.append(int(num % 8))
#         num = int(remain)
#     else:
#         loop = False

# rev_arr = (remainders[:: -1])
# print("Octal:" , end=" ")
# for x in range(len(rev_arr)):
#     print(f"{rev_arr[x]}", end="")

rows = int(input("rows: "))
cols = int(input("cols: "))

Gooding = []

for i in range(rows):
    row = []
    print(f"\nRow {i+1}")
    for j in range(cols):
        num = int(input(f"Enter number: "))
        row.append(num)
    Gooding.append(row)

print("\nGD Matrix with Row Sums:")
for i in range(rows):
    row_sum = sum(Gooding[i])
    for j in range(cols):
        print(Gooding[i][j], end="\t")
    print("Sum:", row_sum)

print("\nColumn Sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += Gooding[i][j]
    print(col_sum, end="\t")