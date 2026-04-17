import random

# declare array
RandomNumber = [0] * 100000
CountedNumber = [[0] for _ in range(100000)]

# generate random integers
for i in range(100000):
    RandomNumber[i] = random.randint(1, 10)

