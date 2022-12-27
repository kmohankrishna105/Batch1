#If condition
age = 60
if age >= 55:
    print("You are a senior")
elif age < 35:
    print("You are a youth")
else:
    print("You are middle aged")

#For Loop

for name in ['Ram', 'Laksman', 'Akbhar','Antony']:
    print(name)

for num in [1,2,3,4,5]:
    print(num+1)

#Use range function
for i in range(2, 9):
    print(i)

Languages1=['pearl', 'C++', 'Python', 'JavaScript', 'Python', 'C++', 'Ruby']
for item in range(len(Languages1)):
    print(Languages1[item])

ages = [78, 34, 21, 47, 9]
for age in ages:
    if age >= 55:
        print("{} is a senior".format(age))
    elif age < 35:
        print(f"{age} is a youth")
    else:
        print(str(age)+ "is middle aged")