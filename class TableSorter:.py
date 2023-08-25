class TableSorter:
    def __init__(self, data, headers):
        self.data = data
        self.headers = headers

    def display_table(self):
        print("Table:")
        for header in self.headers:
            print(f"{header:<15}", end=" ")
        print("\n" + "-" * 45)
        for row in self.data:
            for item in row:
                print(f"{item:<15}", end=" ")
            print()

    def sort_by_p_id(self):
        sorted_data = sorted(self.data, key=lambda x: x[0])
        return sorted_data

    def sort_by_start_time(self):
        sorted_data = sorted(self.data, key=lambda x: x[1])
        return sorted_data

    def sort_by_priority(self):
        sorted_data = sorted(self.data, key=lambda x: x[2])
        return sorted_data


def main():
    data =  [
    ["P1", "VSCode", "100","MID"],
    ["P23","Eclipse", "234","MID"],
    ["P93","Chrome", "189","High"],
    ["P42","JDK","9","High"],
    ["P9","CMD","7","High"],
    ["P87","NotePad","23","Low"],
]

    headers = ["P_ID", "Process", "Start Time(ms)","Priority"]


    sorter = TableSorter(data, headers)

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting.")
            break
        elif choice == 1:
            sorted_data = sorter.sort_by_p_id()
        elif choice == 2:
            sorted_data = sorter.sort_by_start_time()
        elif choice == 3:
            sorted_data = sorter.sort_by_priority()
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        sorter.data = sorted_data
        sorter.display_table()


if __name__ == "__main__":
    main()
