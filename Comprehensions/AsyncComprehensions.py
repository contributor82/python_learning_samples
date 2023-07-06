from asyncio import sleep
import tracemalloc

# Following Async comprehensions seems changed from python 3.10 version hence DO NOT USE. 
# Below program lines generates errors. 
# result = [async for i in aiter() if i % 2]
# result = [await fun() for fun in funcs if await condition()]

# Async function with async iterator that async for. 
# Currently call is never waiting for the completion. 
# added sleep timer for 100 seconds before printing value but getting RuntimeWarning: corountine 'async_for' was never awaited. 


class AsyncComprehensions: 

    async def async_for(self): 
        async for i in range(5): 
            if (i % 2)==0: 
                sleep(100)
                await print(i)

    async def async_with(self):
        async with (1==1) as target:
            await print("Async With statement")


asyncCompInstance = AsyncComprehensions()

asyncCompInstance.async_for()
asyncCompInstance.async_with()
print(tracemalloc.get_tracemalloc_memory() )