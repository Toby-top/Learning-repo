# Generate 100,000 random integers between 1 and 10, count the frequency of each integer, sort them in descending order based on their frequency, and output the integers along with their chances of occurrence.

import random

# declare array
RandomNumber = [0] * 100000
CountedNumber = [[0 for _ in range(2)] for _ in range(100000)]

# generate random integers
for i in range(100000):
    RandomNumber[i] = random.randint(0, 10)

# count the frequency
def Count(Value):
    Frequency = 0 
    for i in range(100000):
        if RandomNumber[i] == Value:
            Frequency += 1
    return Frequency

for Value in range(10):
    CountedNumber[Value][0] = Value + 1
    CountedNumber[Value][1] = Count(Value)

# sort the contents in the counted array
for i in range(10):
    for j in range(10 - 1 - i):
        if CountedNumber[j][1] < CountedNumber[j + 1][1]:
            Temp = CountedNumber[j]
            CountedNumber[j] = CountedNumber[j + 1]
            CountedNumber[j + 1] = Temp

# output values along with their chance
for i in range(10):
    Chance = CountedNumber[i][1] / 100000
    Chance = round(Chance, 4)
    print("Number:", CountedNumber[i][0], "with chance:", Chance)