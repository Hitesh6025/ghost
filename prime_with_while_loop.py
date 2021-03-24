i=2
a=eval(input('enter a value :'))
while(i<a):
    if(a%i==0):
        print("the value is not prime ")
        break 
    i+=1    
else:
    print('the value is prime ')
