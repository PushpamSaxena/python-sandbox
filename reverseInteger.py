
n=int(input("Enter number: "))
rev=0
flag=0

##For negative numbers
if (n<0) :
	flag=1
	n=n*-1

##Separate the quotient and the remainder
while(n>0):
	remainder=n%10
	print ("remainer is: ", remainder)
	rev=rev*10+remainder
	n=n//10
	print ("The quotient is: ", n)

if flag:
	print("Reverse of the number:",rev*-1)
else:
	print("Reverse of the number:",rev)