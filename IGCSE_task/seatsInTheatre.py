Evening = [[False for _ in range(20)] for _ in range(10)]
for i in range(20):
    Evening[0][i] = True
    Evening[1][0],Evening[1][1],Evening[1][2] = True
# The above code do not need to be written during the exam

# Count and output the number of booked seats
Booked = 0
for row in Evening:
    for seat in row:
        if seat == True:
            Booked += 1

print("Booked seats:", Booked)

# Allow users to input seats required
Require = int(input("Enter the number of seats you need:"))

# Validate the input
Remaining = 20*10 - Booked

while Require < 0:
    Require = int(input("Please enter the number of seats required(>=0):"))

if Require < Remaining:
    if Remaining == 0:
        print("House full")
    else:
        print("Seats left:", Remaining)
else:
    Available_row, Row_remaining = divmod(Booked, 20)
    if Require <= Row_remaining:
        for row in Evening:
            for seat in row:
                if seat == False:
                    seat = True
                    print("Row:", Available_row," Seat:", seat "is booked successfully")
    else:
        for j in range(20 - Row_remaining, 20):
            Evening[Available_row][j] = True
            print("Row:", Available_row," Seat:", j "is booked successfully")
        for j in range(Require - (20 - Row_remaining)):
            Available_row += 1
            Evening[Available_row][j] = True
            print("Row:", Available_row," Seat:", j "is booked successfully")