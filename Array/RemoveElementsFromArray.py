import array as arr # importing array 

a = arr.array('i', [1, 2, 3, 1, 5])   # creating a array 


print ("The new created array is : ", end ="")  # printing original array 
for i in range (0, 5): 
    print (a[i], end =" ") 
  
print ("\r") 

print ("The popped element is : ", end ="") 
print (a.pop(2))  # remove element in index number 2 from the array 

print ("The array after popping is : ", end ="")  # printing array after poping 
for i in range (0, 4): 
    print (a[i], end =" ") 
  
print("\r") 