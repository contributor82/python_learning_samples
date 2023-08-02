
import asyncio
import time


class AsyncAwaitOperations:
    ### Async await operations ###
    data: str = ''

    # Function for setting data
    async def set_data(self) -> str:
        ### Setting data ###
        self.data = "Asynchronous data operations"
        await asyncio.sleep(1)
        return self.data

    async def get_data(self) -> str:
        ### Getting data ###
        stored_data: str = " "
        stored_data = await self.set_data()
        if stored_data == ' ':
            raise StopAsyncIteration
        await asyncio.sleep(1)
        return stored_data

    async def task_one(self) -> None:
        ### task one ###
        await asyncio.sleep(1)
        print("First Task")

    async def task_two(self) -> None:
        ### task two ###
        await asyncio.sleep(1)
        print("Second Task")

    async def task_exec(self) -> None:
        ### task execution ###
        task1 = asyncio.create_task(self.task_one())
        task2 = asyncio.create_task(self.task_two())

        print(f"Starting task execution at {time.strftime('%X')}")

        await task1
        await task2

        print(f"finished task execution at {time.strftime('%X')}")


if __name__ == '__main__':
    aao_instance = AsyncAwaitOperations()
    asyncio.run(aao_instance.task_exec())
