MemberID = ["" for _ in range(1000)]
Name = [["", ""] for _ in range(1000)] # No need in the exam

Num = 0

def Menu():
    print("1. Input a new number")
    print("2. Output a list of membership codes and first & last names")
    print("3. Stop")

# Validate the input
def ValidateID(NewID):
    InValidate = False

    for i in range(Num):
        if NewID == MemberID[i]:
            InValidate = True

    if len(NewID) != 6:
        InValidate = True

    return InValidate

# Input function
def Input():
    global Num
    NewID = input("Please input a new membership code:")

    while ValidateID(NewID):
        NewID = input("This code is not six characters or have existed, please enter again:")

    MemberID[Num] = NewID
    Name[Num][0] = input(f"Please enter the first name of {NewID}:")
    Name[Num][1] = input(f"Please enter the family name of {NewID}:")

    Num += 1

# Main program
Menu()
Choice = int(input("Please enter your choice(1-3):"))
while Choice < 1 or Choice > 3:
    Choice = int(input("Please enter your choice(1-3):"))

# Output all data
while Choice != 3:
  if Choice == 1:
      Input()
  elif Choice == 2:
      for i in range(Num):
          print(f"code: {MemberID[i]}")
          print(f"Name: {Name[i]}")
          print("==============================")
  Menu()
  Choice = int(input("Please enter your choice(1-3):"))

print("exiting...")
