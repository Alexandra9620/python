import json

f = open('input_files/Task7.txt', 'r')
company_profit = {}

profit_companies = 0
average_profit = 0

for line in f:
    name, form, income, outcome = line.split()
    income = int(income)
    outcome = int(outcome)
    profit = income - outcome

    company_profit[name] = profit
    if profit > 0:
        average_profit += profit
        profit_companies += 1

f.close()
result = [company_profit, {"average_profit": average_profit / profit_companies}]

f2 = open('output_files/Task7_output.json', 'w')
f2.writelines(json.dumps(result))
f2.close()
