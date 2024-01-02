"""Module for pandas samples."""

from numpy import ndarray
import pandas as pd


class PandasUse:
    """Pandas use class."""

    def print_array(self, arr: ndarray[int]) -> None:  # type: ignore
        """Print array."""
        print(arr)  # type: ignore

    def print_dataframe(self, arr: ndarray[int]) -> None:
        """Print dataframe."""
        df = pd.DataFrame(arr)
        print(df)

    def save_dataframe(self, arr: ndarray[int]) -> None:
        """Save dataframe."""
        df = pd.DataFrame(arr)
        df.to_csv('C:\\Data\\test_dataframe.csv')
        print("Dataframe saved to C:\\Data\\test_dataframe.csv")

    def read_csv(self, path: str) -> None:
        """Read csv."""
        df: pd.DataFrame = pd.read_csv(path)
        print(df)


if __name__ == '__main__':
    pandas_use_instance = PandasUse()
    pandas_use_instance.print_array(pd.array([1, 2, 3]))  # type: ignore
    pandas_use_instance.print_dataframe(
        pd.array([1, 2, 3, 4, 5]))  # type: ignore
    pandas_use_instance.save_dataframe(
        pd.array([1, 2, 3, 4, 5]))  # type: ignore
    pandas_use_instance.read_csv('C:\\Data\\test_dataframe.csv')
