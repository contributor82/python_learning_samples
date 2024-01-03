"""Matplotlib samples one."""

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from mpl_toolkits.mplot3d import Axes3D  # Import the necessary module


class MatplotlibUse:
    """MatplotlibUse class is used to demonstrate the use of matplotlib library"""
    name: str = ""

    def __init__(self) -> None:
        """Constructor of MatplotlibUse class"""
        self.name = "MatplotlibUse"

    def print_name(self) -> None:
        """Prints the name of the class"""
        print("Name is : ", self.name)

    def plot_graph(self, arr: ndarray[int]) -> None:  # type: ignore
        """Plots a graph using matplotlib"""
        plt.plot(arr)  # type: ignore
        plt.ylabel('y axis numbers')  # type: ignore
        plt.xlabel('x axis numbers')  # type: ignore
        plt.show()  # type: ignore

    def plot_1D_array(self) -> None:
        """Plots a 1D array using matplotlib"""
        x = np.linspace(0, 5, 20)
        y = np.linspace(0, 10, 20)
        plt.plot(x, y, 'purple')  # type: ignore
        plt.plot(x, y, 'o')  # type: ignore
        plt.show()  # type: ignore

    def plot_surface_graph(self) -> None:
        """Plots a surface using matplotlib"""
        fig = plt.figure()
        # Fix the type hint for the ax variable
        ax: Axes3D = fig.add_subplot(projection='3d')
        x = np.arange(-5, 5, 0.15)
        y = np.arange(-5, 5, 0.15)
        x, y = np.meshgrid(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        z = np.sin(r)
        ax.plot_surface(x, y, z, rstride=1, cstride=1,
                        cmap='viridis')  # type: ignore


if __name__ == '__main__':
    print("MatplotlibUse class is being run directly")
    matplotlib_use_instance = MatplotlibUse()
   # matplotlib_use_instance.plot_graph([1, 2, 3, 4, 5])  # type: ignore
   # matplotlib_use_instance.plot_1D_array()  # type: ignore
    matplotlib_use_instance.plot_surface_graph()  # type: ignore
