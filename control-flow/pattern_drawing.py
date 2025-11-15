pattern_size = int(input("Enter the size of the pattern: "))
while not pattern_size.isdigit() or int(pattern_size) <= 0:
    pattern_size = int(input("Please enter a valid positive integer for the size of the pattern: "))
pattern_size = int(pattern_size)
for i in range(pattern_size):
    for j in range(pattern_size):
        print("*", end=" ")
    print()
    