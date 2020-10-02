
A = []
for x in range (5):
    A.append(int(input("Enter a Number : ")))
print("Normal Array : ", A, "\n")

n = len(A)
j = 1

def SELECTIONSORT(A):
    for j in range(n-1):
        smallest = j
        for i in range(j+1, n):
            if(A[i] <= A[smallest]):
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

SELECTIONSORT(A)
print("Sorted Array : ", A)