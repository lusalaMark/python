coordinates = (2, 3, 5)
x, y, z = coordinates
print(x)

person1 = ("mark", 25, "ugali")
person2 = ("mrk", 2, "ali")
people = [person1, person2]
(name, age, favfood) = person1
print(name)
print(age)
print(favfood)

for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()

    ###################     SETS            #######################
    s = {"banas", "Oranges", "mangoes"}
    s.add("strawberry")
    s.add("banas")
    print(s)


library_1 = {"Harry Pooter", "Hunger Games", "Lord of the rings"}
library_2 = {"Harry Pooter", "Romeo and Julliet"}

al_books_in_the_town_libraries = library_1.union(library_2)
print(al_books_in_the_town_libraries)
al_books_in_the_libraries = library_1.intersection(library_2)
print(al_books_in_the_libraries)