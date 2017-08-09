a=input("Enter the Year\n")
b=a
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            a=1
        else:
            a=0
    else:
        a=1
else:
    a=0
if (a==1):
    print( str(b) + " is Leap Year")
else:
    print( str(b) + " is not a Leap")
