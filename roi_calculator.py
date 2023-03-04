#!/usr/bin/python

# welcome
# enter price
# calculate income
# enter expenses
# calculate cashflow
# enter dp/closing_costs
# calculate roi

class Property:
    
    def __init__(self, price):
        self.price = price

    def get_monthly_income(self):
        return self.price * .05

    def get_expenses(self):
        monthly_expenses = 0
        possible_expenses = {'tax', 'insurance', 'utilities', 'HOA', 'lawn and snow', 'vacancy', 'repairs', 'capital expenditures', 'property manager', 'mortgage'}
        print("\nNext we'll calculate your monthly expenses.")
        for item in possible_expenses:
            is_there = input(f"{item.title()}? (y/n) ")
            while is_there.lower() != 'y' and is_there.lower() != 'n':
                is_there = input("Answer [Y]es or [N]o. ")
            if is_there.lower() == 'n':
                continue
            else:
                expense = input("How much? ")
                while expense.isdigit() == False:
                    expense = input("Price must be an integer. Try again. ")
                monthly_expenses += int(expense)
        return monthly_expenses
    
    def get_cash_flow(self):
        print("\nBased on your monthly income and expenses, we can calculate your cash flow.")
        return monthly_income - monthly_expenses

    def get_investment(self):
        pass

    def get_roi(self):
        pass

#CASHFLOW
# cashflow = total_income - total_expenses

#CASHONCASH ROI
# down_payment = 40000 # 20%
# closing_costs = 3000
# rehab = 7000
# misc = 0

# total_investment = 50000

# roi = annual_cash_flow / total_investment

def run_calc():
    print("* * * Rental Property ROI Calculator (RPROIC) * * *")
    price = input("\nHow much will you pay for the property? ")
    while price.isdigit() == False:
        price = input("Price must be an integer. Try again. ")
    property = Property(int(price))
    monthly_income = property.get_monthly_income()
    print(f"Based on the price of the property, you can expect a monthly income of {monthly_income}.")
    property.get_expenses()
    print(f"Your monthly expenses are {monthly_expenses}.")
    property.get_cash_flow()


run_calc()
