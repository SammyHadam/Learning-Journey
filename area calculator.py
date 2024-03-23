shape = input("Hello, welcome to your area calculator. Please select a shape to calculate the area of. Your choices are a square, rectangle, triangle, or a circle: ")

area = 0

if shape == 'square':
    side = int(input("Please enter a side length for your square: "))
    area = side ** 2
elif shape == 'rectangle':
    length = int(input("Please enter a length for your rectangle: "))
    width = int(input("Please enter a width for your rectangle: "))
    area = length * width
elif shape == 'triangle':
    height = int(input("Please enter a height for your triangle: "))
    base = int(input("Please enter a base for your triangle: "))
    area = (height*base) / 2
elif shape == 'circle':
    radius = int(input("Please enter a radius for your circle: "))
    area = 3.14 * radius ** 2
else:
    print("You did not choose one of the correct shapes.")
    exit()

print(f'The area of your {shape} is {area}')