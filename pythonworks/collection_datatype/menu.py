orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
order_summery={}
for items in orders:
    if items in order_summery:
        order_summery[items]+=1
    else:
        order_summery[items]=1
print(order_summery)
        