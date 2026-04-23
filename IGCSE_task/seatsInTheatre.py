Evening = [[False for _ in range(20)] for _ in range(10)]
Evening[0] = True
# The above code do not need to be written during the exam

# Count and output the number of booked seats
Booked = 0
for i in range(10):
    for j in range(20):
        if Evening[i][j] == True:
            Booked += 1

print("Booked seats:", Booked)

