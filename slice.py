#1 basic slice 
arr = [10, "10", "20", "30", "40", "50"] 
print(arr[1:4])
print(arr[:3])
print(arr[3:]) 
print(arr[:]) 

#2 slice with step
arr = [10, "10", "20", "30", "40", "50"] 
print(arr[::2])
print(arr[1::2])
print(arr[::3]) 

#3 negative
arr = [10, "10", "20", "30", "40", "50"] 
print(arr[-4:-1])
print(arr[-1::-2])
print(arr[::-3])

#4 reverse slicing
arr= ('i', [1, 2, 3, 4])
print(arr [::-1])

#5 modify slicing
array = [1, 2, 3, 4, 5]
array[1:4] = [20, 30, 40]
print(array)