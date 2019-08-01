num1 = [3, 3, 5, 8, 1]
num2 = [3, 5, 7, 9]
intersection = []

for eachNum1 in num1:
  #print ("The current number in num1 is: ", eachNum1)
  
  for eachNum2 in num2:
    #print ("The current number in num2 is: ", eachNum2)
	
    if (eachNum1 == eachNum2):
      #print ("Matching number found: ", eachNum1)
      intersection.append(eachNum1)

print (intersection)
intersection = list(dict.fromkeys(intersection))
print (intersection)