"""
Parent class : Student 1
Child class : Student 2

student 2 is inheriting student 1 class properties and methods
Hint: parent constructor is called in child class (line 23). This is done in child constructor

function overriding
What is overriding?
Defining a method in the child class with the same name of a method in the parent class

Example:
Method : show() in parent class
show is in child class also .
So first child method is called and mobile number(from child class) is displayed instead of landline(from parent class)

If not overridden:
student 3 has no show() method. Hence orginal parent method from student 1 is used.

Method Arguments
Positional: (line 70)
While calling function , arguments need to be passed in the same order as their respective parameters in the function definition.

Keyword Arguments:(line 72)
while calling function , passing each argument in the form name = value.

Mixing Positional and Keyword arguments (line 74)
positional arguments cannot appear after any keyword arguments have been defined.
Positional arguments comes first and than keyword arguments

Default Arguments:(line 61)
Arguments passed during method definition

rectangle_area()            # this function call uses the default arguments
rectangle_area(10, 5)       # positional arguments width=10 length=5
rectangle_area(width=10)     # this will set length to use the default value, 2
rectangle_area(length=4, width=45)      # keyword arguments
rectangle_area(15)           # sets width = 15 and length uses the default value

"""
class student_1():
    def __init__(self, rollno, name, landline):
        self.rollno=rollno
        self.name=name
        self.name=name
        self.landline=landline
    def show(self):
        print(self.rollno,self.name,self.landline)

class student_2(student_1):
    def __init__(self,rollno,name,mobile,address,landline):
        self.mobile=mobile
        self.address=address

        student_1.__init__(self, rollno, name, landline)

    def show(self):
        print(self.rollno,self.name,self.mobile,self.address)

class student_3(student_1):
    def __init__(self,rollno,name,mobile,address,landline=4198):
        self.mobile=mobile
        self.address=address

        student_1.__init__(self, rollno, name, landline)

    def details(self):
        print(self.rollno,self.name,self.mobile,self.address,self.landline)

s1=student_1(111,"student1",222)
s1.show()
s2=student_2(rollno=222,name="student2",mobile=567,address="Vizag",landline=123)
s2.show()
s3=student_3(333,name="student3",mobile=7398,address='Hyd')
s3.show()