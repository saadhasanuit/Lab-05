print("MUHAMMAD SAAD HASAN \n18B-117-CS \nSECTION:-A \nLAB 05 \nPROGRAMMING EXECRISES \nQUESTION 4")
# A function which will check either the giving string is Palindrome or not Palindrome.
def palindrome_string():
    string = input("Please enter the word:")
    string = string.casefold()
    rev = reversed(string)
    if list(string) == list(rev):
        print("This is a Palindrome")
    else:
        print("This is a not a Palindrome")
