ch=65
n=eval(input("enter the no. of line you wanna print "))
for i in range (0,n):
	for i in range (0,i+1):	
		print(chr(ch),end=' ')
		ch+=1
	print()
