n=int(input("Enter a number >>>"))
prev=0
cur=1
is_febo=False

for i in range(1,n-1):
    next=prev+cur
    prev=cur
    cur=next
    if next==n:
        is_febo=True

        break

print(is_febo)
