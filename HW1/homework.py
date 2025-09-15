nestedlist = []
rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Columns: "))

for i in range(rows):
    print(f"\n- Row {i+1} -")
    row_values = []
    for j in range(cols):
        value = float(input(f"Enter Number {j+1}: "))
        row_values.append(value)
    nestedlist.append(row_values)

print("\nThe Numbers are:")
for i in range(len(nestedlist)):
    for j in range(len(nestedlist[i])):
        print(nestedlist[i][j], end=" ")
    print()

search_num = float(input("\nSearch: "))
found_positions = []
for i in range(len(nestedlist)):
    for j in range(len(nestedlist[i])):
        if nestedlist[i][j] == search_num:
        
            found_positions.append(f"Row {i+1}, Col {j+1}")

if found_positions:
    message = f"Number {search_num} found at " + " and ".join(found_positions)
else:
    message = f"Number {search_num} not found in the matrix."
print(message)
