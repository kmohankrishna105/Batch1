set ={}

#Create a list with unique values
lang = {'Python', 'C++', 'Java', 'C'}
lang.add("Ruby")
print(lang)

#Duplicates are not allowed
lang.add("Ruby")
print(lang)

#Intersection set
nums = {1, 2, 3, 4, 5 }
oddNums = {1, 3, 5, 7, 9}
nums.intersection_update(oddNums)
print("Updated set: ", nums)

nums1 = {1, 2, 2, 3, 4, 5}
nums2 = {4, 5, 6, 7, 7, 8}
distinct_nums = nums1.union(nums2)
print("The union of two sets is: ", distinct_nums)