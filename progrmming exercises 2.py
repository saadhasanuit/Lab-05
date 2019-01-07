print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nPROGRAMMING EXECRISES \nQUESTION 2")
# Function for area of a rectangle
def area_of_rectangle():
    length = eval(input("Enter the length of the rectangle:"))
    width = eval(input("Enter the width of the rectangle:"))
    area = length * width
    print("The Area of Rectangle is {0:.{1}f}cm\u00b2".format(area,width))
# Function for volume of a rectangle
def volume_of_rectangle():
    length = eval(input("Enter the length of the rectangle:"))
    width = eval(input("Enter the width of the rectangle:"))
    height = eval(input("Enter the height of the rectangle:"))
    volume = length * width * height
    print("The Volume of Rectangle is {0:.{1}f}cm\u00b3".format(volume,width))
    
    
