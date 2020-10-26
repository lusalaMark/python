names = ["mark", "bob", "mosh", "sarah", "mary"]
print(names)
numbers = [2, 5, 8, 9, 3, 5, 2, 6]
print(numbers)
numbers.sort()
print(numbers)

print(numbers[:5])  # slicing

for numbers in numbers:
    print(numbers)
names.append("lusala")
print(names)

names = ["mark", "bob", "mosh", "sarah", "mary"]
print(names[2])

names.reverse()

print(names)
names = ["mark", "bob", "mosh", "sarah", "marry"]
print(names[2:])

names = ["mark", "bob", "mosh", "sarah", "marry"]
print(names[2:4])

numbers = [3, 5, 7, 9, 0, 4, 2]
maximum: int = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)

numbers = [3, 5, 7, 9, 4, 2]
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
print(minimum)
