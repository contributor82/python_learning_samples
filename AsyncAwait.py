
class DataOperations:
    data : str = ''
# YET TO BE DONE - OPERATION CAN'T BE COMPLETED SINCE CALL IS NOT IN WAITING FOR COMPLETION. 

    async def set_data(self):
        self.data = "Asynchronous data operations"
        return await self.data
    
    async def get_data(self): 
       storedData = self.set_data()
       if storedData == b'':
            raise StopAsyncIteration
       return await storedData
 
dataOperationsInstance = DataOperations()
data = dataOperationsInstance.get_data()
print(data)
