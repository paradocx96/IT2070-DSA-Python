
n = int(input("Enter a Number : "))

def pow(n):
    if(n == 0):
        return 1
    else:
        return (n * pow(n-1))

print("Factorial :", pow(n))

# def f(n):
#     if(n%2 == 0):
#         return n/4
#     else:
#         return f(n+1)
#
# print("Result :", f(n))

# def sum(n):
#     if(n == 1):
#         return 1
#     else:
#         return sum(n-1) + n
#
# print("Result :", sum(n))

# def summation(n):
#     answer = 0
#     for i in range (n+1):
#         answer += i
#     return answer
#
# print("Result :", summation(n))

