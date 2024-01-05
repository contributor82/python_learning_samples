"""Module for pandas samples."""
import numpy as np
from numpy import ndarray
import pandas as pd


class PandasUse:
    """Pandas use class."""

    def print_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print array."""
        print(arr)  # type: ignore

    def print_dataframe(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print dataframe."""
        df = pd.DataFrame(arr)
        print(df)

    def create_dataframe(self) -> None:  # type: ignore
        """Create dataframe."""
        df = pd.DataFrame({'Name': ['Harris', 'Henry', 'Elizabeth'],
                           'Age': [22, 35, 58],
                           'Sex': ['male', 'male', 'female']})
        print(df)
        print(df['Age'])  # type: ignore

    def create_series_from_scratch(self) -> None:  # type: ignore
        """Create series from scratch."""
        ages = pd.Series([22, 35, 58], name="Age")
        print(ages)
        print("Ages max is ", ages.max())  # type: ignore
        print("Ages min is ", ages.min())
        print("Ages mean is ", ages.mean())
        print("Ages median is ", ages.median())
        print("Ages mode is ", ages.mode())
        print("Ages std is ", ages.std())
        # works on numerical data only.
        print("Ages describe is ", ages.describe())

    # type: ignore
    def create_dataframe_from_array(self, arr: ndarray[int]) -> None:
        """Create dataframe from array."""
        print("Array prior dataframe is ", arr)  # type: ignore
        df = pd.DataFrame(arr)
        print(df)

    def create_dataframe_from_csv(self, path: str) -> None:
        """Create dataframe from csv."""
        df: pd.DataFrame = pd.read_csv(path)  # type: ignore
        print(df)  # type: ignore

    def read_csv_head_rows(self, path: str) -> None:
        """Read csv head rows."""
        print("Reading csv head rows from ", path)
        df = pd.read_csv(path)
        print(df.head(4))

    def read_csv_tail_rows(self, path: str) -> None:
        """Read csv tail rows."""
        print("Reading csv tail rows from ", path)
        df = pd.read_csv(path)
        print(df.tail(4))

    def save_dataframe(self, arr: ndarray[int]) -> None:  # type: ignore
        """Save dataframe."""
        df = pd.DataFrame(arr)
        df.to_csv('C:\\Data\\test_dataframe.csv')
        print("Dataframe saved to C:\\Data\\test_dataframe.csv")

    # type: ignore
    # Currently following routine causing an error. Need to fix.
    def save_dataframe_to_excel(self, path: str) -> None:
        """Save dataframe to excel."""
        df = pd.read_csv(path)
        print(df)
        df.to_excel('C:\\Data\\fruits.xlsx',
                    sheet_name='fruits', index=False)
        print("Dataframe saved to C:\\Data\\fruits.xlsx")

    def save_txt(self, arr: ndarray[int]) -> None:  # type: ignore
        """Save txt."""
        np.savetxt('C:\\Data\\dataframe.csv', arr, fmt='%.2f',  # type: ignore
                   delimiter=',', header='1, 2, 3, 4, 5')
        print("Dataframe saved to C:\\Data\\dataframe.csv")


if __name__ == '__main__':
    pandas_use_instance = PandasUse()
    pandas_use_instance.print_array(pd.array([1, 2, 3]))  # type: ignore
    pandas_use_instance.create_dataframe_from_array(  # type: ignore
        pd.array([1, 2, 3, 4, 5]))  # type: ignore
    # pandas_use_instance.print_dataframe(  # type: ignore
    #     pd.array([1, 2, 3, 4, 5]))  # type: ignore
    # pandas_use_instance.save_dataframe(  # type: ignore
    #     pd.array([1, 2, 3, 4, 5]))  # type: ignore
    # pandas_use_instance.read_csv('C:\\Data\\test_dataframe.csv')
    # pandas_use_instance.save_txt(pd.array([1, 2, 3, 4, 5]))  # type: ignore

    pandas_use_instance.create_dataframe()  # type: ignore
    pandas_use_instance.create_series_from_scratch()  # type: ignore
    pandas_use_instance.create_dataframe_from_csv(  # type: ignore
        "C:\\Data\\Fruits.csv")  # type: ignore
    pandas_use_instance.read_csv_head_rows(
        "C:\\Data\\Fruits.csv")  # type: ignore
    pandas_use_instance.read_csv_tail_rows(
        "C:\\Data\\Fruits.csv")  # type: ignore

    # pandas_use_instance.save_dataframe_to_excel(
    #     "C:\\Data\\Fruits.csv")  # type: ignore
