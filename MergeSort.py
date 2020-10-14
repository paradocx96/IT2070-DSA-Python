####################################
############ FINISHED ##############
####################################

A = []
for x in range(5):
    A.append(int(input("Enter a Number : ")))
print("Original Array : ", A)

def MERGESORT(A,p,r):
    if p < r:
        q = (p + r) // 2
        MERGESORT(A,p,q)
        MERGESORT(A,q+1,r)
        MERGE(A,p,q,r)

def MERGE(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []

    for y in range(0,n1+1):
        L.append(0)
    for z in range(0,n2+1):
        R.append(0)

    for i in range(0,n1):
        L[i] = A[p+i]

    for j in range(0,n2):
        R[j] = A[q+j+1]

    L[n1] = 99999
    R[n2] = 99999
    i = 0
    j = 0

    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

n = len(A)
MERGESORT(A,0,n-1)
print("Sorted Array : ", A)