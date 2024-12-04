users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]


sanju_followers=["sanju","rohit","kohli"]

sugestions=set(users).difference(set(rahul_followers))
# print(user_set)

# rahul_followers_set=set(rahul_followers)

# print(rahul_followers_set)
# sugestion_set

print(sugestions)

mutual_followers=set(rahul_followers).intersection(set(sanju_followers))
print(mutual_followers)         

