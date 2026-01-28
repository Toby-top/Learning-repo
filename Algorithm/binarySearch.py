import random
from time import time
start_time = time()
length =78
Array = [random.randint(0,20045678765) for _ in range(length)]
n = 1
MaxGroup = ["" for _ in range(10)]
MinGroup = ["" for _ in range(10)]

Max = Array[0]
Min = Array[1]

if Array[0] < Array[1]:
    Max = Array[1]
    Min = Array[0]

for i in range(2, length, 2):
    n+=1
    if Array[i] > Array[i+1]:
        if Array[i]>Max:
            Max = Array[i]
        if Array[i+1] < Min:
            Min = Array[i+1]
        n += 2
    else:
        if Array[i+1]>Max:
            Max = Array[i+1]
        if Array[i] < Min:
            Min = Array[i]
        n += 2




print(Array)
print(Min)
print(Max)
print(n)
end_time = time()
print(f"{end_time - start_time:.4f} seconds")
