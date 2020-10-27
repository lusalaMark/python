# write a program that will have;
# Person        -name#         - talk ()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! i am {self.name}")


# each object is a different instance of an object class
john = Person("Mark Lusala")
john.talk()
cynthia = Person("cynthia muli ")
cynthia.talk()
