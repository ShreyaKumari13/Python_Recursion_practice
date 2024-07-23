'''
    4. Write a Python program to get the factorial of a non-negative integer.
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number: "))
print(fact(n))

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * (factorial(n - 1))
print(factorial(5))
