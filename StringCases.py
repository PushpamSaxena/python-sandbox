inputStr=input("Enter String: ")
updatedStr = inputStr

if inputStr.isupper():
    print ("The input string has all characters in upper case.")
else:
    print ("Converting the input string to have all characters in upper case.")
    updatedStr = inputStr.upper()

print (updatedStr)