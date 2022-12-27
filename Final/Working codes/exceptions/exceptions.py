a=input("Enter value a:")
b=input("Enter value b:")

try:
    c=int(a)+int(b)
    print(c)
except:
    print("Value entered are not Numbers...Please check")
#    exit()
finally:
    print("Sum action executed successfully")

