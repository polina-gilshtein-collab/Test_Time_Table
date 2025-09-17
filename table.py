from prettytable import PrettyTable

# specify the Column Names while initializing the Table
table = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# add rows
table.add_row(["Leanord", "X", "B", "91.2 %"])
table.add_row(["Penny", "X", "C", "63.5 %"])
table.add_row(["Howard", "X", "A", "90.23 %"])
table.add_row(["Bernadette", "X", "D", "92.7 %"])
table.add_row(["Sheldon", "X", "A", "98.2 %"])
table.add_row(["Raj", "X", "B", "88.1 %"])
table.add_row(["Amy", "X", "B", "95.0 %"])

print(table)