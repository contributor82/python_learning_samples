
import asyncio
import time

class AsyncAwaitOperations:
    data : str = ''

    async def set_data(self):
        self.data = "Asynchronous data operations"
        await asyncio.sleep(1)
        return self.data
    
    async def get_data(self): 
       storedData = await self.set_data()
       if storedData == b'':
            raise StopAsyncIteration
       await asyncio.sleep(1)
       return storedData
    
    async def task_one(self): 
        await asyncio.sleep(1)
        print("First Task")

    async def task_two(self): 
        await asyncio.sleep(1)
        print("Second Task")
    
    async def task_exec(self): 
        task1 = asyncio.create_task(self.task_one())
        task2 = asyncio.create_task(self.task_two())

        print(f"Starting task execution at {time.strftime('%X')}")

        await task1
        await task2

        print(f"finished task execution at {time.strftime('%X')}")
 
if __name__ == '__main__': 
    asyncAwaitOperationInstance = AsyncAwaitOperations()

    asyncio.run(asyncAwaitOperationInstance.task_exec())
