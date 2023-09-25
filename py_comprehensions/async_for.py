"""Module for asynchronous for loop """

import asyncio

class AsyncIteratorWrapper:
    """Asynchronous iterator wrapper from documentation. """

    def __init__(self, str_val: str) -> None:
        """Initializing iterator"""
        self._it = iter(str_val)

    def __aiter__(self) -> object:
        """Returning self as iterator """
        return self

    async def __anext__(self) -> str:
        """Getting an extension """
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

    async def display(self)-> None:
        """Displaying iterator value. """
        print("Asynchronous for loop execution: \n ")
        async for letter in self: #type: ignore
            print("Letter from iter : ", letter) #type: ignore

if __name__ == '__main__':
    input_str: str = "abc"
    print("Input str : ", input_str)
    instance = AsyncIteratorWrapper(input_str)
    asyncio.run(instance.display())
