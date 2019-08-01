num1 = [2, 9, 3, 8, 4, 7, 5, 1]
key = 3

def binarySearch(arr, x):
  
  ##check if array is empty

    ## Check if middle value is greater
    #return int(len(arr)/2)
    if (x == arr[int(len(arr)/2)]):
      return int(len(arr)/2)
    
    elif (x < arr[int(len(arr)/2)]):
      print (x, " is less than ", arr[int(len(arr)/2)])
    
    #else if (x > arr[int(len(arr)/2)]):
    else:
      print (x, " is greater than ", arr[int(len(arr)/2)])	


## remove duplicates
num1 = list(dict.fromkeys(num1))

## sort the array in ascending order
num1.sort()
print ("Sorter array is: ", num1)

result = binarySearch(num1, key)

print ("Key ", key, " is at position ", int(result)+1, " in the array.")