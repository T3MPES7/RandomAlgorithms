#O(KnLog n) Time Complexity
#Linear Space Complexity

def Merge_sort(nums):
    """Through recursion continusaly splits the array into two groups,
      left and right, until there is a single element per array in a group of arrays"""
    
    if len(nums)<=1: #In case its empty or has a single element 
        return nums
    
    left,right=split(nums) #splist the array into two
    left=Merge_sort(left) #Splits the left and right side continuasly until each elemnet is a seperate array 
    right=Merge_sort(right)

    return merge(left,right) #returns the merged result after sorting
     
def split(nums):
    """Splits the array into halves each time its called, takes overall a O(K Log n) Time complexity
    """
    mid=len(nums)//2 #Finds the middle index
    left=nums[:mid] #ignores the right half of the nums arrary and goes from middle till the end
    right=nums[mid:]#ignored the left half of the nums array and goes from middle till the start
    return left,right
        

def merge(left,right):
    """Merges the two splitted arrays into a single sorted array, Runs at O(n) time complexity"""
    li=[] #New sorted list
    i,j=0,0 #Count keepers

    while i<len(left) and j<len(right): #Runs continuasly until the count is more then the length
        if left[i]<right[j]: #when the lefts arrays index "i" element is smaller then the right arrays index "j" element
            li.append(left[i]) #Appends the smaller result 
            i+=1 #Index i increases
        else:
            li.append(right[j]) #Appends the index "j"'s element as its smaller 
            j+=1
    while i<len(left): #Incase there's a odd number of elements after the splitting where there are elements left out
        li.append(left[i]) 
        i+=1
    while j<len(right): 
        li.append(right[j])
        j+=1
    return li #Returns the appended list




nums=[7,9,6,46,3,3,1,2]
result=Merge_sort(nums)
print(result)
