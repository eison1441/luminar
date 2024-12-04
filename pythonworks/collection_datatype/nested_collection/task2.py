student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[50,50,50]
}

# index=int(input("enter the index >>>"))

# for i,element in enumerate(student_data):

#     # if i+1==index:
        
#         marks=student_data.get(element)
#         avg=sum(marks)/len(marks)

#         print(element,avg)

students_avg_mark={k:sum(v)/len(v) for k,v in student_data.items()}
print(students_avg_mark)


