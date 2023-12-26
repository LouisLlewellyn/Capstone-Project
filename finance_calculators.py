# This is a program that calculates different investment or loan types from the information 
# the user inputs and outputs the results back to them.

import math
invest_type = input("Investment  - to calculate the amount of interest you'll earn on your investment\n\
Bond        - to calculate the amount you'll have to pay on a home lone \n \
    \n\
Enter either 'Investment' or 'Bond' from the menu above to proceed: ")
print(" ")

# Investment calculations
if(invest_type.lower() == "investment"):
    print("Investment option-")
    invest_money = float(input("Enter amount of money you will be investing: "))
    invest_rate = float(input("Enter the interest rate(%): "))
    invest_rate1 = float(invest_rate / 100) 
    invest_years = int(input("Enter the number of years you plan to invest: "))
    print(" ")
    invest_type2 = input("Please enter the type of investment you would like, 'simple' or 'compound': ")
    # 'Simple' investment calculations    
    if(invest_type2.lower() == "simple"):
        invest_simple = invest_money * (1 + invest_rate1 * invest_years)
        simple_diff = invest_simple - invest_money
        print(f"\nYour deposit of £{invest_money:.2f}, after {invest_years}years, will have grown to £{invest_simple:.2f}. An increase of £{simple_diff:.2f}")
    # 'Compound' investment calculations    
    elif(invest_type2.lower() == "compound"):
        invest_compound = invest_money * math.pow((1 + invest_rate1), invest_years)
        compound_diff = invest_compound - invest_money
        print(f"\nYour deposit of £{invest_money:.2f}, after {invest_years}years, will have grown to £{invest_compound:.2f}. An increase of £{compound_diff:.2f}")
    else:
        print("\nSorry, your entry was not recognised, please start again.")     
    
# 'Bond' calculations    
elif(invest_type.lower() == "bond"):
    print("Bond option:")
    bond_value = float(input("Enter the value of your property: "))
    bond_rate = float(input("Enter the interest rate(%): "))
    bond_rate1 = float(bond_rate / 100)
    bond_rate2 = float(bond_rate1 / 12)
    bond_months = int(input("Enter the number of months you wish to repay the bond: "))
    bond_payments = (bond_rate2 * bond_value) / (1 - (1 + bond_rate2) ** (-bond_months))

    print(f"\nYour home lone repayments, for the next {bond_months}months, will be £{bond_payments:.2f} per month.")   

else:
    print("Sorry, your entry was not recognised, please start again.")