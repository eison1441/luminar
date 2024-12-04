text="ABAABABC"
get_count=lambda ch:text.count(ch)

most_frequent_ch=max(text,key=get_count)
print(most_frequent_ch)


most_frequent_ch=min(text,key=get_count)
print(most_frequent_ch)