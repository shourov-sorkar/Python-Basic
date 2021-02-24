import array as arr # importing the array 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # intial the array items 
my_array = arr.array('i', my_list)

print(my_array[2:5]) # 3rd to 5th
print(my_array[:-3]) # beginning to 4th
print(my_array[7:])  # 8th to end
print(my_array[:])   # beginning to end