A = []
for x in range(5):
    A.append(int(input("Enter a Number : ")))
print("Original Array : ", A)

def MERGESORT(A,l,r):
    if l < r:
        q = (l + r) // 2
        MERGESORT(A,l,q)
        MERGESORT(A,q+1,r)
        MERGE(A,l,q,r)

def MERGE(A,l,q,r):
    i = 1
    j = q + 1
    k = 0
    TEMP = []
    for y in range(r+1):
        TEMP.append(0)

    while(i <= q and j <= r):
        k = k + 1
        if A[i] <= A[j]:
            TEMP[k] = A[i]
            i = i + 1
        else:
            TEMP[k] = A[j]
            j = j + 1

    if j > r:
        for t in range(0,q-i):
            A[r-t] = A[q-t]

    for t in range(0,k):
        A[l+t] = TEMP[t+1]

n = len(A)
MERGESORT(A,0,n-1)
print("Sorted Array : ", A)