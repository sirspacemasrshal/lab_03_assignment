from tabulate import tabulate

# Sample data
data = [
    ["P1", "VSCode", "100","MID"],
    ["P23","Eclipse", "234","MID"],
    ["P93","Chrome", "189","High"],
    ["P42","JDK","9","High"],
    ["P9","CMD","7","High"],
    ["P87","NotePad","23","Low"],
]

# Define headers
headers = ["P_ID", "Process", "Start Time(ms)","Priority"]

# Create and print the table
table = tabulate(data, headers=headers, tablefmt="grid")
print(table)
