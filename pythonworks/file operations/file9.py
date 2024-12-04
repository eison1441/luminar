# # century year leap year



# f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\years.txt")
# f1=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\leap_year.txt","w")
# f2=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\century_year.txt","w")



# for year in f:
#     year=int(year)
#     if year%100==0:
#         f2.write(str(year)+"\n")
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         f1.write(str(year)+"\n")
# f.close()
# f1.close()
# f2.close()





f_read=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\years.txt")
f_leap=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\leap_year.txt","w")
f_century=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\century_year.txt","w")

def is_century_yr(year):

    return True if year%100==0 else False
def is_leap_year(year):
   if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
       return True
   else:
       return False
   
for year in f_read:
    year=int(year)
    if is_century_yr(year):
        f_century.write(str(year)+"\n")
    if is_leap_year(year):
        f_leap.write(str(year)+"\n")   


    
f_read.close()
f_century.close()
f_leap.close()