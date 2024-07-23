'''
    6. Write a Python program to get the sum of a non-negative integer.
    Test Data:
    sumDigits(345) -> 12
    sumDigits(45) -> 9
'''

def sumof(n):
    sum1=0
    while(n>0):
        digit = n % 10
        sum1+=digit
        n = n//10
    return sum1
n = int(input("Enter the number: "))
print(sumof(n))


def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))
print(sumDigits(345))
print(sumDigits(45))

