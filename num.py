import numpy as np

#using numpy to declare an array of elements
arr = np.array([1,2,3,4,5])
print(arr)

#adding two elements from your array elements
arr = np.array((1,2,3,4,5,5,6))
print(arr[1] + arr[5])


#slicing elements from your array(start:end)
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

arr = np.array([1,2,3,4,5,6,7])
print(arr[:5])

arr = np.array([1,2,3,4,5,6,7])
print(arr[5:])
print(arr[1:7:2])

arr1 = np.array([1,2,4,5,6] , dtype='S')
print(arr1)
print(arr1.dtype)

arr2 = np.rray(["apple","banana", "orange"])
print(arr2.dtype)

lst = np.array([1,2,3,4])
a = np.asarray(lst, copy=True)

print(a)
a[0] = 0
print(lst)


c = np.array([0.0,0.1,0.2,0.3,0.4,0.5])
print(c[0])

print(c[[0, 2]])

c[[0,1]] = [[0,0.3]]
print(c)

print(c[-5])
print(c[::1])