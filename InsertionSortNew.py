A = []
for x in range(10):
    A.append(int(input("Enter a number : ")))
print("Inputed array : ", A)


def INSERTION_SORT(A):
    for j in range(1,len(A)):
        i = 0
        
        while (A[j] > A[i]):
            i = i + 1
        key = A[j]

        for k in range(j-i):
            A[j-k] = A[j-k-1]
        A[i] = key


INSERTION_SORT(A)
print("Sorted Array : ", A)
