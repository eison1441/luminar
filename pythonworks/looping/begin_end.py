begin=int(input("enter the starting limit >>>"))
end=int(input("enter the limit >>>"))


reverse=True if begin>end else False

i=begin

while(i<=end if reverse==False else i>=end):
    if i%2!=0:
        print(i)

    if reverse==False:
        i=i+1
    else:
        i=i-1