num=int(input("Enter the row >>>"))

for row in range(num,1,-1):

        for speace in range(num-row):
              print(" ",end="")

        for col in range(row-1):
         
            print("* ",end="")
        print()

