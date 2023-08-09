import asyncio
from io import TextIOWrapper
import time

# Following Async comprehensions seems changed from python 3.10 version hence DO NOT USE. 
# Below program lines generates errors. 
# result = [async for i in aiter() if i % 2]
# result = [await fun() for fun in funcs if await condition()]

# Async function with async iterator that async for. 
# Currently call is never waiting for the completion. 
# added sleep timer for 100 seconds before printing value but getting RuntimeWarning: corountine 'async_for' was never awaited. 

# Async comprehensions 
class AsyncComprehensions: 

    async def sleep(self) -> None:
        ### sleep ###
        await asyncio.sleep(1)

    async def async_for(self, input_data: list[int]) -> None: 
        ### asynchronous for ###

        iterable: list[int] = (input_data)
        for i in iter(iterable): 
            if (i % 2)==0: 
                await self.sleep()
                print("async for - printing for even numbers: ", i)

    async def async_with(self, file_name: str ) -> None:
        ### asynchronous with ###

        file_handle: TextIOWrapper
        data:str = ''
        file_handle = open(file_name,'r')
        await self.sleep()
        data = file_handle.read()
        print("async with - File Data: = ", data)

    async def counter(self) -> None: 
        ### counter ### 

        await asyncio.sleep(1)
        print('1')
        await asyncio.sleep(2)
        print('2')
        await asyncio.sleep(3)
        print('3')

    async def gather_all(self, input_data: list[int], file_name: str) -> None: 
        ### aggregating asynchronous results ###
        
        await asyncio.gather(self.counter(), self.counter(), self.counter(), self.async_for(input_data), self.async_with(file_name))


if __name__ == "__main__":
    t: float = time.perf_counter()
    ac_instance = AsyncComprehensions()
    sample_data: list[int] = [1,2,3,4,5]
    file_name: str = 'C:\\Data\\textfile.txt'
    asyncio.run(ac_instance.gather_all(sample_data,file_name))
    t2: float = time.perf_counter()
        
    print(f'Total time elapsed: {t2:0.2f} seconds')
