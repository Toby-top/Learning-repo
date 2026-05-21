import random # No need in exam

# Initialise the array
Rainfall = [0] * 365

# Input data
for i in range(365):
    # Rainfall[i] = int(input("Plz enter the rainfall of the day (mm)"))
    Rainfall[i] = random.randint(0, 24) # No need in exam
# NEXT i

# Calculate the statistics
TotalRainfall = 0
AvgRainfall = 0
TotalNoRainDays = 0
CountNoRainDays = 0
LongestNoRainDays = 0 

# for i in range(365):
#     TotalRainfall += Rainfall[i]
#     if Rainfall[i] == 0:
#         TotalNoRainDays += 1
#         if Rainfall[i - 1] == 0: 
#             CountNoRainDays += 1
#         if CountNoRainDays > LongestNoRainDays:
#             LongestNoRainDays = CountNoRainDays + 1
#     elif Rainfall[i] != 0:
#         CountNoRainDays = 0

for i in range(365):
    TotalRainfall += Rainfall[i]
    if Rainfall == [0]:
        TotalNoRainDays += 1
        if TotalNoRainDays > LongestNoRainDays:
            LongestNoRainDays = TotalNoRainDays
        # ENDIF
    else:
        TotalNoRainDays = 0
    # ENDIF
# NEXT i

AvgRainfall = TotalRainfall / 365
AvgRainfall = round(AvgRainfall, 4)

TotalRainfall = TotalRainfall / 10
TotalRainfall = round(TotalRainfall, 2)

# Output the result
print("The total rainfall of the year is ", TotalRainfall, "cm")
print("The daily average rainfall is ", AvgRainfall, "mm")
print("The number of days with no rain is ", TotalNoRainDays, "days")
print("The longest consecutive days with no rain is ", LongestNoRainDays, "days")

# Checking if there is drought
if LongestNoRainDays >= 15:
    print("There is drought")
else:
    print("No drought")
# ENDIF