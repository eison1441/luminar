score_dict={"appu":75,
           "ammu":60,
           "akhil":88,
           "gokul":95,
           "praveen":100 }

total=0
num=len(score_dict)
for score_dict in score_dict.values():
    total+=score_dict
average_score = total / num if num> 0 else 0
print(f"The average score is: {average_score:.2f}")