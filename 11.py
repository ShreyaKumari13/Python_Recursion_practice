'''
    11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
'''
# def gcdof(a,b):
#     while a!=b:
#         if a>b:
#             a = a-b
#         else:
#             b = b-a
#         return b
# n = int(input("Enter the number:"))
# m = int(input("Enter the power:"))
# print(gcdof(n,m))


def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
a = 12
b = 6
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')
    
