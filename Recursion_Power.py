# Using single variable
n = int(input("Enter a Number : "))
def pow(n):
    if n == 0:
        return 1
    else:
        return n * pow(n-1)

print("Power :", pow(n))


# Using two variable
x = int(input("\n\nx : Enter a Number : "))
n = int(input("n : Enter a Number : "))
def pow(x,n):
    if(n == 0):
        return 1
    else:
        return x * pow(x,n-1)

print("\nPower :", pow(x,n))