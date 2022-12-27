class dog():
    def __init__(self, breed,name):
        self.breed=breed
        self.name=name
        print("Book created successfully")
        #print("Is the breed " + breed)

    def __str__(self):
        return self.name

    def __len__(self):
        return "Length of book is 499 pages"

    def __del__(self):
        print ("Book deleted for ever")

p=dog("Husk","Rambo")
print(p.__len__())
