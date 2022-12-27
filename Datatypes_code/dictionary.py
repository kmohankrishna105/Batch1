
# Please provide me all the keys of a dict, then fetch their values using keys

"""
#i/p


#O/P
Value of ABC is 10
Value of XYZ is 30
Value of PQR is 50
"""
dict1={"ABC" : 10,"XYZ" : 30,"YRT": 50}

print(dict1['XYZ'])
for each in dict1:
    print(f"value of {each} is {dict1[each]}")


key_m=dict1.keys()
print(key_m)
for item in key_m:
    print(item)
    print(dict1[item])

# dictionary -
#keys()
#values

dict2={"ABC" : 10,"XYZ" : 30,"YRT": 50,"ABC1" : 70,"XYZ1" : 80,"YRT1": 90}
print(dict2.keys())
for point in dict2.items():
    print(point)
    print(type(point))
    print(point[0])

#print(dict2['EFG'])

#Real time
# get the marks for all students, and mark absent for those which do not have records
#get
print(dict2.get('ABC'))
print(dict2.get('EFG','ABSENT'))

"""
#problem statement
#I have a list of employee
#Now check the employee in the deparment dict and find the depart
# if department is not assigned...tell me that he is new joinee

# Solution - Hint
employee=[6 items]
department={4 items,   employee : department name}
use for loop to iterate all employee
    and check the deartment
    else print default
"""

employee=["krish","chaitu","kiran","ram","maruthi","tharun"]
department={"krish":"qa","chaitu":"qa","kiran":"dev","Ram":"support"}
for each in employee:
    if each in department:
        print(department[each])
    else:
        print("new joined")

#employee
list=['A','B','C','D','E']
#department
dict={'A':"QA",'B':"DEV",'C':"SUPPORT"}
for item in list:
    # print(dict[item])
    # print(item)
    print(dict.get(item,"new join"))


dict3={"ABC" : 10,"XYZ" : 30,"YRT": 50,"ABC1" : 70,"XYZ1" : 80,"YRT1": 90}
print("Old",dict3)

#Adding new item or changing value
dict3['YRT'] = 'New value'
dict3['EFG'] = 'New item'


print("New",dict3)

dict3={"ABC" : 10,"XYZ" : {'x':1,'y':2,'z':10},"YRT": 50,"ABC1" : 70,"XYZ1" : 80,"YRT1": 90}

print(dict3['XYZ']['y'])

"""
diff in list and dict
In list , we are providing the index value
In dictionary, we shall the key's directly'
"""

# Sets
"""
list vs sets
lists- allow duplicates
sets - unique values no duplicates
"""

list_new = [3,4,5,6,7,8,3,4,5,6,7,8,8,7,6,5,4,3,4,4,5]
print(list_new)
print(set(list_new))
