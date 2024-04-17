# Paint can calculator
# Done without math.ceil like an idiot
def paint_calc(height, width, cover):
  number_of_cans = ((height * width) / cover)
  if number_of_cans - round(number_of_cans) < 0.6 and number_of_cans - round(number_of_cans) > 0.0:
    number_of_cans += 1
    print(f"You'll need {round(number_of_cans)} cans of paint.")
  else:
    print(f"You'll need {round(number_of_cans)} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
