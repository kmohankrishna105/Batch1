#Break --- If a condition is met, exit the loop

# Continue --> Perform the action and loop the other values
"""

list1=[1,2,3,4,5,6,7,8,9]
for item in list1:
    print(item)
    if item ==5:
        print("matching")
        #break
    continue

#Statement: Check for a user Kiran and execute with the login credentials and exit

#Statement: Check for a user Kiran and execute with the login credentials and continue with other users

flag =0
print(f"initial flag value {flag}")
list1=[1,2,3,4,5,6,7,8,9,5]
for item in list1:
    if item ==5:
        flag=1
        print(item)
        print("matching")
        break
print(f"Final flag value {flag}")
"""

list1=[1,2,3,4,5,6,7,8,9,5]
for item in list1:
    if item ==5:
        print(item)
        print("matching")
        list1.remove(item)
        continue
print(list1)