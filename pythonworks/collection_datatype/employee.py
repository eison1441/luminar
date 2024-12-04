employee={"eid":100,
          "name":"eison",
          "salary":50000,
          "department":"ceo",
          "experience":5
          }
employee["contact"]=9497581441
# if employee["experience"]>5:
#     employee["salary"]+=10000
# else:
#     employee["salary"]+=5000
if employee["experience"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="JDE"


print(employee)

# "this is a simple program "