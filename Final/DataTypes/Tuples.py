
# Creating an empty tuple
Tuple1 = ()
print(Tuple1)

# Creating a Tuple with
# the use of Strings
Tuple1 = ('Cannot','change','tuple')

print(Tuple1)

# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]

print(tuple(list1))

# Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'automation')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)


#Tuple3[0]='not possible'

print(Tuple2.count('python'))
print(Tuple2.index('python'))