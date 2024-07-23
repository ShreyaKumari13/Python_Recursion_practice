'''
    8. Write a Python program to calculate the harmonic sum of n-1.
    Note: The harmonic sum is the sum of reciprocals of the positive integers.
    Example :  1+1/2+1/3+1/4
'''
# sum1 = 0
# for i in range(1,5):
#     sum1 = sum1 + (1/i)
# print(sum1)
    
def sum1(n):
    if n<2:
        return 1
    else:
        return 1/n + (sum1(n-1))
n = int(input("Enter the number: "))
print(sum1(n))

