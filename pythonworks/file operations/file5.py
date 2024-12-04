all_students1=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\all_students.txt")
failed_students1=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\failed.txt")

all_students=set()
failed_students=set()
for line in all_students1:
    line=line.rstrip("\n")
    
    all_students.add(line)
    
  
for line in failed_students1:
    line=line.rstrip("\n")
   
    failed_students.add(line)

passed_students=all_students.difference(failed_students)
print(passed_students)
all_students1.close()
failed_students1.close()