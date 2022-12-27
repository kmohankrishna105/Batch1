# a list of programming languages
languages=['Python', 'C++', 'JavaScript']

# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]


list1 = ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# first item
print(list1[0])

# third item
print(list1[2])

# fifth item
print(list1[4])

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])
print(n_list[1][3])

#Change the list item based on index
languages[0]= 'pearl'
print(languages)


#Add item to list based on position
languages.insert(2, "Python")
print(languages)

#Add item to the end of the list
languages.append("Python")
print(languages)

#Add a new list to existing list
languages.extend(["C++","Ruby"])
print(languages)

#Remove Specified Item
languages.remove("JavaScript")
print(languages)

#Remove the second item
languages.pop(1)
print(languages)

Languages1=['pearl', 'C++', 'Python', 'JavaScript', 'Python', 'C++', 'Ruby']
#Looping through list
for x in Languages1:
  print(x)

#looping through the list with index numbers
for i in range(len(Languages1)):
  print(Languages1[i])

#sorting Lists
Languages1.sort()
print(Languages1)

#reversing an list
new_list=[1,2,3,4,5,6,7]
new_list.reverse()
print(new_list)

# Joining two list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


my_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(my_list[1::2])


string = "This is a string."
string_list = string.split(' ') #delimiter is ‘space’ character or ‘ ‘
print(string_list) #output: ['This', 'is', 'a', 'string.']
print(' '.join(string_list)) #output: This is a string.

