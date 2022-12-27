# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

class Above100(Exception):
    "Raised when the input value is above 100"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    if input_num > 100:
        raise Above100

    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")
except Above100:
    print("Is he alive??")
except:
    print("Not a Number")



