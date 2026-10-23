import csv
from datetime import datetime

def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d")
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

# add_expense(15.50, "Food", "Lunch with colleagues")