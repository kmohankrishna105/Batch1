str="Welcome to my world Mohan"

#length of string
length= len(str)
print(length)

#Indexing
#Welcome
#0123456

#Slicing
print(str[0:13])
print(str[:13])
print(str[5:13])
print(str[5:])

#upper and lower case
#purpose : passing values externally
str1="Diwali"
print(str1.upper())
lower_Case=str1.lower()
print(lower_Case)

print(str.upper()=="DIWALI")

#splitting the values based on
email = "proseek@gmail.com"
print(email.split('@'))

str1="  proseek "
print(len(str1))
print(len(str1.strip()))

print(str[::-1])
"""

0 1 2 3 4 5 6 7 8
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
-9 -8 -7 -6 -5 -4 -3 -2 -1



0 1 2 3 4 5 6 7 8
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
-9 -8 -7 -6 -5 -4 -3 -2 -1



0 1 2 3 4 5 6 7 8
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
-9 -8 -7 -6 -5 -4 -3 -2 -

Indexing:
Automation is important
0123456789...........20 (From Left to right)
-21,-20,-19...........-1 (From Right to Left)


"""