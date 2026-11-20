
expenses = []

print("===== EXPENSE TRACKER =====")

while True:
    amount = float(input("Enter expense amount (0 to stop): "))

    if amount == 0:
        break
    elif amount < 0:
        print("Please enter a valid amount!")
    else:
        expenses.append(amount)

print("\n===== EXPENSE REPORT =====")

if len(expenses) > 0:
    total = sum(expenses)
    average = total / len(expenses)

    print("Expenses:", expenses)
    print("Total Expenses: Rs.", total)
    print("Average Expense: Rs.", round(average, 2))
else:
    print("No expenses recorded.")

