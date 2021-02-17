a = input("Enter the value of X: ") # take input from user
b = input("Enter the value of Y: ") # take input from user 

temp = a #take the temporary variable 
a = b
b = temp 

print('The value of x after swapping: {}'.format(a)) #print the results 

print('The value of y after swapping: {}'.format(b))