inputStr="We want to Find Out the NUMBER of characters which are in Upper case and the NUMBER of characters in LOWER Case"
upperCaseChars = []
lowerCaseChars = []
otherChars = []

for a in inputStr:
	if (a.isupper()):
		upperCaseChars.append(a)

	elif (a.islower()):
		lowerCaseChars.append(a)

	else:
		otherChars.append(a)

print ("Number of characters in Upper Case are: ", len(upperCaseChars))
print ("Number of characters in Lower Case are: ", len(lowerCaseChars))
print ("Number of other characters in the string are: ", len(otherChars))