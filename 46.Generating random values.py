import random

for i in range(4):
    print(random.randint(12, 90))

for i in range(4):
    print(random.random())

members = ["mark", "lusala", "sailas", "faith", "sheila", "kilmon"]
pastors = random.choice(members)
print(pastors)

# write a program that when a dice is thrown the walues changes as per the toss
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
