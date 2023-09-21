# This program is specifically designed only to calculate the dimension changes required for the cv.resize() function

def calculate_new_dimensions(width, height, percentage_change):
    new_width = width + (width * percentage_change / 100)
    new_height = height + (height * percentage_change / 100)
    return new_width, new_height

width = float(input("Enter the initial width: "))
height = float(input("Enter the initial height: "))

percentage_change = float(input("Enter the percentage change (positive for increase, negative for decrease): "))

new_width, new_height = calculate_new_dimensions(width, height, percentage_change)

print(f"Initial dimensions: {width} x {height}")
print(f"New dimensions after {percentage_change}% change: {new_width} x {new_height}")
