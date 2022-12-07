class Solution:
    
    # Merge two Sorted arrays
    def merge(self, L, R, A, output):
        nL,nR = len(L), len(R)
        
        i,j,k = 0,0,0
        
        count = 0
        
        while i < nL and j < nR:
            # If element in left array is smaller than right element
            # That means, it is smaller than all the other elements in right
            # So, for this element, the number of elements smaller than it = "count"
            if L[i][1] <= R[j][1]:
                output[L[i][0]] += count
                A[k] = L[i]
                i += 1
            # If element in left array is greater than right, then it means, there is one smaller element than left element
            # But since there can be more elements on right array that are smaller than left element, we will keep incrementing count accordingly
            else: 
                count += 1
                A[k] = R[j]
                j += 1
            k += 1
            
        # If any of the two halves have some elements left
        
        # If left half has elements left, it just means these elements are bigger than all the elements in Right subarray
        while i < nL:
            output[L[i][0]] += len(R)
            A[k] = L[i]
            i += 1
            k += 1
            
        while j < nR:
            A[k] = R[j]
            j += 1
            k += 1
        
    
    # Merge Sort
    def mergeSort(self, A, output):
        N = len(A)
        
        # Base Case
        if N < 2: return
        
        # Split into two halves
        mid = N // 2
        L, R = A[:mid], A[mid:]
        
        # Recursive call to sort these two halves
        self.mergeSort(L, output)
        self.mergeSort(R, output)
        
        # Merge the two sorted halves
        self.merge(L, R, A, output)
    
    
    def countSmaller(self, nums):
        output = [0] * len(nums)
        
        # We want to count elements smaller on the right of each index
        # SO we also want to not lose track of original indexes
        nums = [(i, num) for i,num in enumerate(nums)]
        
        self.mergeSort(nums,output)

        return output



solution = Solution()

print("Output -> ",solution.countSmaller([5,2,6,1]))
