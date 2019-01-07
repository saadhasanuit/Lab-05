print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nPROGRAMMING EXECRISES \nQUESTION 3")
# A function that can calculate the arithmetic sequence of n numbers.
def arithmetic_sequence():
    a=eval(input("Input the value of first term :"))
    d=eval(input("Input the value of common difference :"))
    nth=eval(input("Input the nth term :"))
    # Applying the nth term formula
    x=a+((nth-1)*d)
    print("The first value when n is " , nth , "=" ,x)
    while True:
        question=input("If you want continue enter YES or NO :")
        if (question == "yes"):
            nth=eval(input("Input the nth term :"))
            x=a +((nth-1)*d)
            print("The second value when n is " , nth , "=" , x)
        else:
            print("Thank You!")
            break
        
