#Getting Keyboad input
n = int(input("Enter a number :"))

# Implement sumcube function
def sumcube(n):
    if n == 1: # check the value is 1
        return 1
    else:
        return (sumcube(n-1) + (n * n * n)) #calsulation

# Run the program
while (n != -1): # Check number is equal to -1
    #Call the sumcube function
    print("Result :", sumcube(n))
    # Getting next input
    n = int(input("Enter a number :"))