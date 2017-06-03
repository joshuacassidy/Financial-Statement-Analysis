#Sample Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

profit = list([])

for i in range (0, len(revenue)):
    profit.append(revenue[i] - expenses [i])

tax = [round(i * .3, 2) for i in profit]

profit_after_tax = list([])
for i in range (0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])

profit_margin = list([])
for i in range (0, len(profit)):
    profit_margin.append(profit_after_tax[i] / revenue[i])

profit_margin = [round((i*100),2) for i in profit_margin]

#Calculate The Mean Profit After Tax For The 12 Months
mean_pat = sum(profit_after_tax) / len(profit_after_tax)

#Find The Months With Above-Mean Profit After Tax
good_months = list([])
for i in range (0, len(revenue)):
    good_months.append(profit_after_tax[i] > mean_pat)

bad_months = list([])

for i in range (0, len(good_months)):
    bad_months.append(not (good_months[i]))
    
best_month = list([])
worst_month = list([])

for i in range(0,len(profit_after_tax)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))

revenue_1000 = [round(i/1000, 2) for i in revenue]
expenses_1000 = [round(i/1000, 2) for i in expenses]
profit_1000 = [round(i/1000, 2) for i in profit]
profit_after_tax_1000 = [round(i/1000, 0) for i in profit_after_tax]

revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax]

print ("Revenue :",revenue_1000,"Expenses : ",expenses_1000,"Profit :",profit_1000,"Profit after tax :",profit_after_tax_1000,"Profit margin :",profit_margin,"Good months :",good_months,"Bad months :",bad_months,"Best month :",best_month,"Worst month :",worst_month) 
