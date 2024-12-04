start=int(input("enter the number to strat >>>"))
end=int(input("enter the number to end >>>"))
# step=int(input("enter comon difference >>>"))
if start<end:

   for num in range(start,end+1,1):
    print(num)

else:
  for num in range(start,end-1,-1):
    print(num)
