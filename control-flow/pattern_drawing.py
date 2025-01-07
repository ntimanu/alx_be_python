number = int (input("Enter the size of the pattern:"))
i = 0
while i < number:
    for j in range(number):
        print("*", end="")
    print("")
    i += 1