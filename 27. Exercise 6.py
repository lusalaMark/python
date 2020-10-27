#Write a program to remove the duplicates in a list
numbers =[2,3,5,4,7,5,5,8,8,8,8,8,9]
uniques = []
for number in numbers :
    if number not in uniques :
        uniques.append(number)
print(uniques)
