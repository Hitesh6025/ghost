a=eval(input("enter the value"))
for i in range (2,a):
    if a%i==0:
        print("the value you have entered is not prime ")
        break
else :
    print("the value you have entered is prime ")

