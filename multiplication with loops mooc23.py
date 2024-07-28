number = int(input("Please type in a number: "))

while number > 0:
    x = 0
    i = 1
    while x < number and i <= number:
        x += 1
        total = x * i
        print(f"{i} x {x} = {total}")
        if x == number:
            i += 1
            x = 0
    break