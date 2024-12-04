arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

flatten_list=[num for ls in arr for num in ls]
print(flatten_list)

num_gt_25=[num for ls in arr for num in ls if num>25]
print(num_gt_25)