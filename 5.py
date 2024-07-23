'''
    5. Write a Python program to solve the Fibonacci sequence using recursion.
'''
# def fibonacci(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# n = int(input("Enter the number: "))
# print(fibonacci(n))

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 5
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))