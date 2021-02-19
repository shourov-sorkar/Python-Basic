num = int(input("Enter the number: ")) #take the input from user 

temp = num # set the temporary value 
rev = 0    # rev intial value is 0

while(num > 0):   # when input value is grater than 0
    dig = num % 10
    rev = rev * 10 + dig
    num = num//10
if(temp == rev): # check the rev value and dig value is same or not 
    print("This is palindrome number") # if condition is true 
else:
    print("This is not palindrome number") #if condition is false 
