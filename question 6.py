print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nQUESTION 6")
# Function which takes no argument and generate and print a list of first and last 6 elements where the values are cube of numbers between 1 and 30.
def CubeValues():
    lst = list()
    for i in range(1,31):
        lst.append(i**3)
    print(lst[:6])
    print(lst[-6:])

CubeValues()
