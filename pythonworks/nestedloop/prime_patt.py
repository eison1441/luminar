start=int(input("Enter starting point >>>"))

end=int(input("Enter the limit >>>"))


for num in range(start,end+1):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False


            break

    if is_prime==True:

       

        for row in range(num):
             for col in range(1,row+1):
                 print(num,end="\t")

             print()

