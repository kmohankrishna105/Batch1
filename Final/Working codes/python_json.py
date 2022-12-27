# Python program for json package

import json

# {key:value mapping}
a ={"Application":"Ecommerce","type":"online","Space":25000}

print(type(a))
# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)
print(type(b))


x ='''{"Application":"insurance","type":"offline","Space":5000}'''
print(type(x))
# conversion to JSON done by dumps() function
y = json.loads(x)

# printing the output
print(y)
print(type(y))

