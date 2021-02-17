year = int(input("Enter the Year: ")) # take input from user 

if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("This is Leap Year")
        else:
            print("This is Not Leap Year")
    else:
        print("This is not Leap Year")
else:
    print("This is not Leap Year")
