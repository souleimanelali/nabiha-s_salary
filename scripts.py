

import random

# Monthly Budget Allocator for Nabiha
def main():
    try:
        month = input("Enter the month you are storing the salary for: ")
        salary = float(input("Enter your salary for the month: "))
        
        # Define expense categories
        expense_categories = ["Savings", "Rent", "Electricity"]
        categories = {}
        
          # Get custom percentage allocations
        for category in expense_categories:
            categories[category] = float(input(f"Enter the percentage for {category}: ")) / 100
        
        
        # Calculate allocations
        allocations = {category: salary * percentage for category, percentage in categories.items()}
        
        total_expenses = sum(allocations.values())
        remaining_salary = salary - total_expenses
        
        yearly_expenses = {category: amount * 12 for category, amount in allocations.items() if category in ["Rent", "Electricity"]}
        
        squared_salary = salary ** 2
        
        additional_savings = 50
        savings_divided = additional_savings / allocations["Savings"] if allocations["Savings"] != 0 else 0
        
       
        # Output results
        print(f"\nBudget Allocation for {month}:")
        for category, amount in allocations.items():
            print(f"{category}: ${amount:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Salary: ${remaining_salary:.2f}")
        
        for category, yearly_amount in yearly_expenses.items():
            print(f"Estimated Yearly {category} Cost: ${yearly_amount:.2f}")
        
        print(f"Salary squared (just for fun!): {squared_salary:.2f}")
        print(f"Additional savings of $50 divided by savings: {savings_divided:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numerical values where required.")
if __name__ == "__main__":
    main()
