class mammal :
    def walk(self):
        print("walk")


class Dog (mammal):
    def bark(self):
        print("bark")
class cat (mammal):
    def be_annoying(self):
        print("annoying")
cat1 = cat()
cat1.be_annoying()
