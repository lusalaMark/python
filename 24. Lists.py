names = ["mark", "bob", "mosh", "sarah", "mary"]
print(names)
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
numbers.sort()
print(numbers)
print(numbers[2:4])
print(numbers[5:])
print(numbers[0:-1])
print(numbers[0:10:2])
print(numbers[::-1])
print(numbers[5:0:-2])
print(numbers[:5])  # slicing

for i in range(len(numbers)):
    print(numbers[0:i])
window_size = 2

for i in range(len(numbers)-(window_size-1)):
    print(numbers[i:i+window_size])


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
