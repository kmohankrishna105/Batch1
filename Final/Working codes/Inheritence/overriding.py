
# Parent Class
class A:
    def first(self):
        print("First function of class A")

    def second(self):
        print('Second function of class A')


# Derived Class
class B(A):
    # Overriden Function
    def first(self):
        print("Redefined function of class A in class B")

    def display(self):
        print('Display Function of Child class')

print(__name__)
# main Driver Code
if (__name__ == "__main__"):
    # Creating child class object
    child_obj = B()


    # Calling the overridden method
    print("Method Overriding\n")
    child_obj.first()

    # Calling the original Parent class method
    # Using parent class object.
    A().first()
