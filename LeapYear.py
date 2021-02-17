year = int(input("Enter the Year: ")) # take input from user 

if(year % 4) == 0: #condition year is divisible by 4 or not 
    if(year % 100) == 0: #condition year is divisible by 100 or not 
        if(year % 400) == 0:  #condition year is divisible by 400 or not 
            print("{0} is Leap Year".format(year)) #print when condition is true 
        #print when condition is false 
        else:
            print("{0} is Not Leap Year".format(year)) 
    else: 
        print("{0} is not Leap Year".format(year))
else:
    print("{0} is not Leap Year".format(year)) 
