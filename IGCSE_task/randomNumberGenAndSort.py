import random

# declare array
RandomNumber = [0] * 100000
CountedNumber = [[0] for _ in range(100000)]

# generate random integers
for i in range(100000):
    RandomNumber[i] = random.randint(1, 10)

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
            Temp = CountedNumber[j][1]
            CountedNumber[j][1] = CountedNumber[j + 1][1]
            CountedNumber[j + 1][1] = Temp
