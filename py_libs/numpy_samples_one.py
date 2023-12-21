"""Array from numpy library samples"""""

import numpy as np
from numpy import ndarray

class NumpyUse:
    """NumpyUse class is used to demonstrate the use of numpy library"""

    def __init__(self) -> None:
        self.name = "NumpyUse"

    def print_name(self) -> None:
        print("Name is : ", self.name)

    def print_array(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array is : ", arr.tolist())

    def print_array_shape(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array shape is : ", arr.shape)

    def print_array_dimension(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array dimension is : ", arr.ndim)

    def print_array_expand_dimension(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expand dimension is : ", arr) # type: ignore
        arr = np.expand_dims(arr, axis=0) # type: ignore
        print("Array after expand dimension is : ",arr) # type: ignore
        arr = arr.shape # type: ignore
        print("Array after shape is : ",arr) # type: ignore

    def print_array_size(self, arr: ndarray[int]) -> None:# type: ignore
        print("Array size is : ", arr.size)

    def print_array_data_type(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array data type is : ", arr.dtype) # type: ignore

    def print_array_item_size(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array item size is : ", arr.itemsize)

    def print_array_data(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array data is : ", arr.data)

    def print_array_flags(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array flags is : ", arr.flags)

    def print_array_strides(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array strides is : ", arr.strides)

    def print_array_transpose(self, arr: ndarray[int]) -> None:  # type: ignore
        print("Array transpose is : ", arr.transpose()) # type: ignore

    def print_array_flatten(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array flatten is : ", arr.flatten()) # type: ignore

    def print_array_reshape(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before reshape is : ", arr) # type: ignore
        arr = arr.reshape(2,4) # type: ignore
        print("Array after reshape is : ", arr) # type: ignore

    def print_array_resize(self, arr: ndarray[int]) -> None: # type: ignore
        print("array before resize is : ", arr) # type: ignore
        print("Array resize is : ", arr.resize(2,4))
        print("Array after resize is : ", arr) # type: ignore

    def print_array_append(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before append is : ", arr) # type: ignore
        arr = np.append(arr, [1,2,3,4,5,6,7,8]) # type: ignore
        print("Array append is : ", arr) # type: ignore
        print("Array after append is : ", arr) # type: ignore

    def print_array_insert(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before insert is : ", arr) # type: ignore
        arr = np.insert(arr, 2, [1,2,3,4,5,6,7,8]) # type: ignore
        print("Array after insert is : ", arr) # type: ignore

    def print_array_delete(self, arr: ndarray[int]) -> None:# type: ignore
        print("Array before delete is : ", arr) # type: ignore
        print("Array delete is : ", np.delete(arr, 2)) # type: ignore
        print("Array after delete is : ", arr) # type: ignore

    def print_array_concatenate(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before concatenate is : ", arr) # type: ignore
        arr = np.concatenate((arr, [1,2,3,4,5,6,7,8])) # type: ignore
        print("Array concatenate is : ", arr) # type: ignore
        print("Array after concatenate is : ", arr) # type: ignore

    def print_array_stack(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before stack is : ", arr) # type: ignore
        arr = np.stack((arr, [1,2,3,4,5,6,7,8])) # type: ignore
        print("Array stack is : ", arr) # type: ignore
        print("Array after stack is : ", arr) # type: ignore

    # def print_array_VStack(self, arr: np.ndarray):
    def print_expression_of_array(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expression is : ", arr) # type: ignore
        print("Array expression is 0:3 : ", arr[0:3]) # type: ignore
        print("Array expression is arr < 5 : ", arr[arr < 5]) # type: ignore

    def print_array_divisible_by2(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expression is : ", arr) # type: ignore
        arr = arr[arr % 2 == 0] # type: ignore
        print("Array expression is arr % 2 == 0 : ", arr) # type: ignore

    def print_array_using_logical_operator(self, arr: ndarray[int]) -> None: # type: ignore
        print("Array before expression is : ", arr) # type: ignore
        arr = arr[(arr > 2) & (arr < 5)] # type: ignore
        print("Array expression is arr[(arr > 2) & (arr < 5)] : ", arr) # type: ignore

if __name__ == '__main__':
    numpy_use_instance = NumpyUse()

    numpy_use_instance.print_name()
    numpy_use_instance.print_array(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_shape(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_dimension(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.print_array_size(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_data_type(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_item_size(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_data(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.print_array_flags(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_strides(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_transpose(np.array([[1,2,3,4],[5,6,7,8]])) # type: ignore
    numpy_use_instance.print_array_flatten(np.array([[1,2,3,4],[5,6,7,8]])) # type: ignore

    numpy_use_instance.print_array_reshape(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_resize(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_expand_dimension(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.print_array_append(np.array([9,10,11,12,13,14,15,16])) # type: ignore
    numpy_use_instance.print_array_insert(np.array([17,18,19,20,21,22,23,24])) # type: ignore
    numpy_use_instance.print_array_delete(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_concatenate(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_stack(np.array([1,2,3,4,5,6,7,8])) # type: ignore

    numpy_use_instance.print_expression_of_array(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_divisible_by2(np.array([1,2,3,4,5,6,7,8])) # type: ignore
    numpy_use_instance.print_array_using_logical_operator(np.array([1,2,3,4,5,6,7,8])) # type: ignore



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
