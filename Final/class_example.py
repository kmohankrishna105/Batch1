class employee():
    def __init__(self, name, age, id,  salary):
        self.name=name
        self.age = age
        self.salary = salary
        self.id = id
    def work(self,hrs):
        print(f"I am working for {hrs} hrs {self.name}")


emp1 = employee("Mahesh", 22, 1234,2000)
emp2 = employee("Suresh", 23, 1235,3000)
#print(emp1.__dict__) dictionary

print(emp1.salary)
#print(emp1.name)
print(emp2.salary)
emp1.work(9)
emp2.work(10)