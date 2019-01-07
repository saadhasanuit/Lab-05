print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nQUESTION 3")
# program which takes the limit for while loop condition and sum the total amount
n = eval(input("Enter the value to execute the for loop:"))
sum = 0
i = 1
for i in range (0,n+1):
    sum = sum + i
    i = i+1
print("The sum is", sum)
