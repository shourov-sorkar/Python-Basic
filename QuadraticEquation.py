import cmath  # import complex math module 

a = 1 #define the values 
b = 4
c = 5

dis = (b**2) - (4 * a*c) # calculate the discriminant

sol1 = (-b-cmath.sqrt(dis))/(2 * a) #find the results 
sol2 = (-b + cmath.sqrt(dis))/(2 * a) #find the results 

print('The roots are {0} and {1}'.format(sol1,sol2)) #printing the result 

