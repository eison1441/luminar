# st=set()
# se={10,20,30}

# print(se)
# print(type(se))



# st={10,20,30,20,"hai","hloooo"}
# print(st)
# st.add("red")
# print(st)



# arr=[10,10,20,30,40,50,40]

# st=set()
# for num in arr:
#     st.add(num)
# print(st)                                                       


st1={10,20,30,40,50,60}
st={10,20,30,50,89,90,72}

intersection_set=st1.intersection(st)

print(intersection_set)


st1={10,20,30,40,50,60}
st={10,20,30,50,89,90,72}

union_set=st1.union(st)#st1 not mosifying

print(union_set)

st1={10,20,30,40,50,60}
st={10,20,30,50,89,90,72}

difference_set=st1.difference(st)

print(difference_set)



st1={10,20,30,40,50,60}

st1.remove(50)
print(st1)


s3={1,2,3,4,5,}
s2={1,2,3,5,8,9,10}

print(s2.issubset(s3))#subset
print(s3.issuperset(s2))#SUPESET
print(s3.symmetric_difference(s2))
s3.update(s2)#s3 is modifying 
print(s3)


text="this is a test to remove duplicate words this test is simple"

text2="this siple test remove duplicate words"

words=text.split(" ")


print(set(words))
print(set(text2).issuperset(set(text)))