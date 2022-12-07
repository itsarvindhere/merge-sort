# Method to Merge two Sorted Arrays
def merge(L,R,A):
    nL = len(L)
    nR = len(R)

    i,j,k = 0,0,0

    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else: 
            A[k] = R[j]
            j += 1
        k += 1

    # Here, either left half will have some elements left
    # Or the right half will have some elements left

    # If left half has some elements left
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1

    # If right half has some elements left
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1


# Merge Sort Method
def mergeSort(A):
    N = len(A)

    # Base Case
    if N < 2: return

    # Split into two halves
    mid = N // 2
    L = [0] * mid
    R = [0] * (N - mid)

    # Fill the two halves
    for i in range(mid): L[i] = A[i]
    for i in range(mid, N): R[i - mid] = A[i]

    # Make a recursive call to sort Left and Right half separately
    mergeSort(L)
    mergeSort(R)

    # Now that both are sorted, merge them
    merge(L,R,A)

A = [2,4,1,6,8,5,3,7]

# Apply Merge Sort
mergeSort(A)

print("After Sorting -> ", A)
