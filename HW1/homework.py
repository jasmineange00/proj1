rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []

for i in range(rows):
    print("Row", i+1)
    num1 = float(input("Enter number1: "))
    num2 = float(input("Enter number2: "))
    row_dict = {(i, 0): num1, (i, 1): num2}
    matrix.append(row_dict)

search_num = float(input("\nSearch: "))

print("\nThe numbers are:\n")
for i in range(rows):
    values = [matrix[i][(i, c)] for c in range(cols)]
    for v in values:
        print(v, end=" ")
    print()

positions = []
for i in range(rows):
    for c in range(cols):
        if matrix[i][(i, c)] == search_num:
            positions.append((i, c))

pos_strings = []
for pos in positions:
    pos_strings.append("Row " + str(pos[0]) + ", Col " + str(pos[1]))

print("\nNumber", search_num, "found at", " and ".join(pos_strings))