import array as arr # import array 

a = arr.array('i', [1, 2, 3])  # array element 
  
  
print ("Array before insertion : ", end =" ")   
for i in range (0, 3): 
    print (a[i], end =" ") 
print() 
  

a.append(4)  # inserting number in array 
  
print ("Array after insertion : ", end =" ") 
for i in (a):  
    print (i, end =" ") 
print() 