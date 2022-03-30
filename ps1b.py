annual_salary = int(input("Enter your starting annual salary:​ "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:​ "))
total_cost = int(input("Enter the cost of your dream home:​ "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
current_savings = 0
portion_down_payment = 0.25 * total_cost
num_months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings * 0.04 / 12
    current_savings += (annual_salary / 12) * portion_saved
    num_months += 1
    # increase salary every six months
    if num_months % 6 == 0:
        annual_salary = annual_salary * (1+semi_annual_raise)
print("Number of months: ", num_months)

