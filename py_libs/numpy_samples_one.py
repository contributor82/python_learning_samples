"""Array from numpy library samples"""""

import numpy as np
from numpy import ndarray

class NumpyUse:
    """NumpyUse class is used to demonstrate the use of numpy library"""

    def __init__(self) -> None:
        self.name = "NumpyUse"

    def printName(self) -> None:
        print("Name is : ", self.name)

    def printArray(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array is : ", arr.tolist())

    def printArrayShape(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array shape is : ", arr.shape)

    def printArrayDimension(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array dimension is : ", arr.ndim)

    def printArrayExpandDimension(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expand dimension is : ", arr) # type: ignore
        arr = np.expand_dims(arr, axis=0) # type: ignore
        print("Array after expand dimension is : ",arr) # type: ignore
        arr = arr.shape # type: ignore
        print("Array after shape is : ",arr) # type: ignore

    def printArraySize(self, arr: ndarray[int]) -> None:# type: ignore
        print("Array size is : ", arr.size)

    def printArrayDataType(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array data type is : ", arr.dtype)

    def printArrayItemSize(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array item size is : ", arr.itemsize)

    def printArrayData(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array data is : ", arr.data)

    def printArrayFlags(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array flags is : ", arr.flags)

    def printArrayStrides(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array strides is : ", arr.strides)

    def printArrayTranspose(self, arr: ndarray[int]) -> None:  # type: ignore
        print("Array transpose is : ", arr.transpose())

    def printArrayFlatten(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array flatten is : ", arr.flatten())

    def printArrayReshape(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before reshape is : ", arr)
        arr = arr.reshape(2,4)
        print("Array after reshape is : ", arr)

    def printArrayResize(self, arr: ndarray[int]) -> None: # type: ignore
        print("array before resize is : ", arr)
        print("Array resize is : ", arr.resize(2,4))
        print("Array after resize is : ", arr)

    def printArrayAppend(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before append is : ", arr)
        arr = np.append(arr, [1,2,3,4,5,6,7,8])
        print("Array append is : ", arr)
        print("Array after append is : ", arr)

    def printArrayInsert(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before insert is : ", arr)
        arr = np.insert(arr, 2, [1,2,3,4,5,6,7,8])
        print("Array after insert is : ", arr)

    def printArrayDelete(self, arr: ndarray[int]) -> None:# type: ignore
        print("Array before delete is : ", arr)
        print("Array delete is : ", np.delete(arr, 2))
        print("Array after delete is : ", arr)

    def printArrayConcatenate(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before concatenate is : ", arr)
        arr = np.concatenate((arr, [1,2,3,4,5,6,7,8]))
        print("Array concatenate is : ", arr)
        print("Array after concatenate is : ", arr)

    def printArrayStack(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before stack is : ", arr)
        arr = np.stack((arr, [1,2,3,4,5,6,7,8]))
        print("Array stack is : ", arr)
        print("Array after stack is : ", arr)

    # def printArrayVStack(self, arr: np.ndarray):
    def printExpressionOfArray(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expression is : ", arr)
        print("Array expression is 0:3 : ", arr[0:3])
        print("Array expression is arr < 5 : ", arr[arr < 5])

    def printArrayDivisibleBy2(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expression is : ", arr)
        arr = arr[arr % 2 == 0]
        print("Array expression is arr % 2 == 0 : ", arr)

    def printArrayUsingLogicalOperator(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expression is : ", arr)
        arr = arr[(arr > 2) & (arr < 5)]
        print("Array expression is arr[(arr > 2) & (arr < 5)] : ", arr)

if __name__ == '__main__':
    numpy_use_instance = NumpyUse()

    numpy_use_instance.printName()
    numpy_use_instance.printArray(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayShape(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayDimension(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.printArraySize(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayDataType(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayItemSize(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayData(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.printArrayFlags(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayStrides(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayTranspose(np.array([[1,2,3,4],[5,6,7,8]])) # type: ignore
    numpy_use_instance.printArrayFlatten(np.array([[1,2,3,4],[5,6,7,8]])) # type: ignore

    numpy_use_instance.printArrayReshape(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayResize(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayExpandDimension(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.printArrayAppend(np.array([9,10,11,12,13,14,15,16])) # type: ignore
    numpy_use_instance.printArrayInsert(np.array([17,18,19,20,21,22,23,24])) # type: ignore
    numpy_use_instance.printArrayDelete(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayConcatenate(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayStack(np.array([1,2,3,4,5,6,7,8])) # type: ignore


    numpy_use_instance.printExpressionOfArray(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayDivisibleBy2(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.printArrayUsingLogicalOperator(np.array([1,2,3,4,5,6,7,8])) # type: ignore



# a = np.arange(15)
# print("Array for the specified limit using arange: ", a)
# a2 = a[np.newaxis,:]
# print(a2.shape)
# a = np.arange(2,9,2)
# print("Array for the specified limit using arange: ", a)

# # a[2] = "hello"
# # print(a)

# a3 = np.array([1,2,3,4,5])
# print("Default array creation using numpy: ", a3)

# print("Array filled with 0s : ", np.zeros((3,4)))

# print("Array filled with 1s : ", np.ones((3,4)))

# print("create an array with emptys : ", np.empty((2)))

# print("Array with linear space : ", np.linspace(0,2,9))

# arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# print("Array before sorting : ", arr)

# arr = np.sort(arr)
# print("Array after sorting : ", arr)

# randomNubers = np.random.random((2,3))
# print("Array with random numbers : ", randomNubers)

# print("Array before argsort : ", arr)
# arr = np.argsort(arr)
# print("Array after argsort : ", arr)
