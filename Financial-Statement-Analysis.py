import os

def Clear():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')
#Data
def Analysis(revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
,expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]):
    Clear()
    #Finding the profit of the company
    profit = [(revenue[i] - expenses [i]) for i in range(len(revenue))]
    #Find the Tax, Profit after tax, average tax and the profit margin
    tax = [round(i * .3, 2) for i in profit]
    profit_after_tax = [(profit[i] - tax[i]) for i in range(len(profit))]
    mean_profit_after_tax = sum(profit_after_tax) / len(profit_after_tax)
    profit_margin = [(int(round(((profit_after_tax[i] / revenue[i])*100),0))) for i in range(len(profit))]
    #Finding the good months, the bad months, each months preformance, the best month and the worst month for the company
    bad_months = list([])
    good_months = list([])
    months_preformance = [good_months.append(i) if profit_after_tax[i] > mean_profit_after_tax else bad_months.append(i) for i in range(len(profit))]
    best_month = ' '.join([str(i+1) if profit_after_tax[i] == max(profit_after_tax) else '' for i in range(len(profit))]).strip()
    worst_month = ' '.join([str(i+1) if profit_after_tax[i] == min(profit_after_tax) else '' for i in range(len(profit))]).strip()

    #Rounding and Casting the figures in the Revenue,Expenses,Profit and Profit After Tax to integers
    revenue_1000 = [int(round(i, 0))for i in revenue]
    expenses_1000 = [int(round(i, 0)) for i in expenses]
    profit_1000 = [int(round(i, 0)) for i in profit]
    profit_after_tax_1000 = [int(round(i, 0)) for i in profit_after_tax]

    print("\nEach months revenue : {0}. \n\nEach months expenses: {1}. \n\nThe profit for each month {2}. \n\nThe profit after tax for each month {3}. \n\nThe profit margin for each month {4}. \n\nThe good months where the profit was above average: {5}.\n\nThe bad months where the profit was below average: {6}.\n\nThe most profitable month {7}.\n\nThe least profitable month {8}.\n".format(revenue_1000,expenses_1000,profit_1000,profit_after_tax_1000,profit_margin,good_months,bad_months,best_month,worst_month))
Analysis()