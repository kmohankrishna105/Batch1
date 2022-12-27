first_dict = {
    "name": "Employee1",
    "Dept": "QA",
    "type": "Automation",
    "age": 28,
    "price": "free",
    "work-style": "remote",
}

#Display the value of a key
print(first_dict['Dept'])

print(first_dict.get('Dept'))

#show a default value if key does not exist
print(first_dict.get('Company','XYZ'))

#Display all keys of dict
dict_keys = first_dict.keys()
print(dict_keys)

#Display all values of key
dict_values = first_dict.values()
print(dict_values)

#Display all items of key
items = first_dict.items()
print(items)

#remove item based on key
first_dict.pop("work-style")
print(first_dict)

#Remove item from last
first_dict.popitem()
print(first_dict)


#Nested dictionary with a list and dictionary
main_dict = {
    "name": "Employee1",
    "Dept": "QA",
    "type": ["Automation","Manual"],
    "age": 28,
    "price": {"Morning": 100,"Night" : 200},
    "work-style": "remote"
}

print(main_dict["price"]["Morning"])
print(main_dict["type"][1])

main_dict.clear()
print(main_dict)


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

