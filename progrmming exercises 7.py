print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nPROGRAMMING EXECRISES \nQUESTION 7")
# Functions that can calculate projectile motion.
def projectile_motion():
    velocity = eval(input("Enter the velocity of projectile:"))
    angle = eval(input("Enter the angle of projectile:"))
    import math
    time = 2*((velocity*math.sin(angle*math.pi/180))/9.8)
    vertical_range = ((velocity**2)*(math.sin(angle*math.pi/180)**2))/(2*9.8)
    horizontal_range = ((velocity**2)*math.sin (2*(angle*math.pi/180)))/9.8
    decision = input("What would like to find Time , Height or Range:")
    if decision == 'time':
        print("The time taken by the projectile is :"+str(time)+"sec")
    elif decision == 'height':
        print("The maximum height reached by the projectile is:"+str(vertical_range)+"m")
    else:
        print("The maximum distance covered by the projectile is:"+str(horizontal_range)+"m")
    
            
    
