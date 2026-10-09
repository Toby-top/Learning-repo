def tri(n):
    Symbol = input("What do you want for this triangle (SINGLE Letter):")
    print("Hollow Triangle of height", n, ":")
    mid = 1
    for i in range(n):
        # for j in range((n-1)/2):
            print(" " * (n-1)/2, Symbol )
