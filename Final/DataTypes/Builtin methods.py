#ZIP

numbers = [1,2,3]
str_numbers = ['One','Two','Three']
result = zip(numbers, str_numbers)
print(result)
print(list(result))

#ALL
lst = []
print(all(lst)) # Returns True for empty list

nums = [1, 2, 3, -4, -5]
print(all(nums)) # Returns True

nums = [0, 1, 2, 3]
print(all(numbers)) # Returns False because of 0

data = [1, 'Phone', 12.5, 5, False]
print(all(data)) # Returns False because of False

#Type
lang = 'Python'
nums = [1,2,3,4]
nums_dict = {'one':1,'two':2,'three':3}

print(type(nums))
print(type(lang))
print(type(nums_dict))

nums = [2,1,5,3,4]
asc_nums = sorted(nums)
dsc_nums = sorted(nums, reverse = True)
print("Ascending Numbers: ", asc_nums)
print("Descending Numbers: ", dsc_nums)

print(10 > 9)
print(10 == 9)
print(10 < 9)