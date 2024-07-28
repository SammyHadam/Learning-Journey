while True:
    i = 0
    total = 1
    number = int(input("Please type in a number: "))
    if number == 1:
        print("The factorial of the number 1 is 1")
    while i < number:
        i += 1
        total *= i
    if number <= 0:
        print("Thanks and bye!")
        break
    elif number > 1:
        print(f"The factorial of the number {number} is {total}")