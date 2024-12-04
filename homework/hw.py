num=[-1,1,0,-3,3]
result=[]
for i in range(len(num)):
    dlt=num[:i]+num[i+1:]
    total=1
    for j in dlt:
        total=total*j
    result.append(total)
print(result)