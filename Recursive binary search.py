list=[1,2,3,4,5,6,7,8]
target=-3

def Recursive_binary_search(list,target):
"""
Returns true if the target exists and false none if it dose not.
"""
    if len(list)==0: #When the list is empty 
        return None
    else:
        mid=len(list)//2 #Middle index in array
        if list[mid] == target: #If the target is in the middle
            return True
        else:
            if list[mid]>target: #If the target is in the left half of the array
                return Recursive_binary_search(list[:mid],target)
            else: #If the target is in the right half of the array
                return Recursive_binary_search(list[mid+1:],target)




print(Recursive_binary_search(list,target))
