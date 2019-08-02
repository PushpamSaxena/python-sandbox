import sys

num1 = [2, 9, 3, 12, 8, 15, 4, 68, 7, 5, 1, 35, 70, 6]
key = 7

def binarySearch(arr, x):
  
  #print (int(len(arr)/2))
  
  ##check if array is empty
  if (len(arr) == 0):
    print ("ERROR: The KEY is not present in the array!!!!")
    sys.exit()

  else:
    ## Check if middle value is greater
    print ("Current array under search is ",arr)
    if (x == arr[int(len(arr)/2)]):
      return int(len(arr)/2)
    
    elif (x < arr[int(len(arr)/2)]):
      print ("The key to search is: ", x, " and it is less than the middle number ", arr[int(len(arr)/2)])
      #print (arr[0:int(len(arr)/2)])
      return (binarySearch(arr[0:int(len(arr)/2)], x))
    
    else:
      print ("The key to search is: ", x, " and it is greater than the middle number ", arr[int(len(arr)/2)])	
      #print (arr[int(len(arr)/2)+1:len(arr)])
      return (binarySearch(arr[int(len(arr)/2)+1:len(arr)], x) + (int(len(arr)/2)+1))

## remove duplicates
num1 = list(dict.fromkeys(num1))

## sort the array in ascending order
num1.sort()
#print ("Sorted array is: ", num1)

result = binarySearch(num1, key)
print ("Key ", key, " is at position ", result+1, " in the array.")