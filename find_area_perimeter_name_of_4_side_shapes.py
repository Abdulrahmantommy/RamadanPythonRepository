"""
Training program to find the area and perimeter of a 4-side regular shape and the name of this shape
parameters:
height : the height of the shape
width : the width of the shape
returns:
shape name : square or rectangle
area : the area value of that shape
perimeter: the perimeter value  of the shape 
"""
height=float(input("Enter the height of your shape: "))
width=float(input("Enter the width of your shape: "))
shape = " "
if height == width:
    shape = "square"
else:
    shape = "rectangle"
area = height * width
perimeter = (height + width) * 2
print("The area of your {0} is : {1} and its perimeter is {2}".format(shape, area, perimeter))
    
