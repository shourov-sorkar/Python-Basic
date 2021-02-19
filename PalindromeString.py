myString = input("Enter the string : ") # take input from user 

myString = myString.casefold()  # caseless comparision 

revString = reversed(myString) # reverse the string 

if list(myString) == list(revString): # check input string and receive string is same or not 
    print("This is palindrome")     #  if condition is true 
else:
    print("This is  not palindrome") # if condition is false 
