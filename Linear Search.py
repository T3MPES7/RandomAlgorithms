#Linear Search using Python

def LinearSearch(arry, target):
    
    for i in range(0, len(arry)):   #Runs sequanlty through the array 
        if (arry[i] == target):     #Once the target is found the function ends
            return 1
     
    return 0      #incase the element isn't in the array


arry = [1,3,5,2,4,8,5,3,34,656,342,1,32,45,123] 
target=32 

if (LinearSearch(arry,target)==1): 
    print("Element", target, " Has been found!")
else:
    print("No such element exists")
