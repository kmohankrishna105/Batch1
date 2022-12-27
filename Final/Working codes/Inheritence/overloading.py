# Function to take multiple arguments
# *- defines any number of arguments

item=['a',1,'b',2]
for n in item:
    print(n)

def sum_number(*args):
    result = 0
    for num in args:
        result =result+ num
    print("Sum : ", result)


sum_number(10)
sum_number(30, 2)
sum_number(1, 2, 3, 4, 5)

List_num =[1,4,3,4,6,7,4,2,43,1,2]
sum_number(*List_num)
