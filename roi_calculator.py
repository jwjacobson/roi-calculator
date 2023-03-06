#!/usr/bin/python
from prettytable.colortable import ColorTable, Themes

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
        print("\n")
        print("\u001b[44;1m~\u001b[0m"*84)
        print("\n\u001b[36mNext we'll calculate your monthly expenses.\n")
        for item in possible_expenses:
            is_there = input(f"\u001b[33m{item}? \u001b[36m(y/n) ")
            while is_there.lower() != 'y' and is_there.lower() != 'n':
                is_there = input("Answer [Y]es or [N]o. ")
            if is_there.lower() == 'n':
                continue
            else:
                expense = input("\u001b[33mHow much?\u001b[36m ")
                while expense.isdigit() == False or int(expense) < 1:
                    print("\u001b[31;1mValue must be a positive integer. Try again.\u001b[0m")
                    expense = input("\n\u001b[33mHow much?\u001b[36m ")
                self.monthly_expenses += int(expense)
        return self.monthly_expenses
    
    def get_cash_flow(self):
        print("\n")
        print("\u001b[44;1m~\u001b[0m"*84)
        print("\n\u001b[36mBased on your monthly income and expenses, we can calculate your cash flow.")
        self.cash_flow = self.monthly_income - self.monthly_expenses 
        return self.cash_flow

    def get_investment(self):
        self.initial_investment = 0
        possible_investments = ["Down payment", "Closing costs", "Rehabilitation", "Anything else"]
        print("\n")
        print("\u001b[44;1m~\u001b[0m"*84)
        print("\n\u001b[36mNow we need to calculate your initial investment.\n")
        for item in possible_investments:
            is_there = input(f"\u001b[33m{item}? \u001b[36m(y/n) ")
            while is_there.lower() != 'y' and is_there.lower() != 'n':
                is_there = input("Answer [Y]es or [N]o. ")
            if is_there.lower() == 'n':
                continue
            else:
                investment = input("\u001b[33mHow much?\u001b[36m ")
                while investment.isdigit() == False or int(investment) < 1:
                    print("\u001b[31;1mValue must be a positive integer. Try again.\u001b[0m")
                    investment = input("\n\u001b[33mHow much?\u001b[36m ")
                self.initial_investment += int(investment)
        while self.initial_investment == 0:
                print("\u001b[31;1mInitial investment cannot be 0 (produces infinite return)\u001b[0m")
                self.initial_investment = input("\n\u001b[33mHow much did you really invest?\u001b[36m ")
                while self.initial_investment.isdigit() == False or int(self.initial_investment) < 1:
                    print("\u001b[31;1mValue must be a positive integer. Try again.\u001b[0m")
                    self.initial_investment = input("\n\u001b[33mHow much did you really invest?\u001b[36m ")
                self.initial_investment = int(self.initial_investment)
        return self.initial_investment

    def get_roi(self):
        print("\n")
        print("\u001b[44;1m~\u001b[0m"*84)
        print("\n\u001b[36mNow we can calculate your cash on cash return.")
        print("We find it by dividing your annual cash flow by your initial investment.")
        self.roi = ((self.cash_flow * 12) / self.initial_investment) * 100
        return self.roi

    def get_summary(self):
        print("\nPreparing your summary...")
        entries = [
            ["Market Value", "$ " + str(self.price)],
            ["Monthly Income", "$ " + str(self.monthly_income)],
            ["Monthley Expenses", "$ " + str(self.monthly_expenses)],
            ["Monthly Cashflow", "$ " + str(self.cash_flow)],
            ["Initial Investment", "$ " + str(self.initial_investment)],
            ["Rate of Return", str(self.roi) + "%"]
            ]
        x = ColorTable(theme=Themes.OCEAN)
        x.field_names = ["Category", "Value"]
        x.add_rows(entries)
        # x.align["Category"] = "l"
        x.align["Value"] = "l"
        print(x)

def run_calc():
    print("\n")
    print("\u001b[44;1m#\u001b[0m"*42)
    print("\u001b[44;1m# * * Rental Property ROI Calculator * * #\u001b[0m")
    print("\u001b[44;1m#\u001b[0m"*42)
    price = input("\n\u001b[36mWhat is the market value of the property? (in USD) ")
    while price.isdigit() == False or int(price) < 1:
        print("\u001b[31;1mValue must be a positive integer. Try again.\u001b[0m")
        price = input("\n\u001b[36mWhat is the market value of the property? ")
    property = Property(int(price))
    print(f"\nBased on the the property's market value, you can expect a \u001b[33;1mmonthly income\u001b[0m \u001b[36mof \u001b[33;1m${property.get_monthly_income()}\u001b[0m\u001b[34m.")
    print(f"\nYour \u001b[33;1mmonthly expenses\u001b[0m \u001b[36mare \u001b[33;1m${property.get_expenses()}\u001b[36m.")
    print(f"\nYour \u001b[33;1mmonthly cashflow\u001b[0m\u001b[36m is \u001b[33;1m${property.get_cash_flow()}\u001b[36m.")
    print(f"\nYour \u001b[33;1minitial investment\u001b[0m\u001b[36m is \u001b[33;1m${property.get_investment()}\u001b[36m.")
    print(f"\nYour \u001b[33;1mcash on cash return\u001b[0m\u001b[36m is \u001b[33;1m{property.get_roi()}%\u001b[0m\u001b[36m.")
    property.get_summary()

run_calc()

