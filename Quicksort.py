#Time Complexity O(N LogN)

def quicksort(nums): #recurisive sorting method
    if len(nums)<=1: #incase the list is null or a single digit
        return nums
    less_then_pivot=[] #splits from main list into less then pivot list 
    greater_then_pivot=[] #splits from main list into greater then pivot list 
    pivot=nums[0] #the pivot
    for nums in nums[1:]: #runs all the number sequentally from index 1 till end
        if nums <= pivot: #when the number is less then pivot
            less_then_pivot.append(nums)
        else: #When its greater then the pivot
            greater_then_pivot.append(nums)
    return quicksort(less_then_pivot)+[pivot]+quicksort(greater_then_pivot) #returns the sorted list after sorting each list and adding them together in the correct order

print(quicksort([9,3,1,52,1,5,2,9,1]))
