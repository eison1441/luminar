expenses=[10000,11000,12000,14000,15000,16000,13000]

exp_count=len(expenses)
sum=0   
for exp in expenses:
    sum+=exp

avg=sum//exp_count
print(avg)



