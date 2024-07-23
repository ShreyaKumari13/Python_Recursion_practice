'''
    10. Write a Python program to calculate the value of 'a' to the power 'b'.
    TestData :  (power(3,4) -> 81           
'''
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif a==0:
        return 0
    else:
        return a**b
n = int(input("Enter the number:"))
m = int(input("Enter the power:"))
print(power(n,m))