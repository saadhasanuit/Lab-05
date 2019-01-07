print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nPROGRAMMING EXECRISES \nQUESTION 1")
# Function for area of a cylinder
def area_of_cylinder():
    radius = eval(input("Enter the radius of the cylinder:"))
    height = eval(input("Enter the height of the cylinder:"))
    from math import pi
    area = (2*pi*radius*height) + (2*pi*(radius)**2)
    print("The Area of Cylinder is {0:.{1}f}cm\u00b2".format(area,height))
def volume_of_cylinder():
    radius = eval(input("Enter the radius of the cylinder:"))
    height = eval(input("Enter the height of the cylinder:"))
    from math import pi
    volume = pi*(radius**2)*height
    print("The Volume of Cylinder is {0:.{1}f}cm\u00b3".format(volume,height))
    
