n=int(input("enter the number >>>"))
i=0
b1=0
b2=1
f=0
while(i<=n):
    b1=b2
    b2=f
    f=b1+b2
    print(f)