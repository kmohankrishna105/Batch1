#Statement 1:
str1="Never share my Password"
#o/p= "password my share never"

#reversing the entire string
print(str1[::-1])

"""
reverse the words
#change to lower case
#1.splithe words - Done
#2.split o/p will be list - Done
#3. print the list from reverse order- Done
"""

words=str1.lower().split()
print(words)
print(words[::-1])

#Problem statement:
List1 =[1,2,3,4,5,3,4,5,6,7,89,98,89]
#for ,if loop retrieve the unique values
new_list =[]
#Do not use set

for each in List1:
    if each not in new_list:
        new_list.append(each)

for each in List1:
    if each in new_list:
        print("already inserted")
    else:
        new_list.append(each)

print("List1" ,List1)
print("new_list" ,new_list)

#Excercie: 3

#2 dicts ----> convert to one single dict

dictpc={"Lenovo":10,"Dell":20}
dictandroid={"MI":30,"Samsung":40}

dict_main={}

for item in [dictpc,dictandroid]:
    dict_main.update(item)
print(dict_main)