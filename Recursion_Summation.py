n = int(input("Enter a number : "))
def sum(n):
    if(n == 0):
        return 0
    else:
        return sum(n-1) + n

print("Result :", sum(n))

# Another Method
n = int(input("\n\nEnter a number : "))
def summation(n):
    answer = 0
    for i in range (n+1):
        answer += i
    return answer

print("Result :", summation(n))