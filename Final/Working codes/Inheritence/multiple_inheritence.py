class A1:
    def A1_method(self):
        print("this is A1 method")

class B1:
    def B1_method(self):
        print("this is B1 method")

class child_class(A1,B1):
    def child_method(self):
        print("This is child method")


child=child_class()
child.child_method()
child.B1_method()
child.A1_method()