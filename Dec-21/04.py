           
def get_square(height, width = None):
    rectangle_formula = height * width
    square_formula = height**2 or width**2
    if height == True and width == True:
        return rectangle_formula
    elif height == True and width == None:
        return square_formula

result = get_square(7, 4)
print(result)  