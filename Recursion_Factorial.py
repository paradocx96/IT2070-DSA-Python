n = int(input("\n\nEnter a Number : "))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial : ", factorial(n))


# This is not for factorial
# n = int(input("Enter a Number : "))
# def f(n):
#     if(n%2 == 0):
#         return n/4
#     else:
#         return f(n+1)
#
# print("Result :", f(n))