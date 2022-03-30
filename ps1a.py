annual_salary = int(input("Enter your annual salary:​ "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:​ "))
total_cost = int(input("Enter the cost of your dream home:​ "))
current_savings = 0
portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
monthly_return = current_savings * 0.04 / 12
num_months = 0

while current_savings < portion_down_payment:
    current_savings += monthly_return
    current_savings += (monthly_salary * portion_saved)
    num_months += 1
    monthly_return = current_savings * 0.04 / 12
print("Number of months: ", num_months)

