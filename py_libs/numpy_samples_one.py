import numpy as np

a = np.arange(15)
print("Array for the specified limit: ", a)
a2 = a[np.newaxis,:]
print(a2.shape)

# a[2] = "hello"
# print(a)

a3 = np.array([1,2,3,4,5])
print("Default array creation using numpy: ", a3)

print("Array filled with 0s : ", np.zeros((3,4)))

print("Array filled with 1s : ", np.ones((3,4)))

print("create an array with emptys : ", np.empty((2)))

print("Array with linear space : ", np.linspace(0,2,9))

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print("Array before sorting : ", arr)
arr = np.sort(arr)
print("Array after sorting : ", arr)


