class A1:
    def A1_method(self):
        print("this is A1 method")

class A2(A1):
    def A2_method(self):
        print("this is A2 method")

class child_class(A2):
    def child_method(self):
        print("This is child method")


child=child_class()
child.child_method()
child.A1_method()
child.A2_method()