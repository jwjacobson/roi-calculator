#!/usr/bin/python

class Property():
    
    def __init__(self, price):
        self.price = price
        self.monthly_income = int
        self.monthly_expenses = int
        self.cash_flow = int
        self.initial_investment = int
        self.roi = float


    def get_monthly_income(self):
        self.monthly_income = int(self.price * .05) 
        return self.monthly_income
        

    def get_expenses(self):
        self.monthly_expenses = 0
        possible_expenses = {'Tax', 'Insurance', 'Utilities', 'HOA', 'Lawn and snow', 'Vacancy', 'Repairs', 'Capital expenditures', 'Property manager', 'Mortgage'}
        print("\nNext we'll calculate your monthly expenses.\n")
        for item in possible_expenses:
            is_there = input(f"{item}? (y/n) ")
            while is_there.lower() != 'y' and is_there.lower() != 'n':
                is_there = input("Answer [Y]es or [N]o. ")
            if is_there.lower() == 'n':
                continue
            else:
                expense = input("How much? ")
                while expense.isdigit() == False:
                    expense = input("Price must be an integer. Try again. ")
                self.monthly_expenses += int(expense)
        return self.monthly_expenses
    
    def get_cash_flow(self):
        print("\nBased on your monthly income and expenses, we can calculate your cash flow.")
        self.cash_flow = self.monthly_income - self.monthly_expenses 
        return self.cash_flow

    def get_investment(self):
        self.initial_investment = 0
        possible_investments = ["Down payment", "Closing costs", "Rehab", "Anything else"]
        print("\nNow we need to calculate your initial investment.\n")
        for item in possible_investments:
            is_there = input(f"{item}? (y/n) ")
            while is_there.lower() != 'y' and is_there.lower() != 'n':
                is_there = input("Answer [Y]es or [N]o. ")
            if is_there.lower() == 'n':
                continue
            else:
                investment = input("How much? ")
                while investment.isdigit() == False:
                    investment = input("Price must be an integer. Try again. ")
                self.initial_investment += int(investment)
        return self.initial_investment

    def get_roi(self):
        print("Now we can calculate your cash on cash return.")
        print("We find it by dividing your annual cash flow by your initial investment.")
        self.roi = ((self.cash_flow * 12) / self.initial_investment) * 100
        return self.roi

def run_calc():
    print("* * * Rental Property ROI Calculator (RPROIC) * * *")
    price = input("\nHow much will you pay for the property? ")
    while price.isdigit() == False:
        price = input("Price must be an integer. Try again. ")
    property = Property(int(price))
    print(f"\nBased on the price of the property, you can expect a monthly income of {property.get_monthly_income()}.")
    print(f"\nYour monthly expenses are {property.get_expenses()}.")
    print(f"\nYour monthly cashflow is {property.get_cash_flow()}.")
    print(f"\nYour initial investment is {property.get_investment()}.")
    print(f"\nYour cash on cash return is {property.get_roi()} percent.")

run_calc()
