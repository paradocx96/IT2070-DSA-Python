####################################
# NOT FINISHED YET #################
####################################

A=[]
for x in range(5):
    A.append(int(input("Enter a Number : ")))
print("Original Array : ", A)

def MAX_HEAPIFY(A,i):
    l = 2 * i
    r = 2 * i + 1

    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        MAX_HEAPIFY(A,largest)

def BUILD_MAX_HEAP(A):
    heap_size = len(A)
    for i in range (len(A)//2,1,-1):
        MAX_HEAPIFY(A,i)


n = len(A)
def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    for i in range(n,2,-1):
        A[1],A[i] = A[i],A[1]
        heap_size = heap_size - 1
        MAX_HEAPIFY(A,1)


HEAPSORT(A)
print(A)