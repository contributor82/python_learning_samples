"""Module for pandas samples."""

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

    def save_dataframe(self, arr: ndarray[int]) -> None:  # type: ignore
        """Save dataframe."""
        df = pd.DataFrame(arr)
        df.to_csv('C:\\Data\\test_dataframe.csv')
        print("Dataframe saved to C:\\Data\\test_dataframe.csv")

    def read_csv(self, path: str) -> None:
        """Read csv."""
        df: pd.DataFrame = pd.read_csv(path)  # type: ignore
        print(df)

    def save_txt(self, arr: ndarray[int]) -> None:
        """Save txt."""
        np.savetxt('C:\\Data\\dataframe.csv', arr, fmt='%.2f',
                   delimiter=',', header='1, 2, 3, 4, 5')
        print("Dataframe saved to C:\\Data\\dataframe.csv")


if __name__ == '__main__':
    pandas_use_instance = PandasUse()
    pandas_use_instance.print_array(pd.array([1, 2, 3]))  # type: ignore
    pandas_use_instance.print_dataframe(  # type: ignore
        pd.array([1, 2, 3, 4, 5]))  # type: ignore
    pandas_use_instance.save_dataframe(  # type: ignore
        pd.array([1, 2, 3, 4, 5]))  # type: ignore
    pandas_use_instance.read_csv('C:\\Data\\test_dataframe.csv')
    pandas_use_instance.save_txt(pd.array([1, 2, 3, 4, 5]))  # type: ignore
