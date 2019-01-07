print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nPROGRAMMING EXECRISES \nQUESTION 6")
# Multiple functions that can calculate three laws of motions in physics.
def first_law_of_motion():
    Vi = int(input("Enter the initial velocity of the object:"))
    a = int(input("Enter the accelaration of the object:"))
    t = int (input("Time taken by the object:" ))
    Vf = Vi + (a*t)
    print("The Final Velocity of the object is:",Vf, " m/s")
def second_law_of_motion():
    Vi = eval(input("Enter the initial velocity of the object:"))
    a = eval(input("Enter the accelaration of the object:"))
    t = eval(input("Time taken by the object:"))
    S =  Vi*t+ 1/2*(a*(t**2))
    print("The distance taken by the object is:",str(S),"m")
def third_law_of_motion():
    vf = int(input("Enter the final velocity of the object:"))
    vi = int(input("Enter the initial velocity of the object:"))
    decision = (input("What does you want to find,Acceleration or Distance..?"))
    if decision == 'acceleration':
        s = int(input("Enter the distance cover by object in metres(m):"))
        a = ((vf**2)-(vi**2))/(2*s)
        print("The acceleration of the object at that time will be:",a,"m/s²")
    else:
        a = int(input("Enter the accelaration of the object in m/s²:"))
        s = abs(((vf**2)-(vi**2))/(2*a))
        print("The distance covered by the object is:", s,"m")
        
