"""
current_age = int(input("How old are you? "))
future_age = current_age + 27
print(f"In 2050, you will be ", future_age, " years old.")
"""
rows = 5

i = 0
while i <= rows:
    j = 0
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1