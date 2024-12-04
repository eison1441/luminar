# expenses=[10000,11000,12000,14000,15000,16000,13000]

# for exp in expenses:

#     print(exp)



expenses=[10000,11000,12000,14000,15000,16000,13000]

max=0
for exp in expenses:

    if exp>max:
        max=exp

min=expenses[0]

print(min)

for exp in expenses:

    if exp<min:
        min=exp
    
print(max)








