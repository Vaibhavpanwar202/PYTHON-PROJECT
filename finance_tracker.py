import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store expenses
FILENAME = "expenses.csv"

# Initialize file
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILENAME, index=False)

# Add new expense (Warning-free version)
def add_expense(date, category, amount):
    new_row = pd.DataFrame([{"Date": date, "Category": category, "Amount": float(amount)}])
    
    # Check if file is not empty before reading
    if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
        df = pd.read_csv(FILENAME)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row  # If file is empty or doesn't exist

    df.to_csv(FILENAME, index=False)
    print("✅ Expense added successfully.")

# View all expenses
def view_expenses():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("\n📂 No expenses found.")
        return
    df = pd.read_csv(FILENAME)
    print("\n📋 All Expenses:")
    print(df)

# Show summary by category
def show_summary():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("\n📂 No data available.")
        return
    df = pd.read_csv(FILENAME)
    summary = df.groupby("Category")["Amount"].sum()
    print("\n📊 Category-wise Summary:")
    print(summary)

# Visualize expenses
def visualize_expenses():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("\n📂 No data available to visualize.")
        return
    df = pd.read_csv(FILENAME)
    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), title='Expenses by Category')
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# Main menu
def menu():
    while True:
        print("\n📌 Personal Finance Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Visualize Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Rent): ")
            amount = input("Enter amount: ")
            add_expense(date, category, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            visualize_expenses()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
menu()
