
A = []
for x in range (5):
    A.append(int(input("Enter a Number : ")))
print("\nNormal Array : ", A)

j = len(A)
def BUBBLESORT(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]

BUBBLESORT(A)
print("Sorted Array : ", A)