# expenses=[10000,11000,12000,10000,15000,10000,13000]




expenses=[10000,11000,12000,10000,15000,10000,13000]
expense_count = {}

for expense in expenses:
    if expense in expense_count:
        expense_count[expense] += 1
    else:
        expense_count[expense] = 1



most_common_expense = max(expense_count, key=expense_count.get)
print(f"The most frequent expense is: {most_common_expense}")
