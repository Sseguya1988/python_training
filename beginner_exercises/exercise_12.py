# Exercise 12: Calculate income tax for the given income by adhering to the rules below
def income_tax(salary):
    salary_num = int(salary)
    if salary_num <= 10000:
        tax_income = 0
    elif salary_num <= 20000:
        tax_income = 10000*0.1
    else:
        tax_income = 10000*0.1 + (salary_num - 20000)*0.2
    return tax_income


# apply this function
salary = input("Enter your salary, to compute your income tax: ")
result = income_tax(salary)
print(f"Your calculated income tax is {result}")
