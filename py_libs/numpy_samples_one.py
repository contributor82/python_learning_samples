"""Array from numpy library samples"""""

import numpy as np
from numpy import ndarray, save


class NumpyUse:
    """NumpyUse class is used to demonstrate the use of numpy library"""
    name: str = ""

    def __init__(self) -> None:
        """Constructor of NumpyUse class"""
        self.name = "NumpyUse"

    def print_name(self) -> None:
        """Prints the name of the class"""
        print("Name is : ", self.name)

    def print_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the array"""
        print("Array is : ", arr.tolist())

    def print_array_shape(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the shape of the array"""
        print("Array shape is : ", arr.shape)

    def print_array_dimension(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the dimension of the array"""
        print("Array dimension is : ", arr.ndim)

    # type: ignore
    def print_array_expand_dimension(self,
                                     arr: ndarray[int]) -> None:     # type: ignore
        """Prints the array after expanding the dimension"""
        print("Array before expand dimension is : ", arr)  # type: ignore
        arr = np.expand_dims(arr, axis=0)  # type: ignore
        print("Array after expand dimension is : ", arr)  # type: ignore
        arr = arr.shape  # type: ignore
        print("Array after shape is : ", arr)  # type: ignore

    def print_array_size(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the size of the array"""
        print("Array size is : ", arr.size)

    def print_array_data_type(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the data type of the array"""
        print("Array data type is : ", arr.dtype)  # type: ignore

    def print_array_item_size(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the item size of the array"""
        print("Array item size is : ", arr.itemsize)

    def print_array_data(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the data of the array"""
        print("Array data is : ", arr.data)

    def print_array_flags(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the flags of the array"""
        print("Array flags is : ", arr.flags)

    def print_array_strides(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the strides of the array"""
        print("Array strides is : ", arr.strides)

    def print_array_transpose(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the transpose of the array"""
        print("Array transpose is : ", arr.transpose())  # type: ignore

    def print_array_flatten(self, arr: ndarray[int]) -> None:  # type: ignore
        """prints the flatten of the array"""
        print("Array flatten is : ", arr.flatten())  # type: ignore

    def print_array_reshape(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the reshape of the array"""
        print("Array before reshape is : ", arr)  # type: ignore
        arr = arr.reshape(2, 4)  # type: ignore
        print("Array after reshape is : ", arr)  # type: ignore

    def print_array_resize(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the resize of the array"""
        print("array before resize is : ", arr)  # type: ignore
        print("Array resize is : ", arr.resize(2, 4))
        print("Array after resize is : ", arr)  # type: ignore

    def print_array_append(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the append of the array"""
        print("Array before append is : ", arr)  # type: ignore
        arr = np.append(arr, [1, 2, 3, 4, 5, 6, 7, 8])  # type: ignore
        print("Array append is : ", arr)  # type: ignore
        print("Array after append is : ", arr)  # type: ignore

    def print_array_insert(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the insert of the array"""
        print("Array before insert is : ", arr)  # type: ignore
        arr = np.insert(arr, 2, [1, 2, 3, 4, 5, 6, 7, 8])  # type: ignore
        print("Array after insert is : ", arr)  # type: ignore

    def print_array_delete(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the delete of the array"""
        print("Array before delete is : ", arr)  # type: ignore
        print("Array delete is : ", np.delete(arr, 2))  # type: ignore
        print("Array after delete is : ", arr)  # type: ignore

    # type: ignore
    def print_array_concatenate(self,
                                arr1: ndarray[int], arr2: ndarray[int]) -> None:     # type: ignore
        """Prints the concatenate of the array"""
        print("Array 1 before concatenate is : ", arr1)  # type: ignore
        print("Array 2 before concatenate is : ", arr2)  # type: ignore
        arr = np.concatenate((arr1, arr2))  # type: ignore
        print("Array after concatenate is : ", arr)  # type: ignore

    def print_array_stack(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the stack of the array"""
        print("Array before stack is : ", arr)  # type: ignore
        arr = np.stack((arr, [1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
        print("Array stack is : ", arr)  # type: ignore
        print("Array after stack is : ", arr)  # type: ignore

    # def print_array_VStack(self, arr: np.ndarray):
    # type: ignore
    def print_expression_of_array(self,
                                  arr: ndarray[int]) -> None:     # type: ignore
        """Prints the expression of the array"""
        print("Array before expression is : ", arr)  # type: ignore
        print("Array expression is 0:3 : ", arr[0:3])  # type: ignore
        print("Array expression is arr < 5 : ", arr[arr < 5])  # type: ignore

    # type: ignore
    def print_array_divisible_by2(self,
                                  arr: ndarray[int]) -> None:     # type: ignore
        """Prints the array divisible by 2"""
        print("Array before expression is : ", arr)  # type: ignore
        arr = arr[arr % 2 == 0]  # type: ignore
        print("Array expression is arr % 2 == 0 : ", arr)  # type: ignore

    # type: ignore
    def print_array_using_logical_operator(self,
                                           arr: ndarray[int]) -> None:     # type: ignore
        """Prints the array using logical operator"""
        print("Array before expression is : ", arr)  # type: ignore
        arr = arr[(arr > 2) & (arr < 5)]  # type: ignore

        print("Array expression is arr[(arr > 2) & (arr < 5)] : ",
              arr)  # type: ignore

    def print_array_sort(self, arr: ndarray[int]) -> None:  # type: ignore
        """Prints the array after sorting"""
        print("Array before sorting : ", arr)  # type: ignore
        arr = np.sort(arr)  # type: ignore
        print("Array after sorting : ", arr)  # type: ignore

    def print_mean_square_error(self, n: int,
                                predictions: ndarray[int],      # type: ignore
                                labels: ndarray[int]) -> None:     # type: ignore
        """Prints the mean square error"""
        print("n value : ", n)
        print("predictions value : ", predictions)  # type: ignore
        print("labels value : ", labels)  # type: ignore
        print("Mean Square Error : ", np.sum(
            np.square(predictions - labels)) / n)  # type: ignore

    def save_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Saves the array in a file"""
        print("Array to save : ", arr)  # type: ignore
        save('C:\\Data\\numpy_array.npy', arr)  # type: ignore
        print("Array saved successfully")

    def load_array_from_file(self, file_name: str) -> None:
        """Loads the array from a file"""
        arr = np.load(file_name)  # type: ignore
        print("Array loaded successfully : ", arr)  # type: ignore

    def print_linear_space_array(self) -> None:
        """Prints the linear space array"""
        print("Array with linear space : ", np.linspace(0, 2, 9))


if __name__ == '__main__':
    numpy_use_instance = NumpyUse()

    numpy_use_instance.print_name()
    numpy_use_instance.print_array(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_shape(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_dimension(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore

    numpy_use_instance.print_array_size(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_data_type(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_item_size(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_data(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore

    numpy_use_instance.print_array_flags(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_strides(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_transpose(  # type: ignore
        np.array([[1, 2, 3, 4], [5, 6, 7, 8]]))  # type: ignore
    numpy_use_instance.print_array_flatten(  # type: ignore
        np.array([[1, 2, 3, 4], [5, 6, 7, 8]]))  # type: ignore

    numpy_use_instance.print_array_reshape(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_resize(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_expand_dimension(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore

    numpy_use_instance.print_array_append(  # type: ignore
        np.array([9, 10, 11, 12, 13, 14, 15, 16]))  # type: ignore
    numpy_use_instance.print_array_insert(  # type: ignore
        np.array([17, 18, 19, 20, 21, 22, 23, 24]))  # type: ignore
    numpy_use_instance.print_array_delete(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_concatenate(np.array(  # type: ignore
        [1, 2, 3, 4, 5, 6, 7, 8]), np.array([10, 11, 12, 13, 14, 15]))  # type: ignore
    numpy_use_instance.print_array_stack(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore

    numpy_use_instance.print_expression_of_array(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_divisible_by2(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_using_logical_operator(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.print_array_sort(  # type: ignore
        np.array([2, 1, 5, 3, 7, 4, 6, 8]))  # type: ignore

    numpy_use_instance.print_mean_square_error(3, np.array(  # type: ignore
        [1, 1, 1, 1, 1, 1, 1, 1]), np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.save_array(  # type: ignore
        np.array([1, 2, 3, 4, 5, 6, 7, 8]))  # type: ignore
    numpy_use_instance.load_array_from_file(
        'C:\\Data\\numpy_array.npy')  # type: ignore

    numpy_use_instance.print_linear_space_array()


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


# randomNubers = np.random.random((2,3))
# print("Array with random numbers : ", randomNubers)

# print("Array before argsort : ", arr)
# arr = np.argsort(arr)
# print("Array after argsort : ", arr)
