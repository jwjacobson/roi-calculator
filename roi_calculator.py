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
        

#INCOME
rental_income = 2000
total_income = rental_income

#EXPENSES
tax = 150
insurance = 100
utilities = 0
    # electric
    # water
    # sewer
    # garbage
    # gas
hoa = 0
# lawn/snow = 0
vacancy = 100 # 5%
repairs = 100
cap_ex = 100
prop_man = 200
mortgage = 860

total_expenses = 1610

#CASHFLOW
cashflow = total_income - total_expenses

#CASHONCASH ROI
down_payment = 40000 # 20%
closing_costs = 3000
rehab = 7000
misc = 0

total_investment = 50000

# roi = annual_cash_flow / total_investment

def run_calc():
    print("Rental Property ROI calculator.")
    price = input("How much will you pay for the property? ")
    property = Property(int(price))
    monthly_income = property.get_monthly_income()
    print(f"Based on the price of the property, you can expect a monthly income of {monthly_income}.")

run_calc()
