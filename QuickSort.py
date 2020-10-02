
A = []
for x in range (5):
    A.append(int(input("Enter a Number : ")))
print("\nNormal Array")
print(A)

n = len(A)
r = n-1
p = 0

def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if(A[j] <= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

result = PARTITION(A,p,r)
print(result)

def QUICKSORT(A,p,r):
    if (p < r):
        q = PARTITION(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)

QUICKSORT(A,p,r)
print("\nSorted Array")
print(A)