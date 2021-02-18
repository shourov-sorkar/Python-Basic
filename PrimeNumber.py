num = int(input("Enter the Number: ")) #take input from user 

if(num>1): # check impur number is greater than 1 or not 
    for i in range(2, num):  # execute for loop 
        if(num % i) == 0:
            print(num, "is not prime number")
            break
    else:
        print(num, "is prime number")
else:
    print(num, "is not prime number")

