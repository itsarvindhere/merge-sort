# PROBLEM STATEMENT

Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

# EXAMPLE

    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

# MERGE SORT APPROACH

This is similar to the "Inversion Count" Problem. 

Here, we used Merge Sort becaue in Merge Sort, we first split the given list into sublists till each sublist has only one element. Then, we Merge these sorted sublists together and during Merging, we will check whether left subarray element is smaller or greater than right subarray element. If it is equal or smaller, then we pick the left element to put in our final array. Otherwise, we will pick the right subarray element as that is smaller.

In this problem, we want to find how many elements are smaller to the "right" side of an element. So, we just need to tweak the Merge Sort a bit such that, if at any time, an element on left is bigger than an element on right, we increment the count of smaller elements. It is also possible that there are more elements in the right subarray that are smaller than left element. So while that is the case, we will keep incrementing the count.

But, as soon as the left element becomes <= right element, we know that we cannot find any more smaller elements than this left element on its right. At that moment, we will simply take the original index of this "left" element and at the "index" position in the output, we will add the count. 

As we know, in Merging process, either left or right subarray has some elements that are not added to final sorted array. So, if the left subarray has some elements that were not yet put in the final sorted array, what does that mean? That simply means, all the elements in the left subarray are bigger than the right subarray. So we can simply append the length of right subarray that is, all elements of right subarray are smaller than all the elements in left subarray.

Let's understand with an example.

	nums = [5,2,6,1]
	
	Before merge sort, we also want to ensure we do not lose track of the indices. 
	
	So, convert each number into a pair (index, number)
	
	nums = [(0,5), (1,2), (2,6), (3,1)]
	
	First, we split it from mid. we get two subarrays [(0,5), (1,2)] and [(2,6), (3,1)]
	
	****************************************************************************
	First, recursive call gets made on [(0,5), (1,2)]
	
	It is further split into L = [(0,5)] and R = [(1,2)]
	
	Now, recursive call is made on [(0,5)]. Since length is < 2, we return.
	Same with [(1,2)]
	
	And now, we call the merge() method, passing [(0,5)] and [(1,2)] as L and R.
	
	In Merge, i = 0, j = 0, k = 0
	
	We see that at ith index in L, we have "5" and at jth index in R, we have 2.
	
	Since 5 > 2, it means, we got one element that is smaller than "5". So we increment the count.
	
	We put "2" in the sorted array and Now j became 1 and we come out of the loop.
	
	Since there is still "5" in left subarray, it simply means it is bigger than all elements in the right sublist.
	
	So, for this reason, for "5", the number of smaller elements is incremented by whatever length the right sublist has.
	
	Do note that we are not doing = len(right). We are doing += len(right) because when we come back to merge() method next time,
	It is possible that there are more elements smaller than "5".
	
	Hence, after sorting, L = [(1,2), (0,5)]. 
	
	Output array so far [1,0,0,0]
	
	****************************************************************************
	Now, the second recursive call is made on [(2,6), (3,1)]
	
	It is split into L = [(2,6)] and R = [(3,1)]
	
	When we come in Merge() method, then again the same situation as above.
	
	Since "6" is bigger than "1", it means, we got one smaller element than "6". So count += 1.
	
	And loop will terminate since j became 1. 
	
	And since we still have "6" in the left subarray, we do the same as we did for "5".
	
	That is, it is bigger than all elements in right sublist so number of elements smaller than it right now = length of right sublist. 
	
	So, we add this number to whatever we have already for "6".
	
	Hence, after sorting, R = [(3,1), (2,6)]. 
	
	Output array so far [1,0,1,0]
	
	****************************************************************************
	
	Now that these two parts are sorted, we will call merge() again. 
	
	This time, L = [(1,2), (0,5)] and R = [(3,1), (2,6)]
	
	i = 0, j = 0
	
	we see that at i, we have "2" and at j we have "1'. Since 2 > 1, we increment the count by 1. Count = 1.
	
	i = 0, j = 1
	
	At "i", we still have "2", but at "j", we now have "6". Since 2 is not greater than "6", it means, no more elements are smaller than 2.
	
	Hence, we simply add the count at the index of 2 in output array. Output array so far [1,1,1,0]
	
	i = 1, j = 1
	
	we see that at i, we have "5" and at j we have "6'. Since 5 is not smaller than 6, it means, no element after "6" can be smaller than 5 as well.
	
	So, we simply add the count so far at the index of "5". 
	
	Do note that "5" already had "1' smaller element and now, when we add count = 1, then number of elements smaller than "5" become 2.
	
	And it makes sense because since "1" was smaller than "2", then "1" is also smaller than whatever element is greater than "2" in left subarray.
	
	And finally, the output array will become [2,1,1,0]
