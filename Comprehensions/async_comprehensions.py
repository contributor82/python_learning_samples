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
        await asyncio.sleep(1)

    async def async_for(self) -> None: 
        data: list[int] = [1,2,3,4,5]
        iterable: list[int] = (data)
        for i in iter(iterable): 
            if (i % 2)==0: 
                await self.sleep()
                print("async for - printing for even numbers: ", i)

    async def async_with(self) -> None:
        file_handle: TextIOWrapper
        data:str = ''
        file_handle = open('C:\\Data\\textfile.txt','r')
        await self.sleep()
        data = file_handle.read()
        print("async with - File Data: = ", data)

    async def counter(self) -> None: 
        await asyncio.sleep(1)
        print('1')
        await asyncio.sleep(2)
        print('2')
        await asyncio.sleep(3)
        print('3')

    async def gather_all(self) -> None: 
        await asyncio.gather(self.counter(), self.counter(), self.counter(), self.async_for(), self.async_with())


if __name__ == "__main__":
    t: float = time.perf_counter()
    acInstance = AsyncComprehensions()
    asyncio.run(acInstance.gather_all())
    t2: float = time.perf_counter()
        
    print(f'Total time elapsed: {t2:0.2f} seconds')
