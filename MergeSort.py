####################################
# NOT FINISHED YET #################
####################################

A = []
for x in range(5):
    A.append(int(input("Enter a Number : ")))
print("Original Array : ", A)

def MERGE(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = [0]
    R = [0]

    for i in range(0,n1):
        L[i] = A[p+i-1]

    for j in range(0,n2):
        R[j] = A[q+j]

    # L[n1 + 1] = 0
    # R[n2 + 1] = 0
    i = 0
    j = 0
    k = p
    for k in range(r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def MERGESORT(A,p,r):
    if p < r:
        q = (p + r) // 2
        MERGESORT(A,p,q)
        MERGESORT(A,q+1,r)
        MERGE(A,p,q,r)

n = len(A)
MERGESORT(A,0,n-1)
print("Sorted Array : ", A)