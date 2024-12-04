def find_closest_to_zero(nums):
    closest_num = nums[0]
    min_distance = abs(nums[0])

    for num in nums[1:]:
        distance = abs(num)
        if distance < min_distance:
            min_distance = distance
            closest_num = num
        elif distance == min_distance and num > closest_num:
            closest_num = num
    
    return closest_num


nums1 = [-42, 1, 4, 8]
print(find_closest_to_zero(nums1))  

nums2 = [2, -1, 1]
print(find_closest_to_zero(nums2)) 