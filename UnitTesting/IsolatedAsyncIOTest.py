
# Isolated Asynchronous IO test
import unittest
from unittest import IsolatedAsyncioTestCase

# Incomplete due to connection object and its properties. 

class Test(IsolatedAsyncioTestCase): 
    events = ['']
    _async_connection = ''


    def setUp(self) -> None:
        self.events.append("setUp")

    # Connection can't be formed since there is no connection object to be generated. 
    async def AsyncConnection(self) -> None: 
        return None
    
    async def asyncSetUp(self) -> None:
        self._async_connection = await self.AsyncConnection()
        self.events.append("asyncSetUp")

    async def test_response(self) -> None: 
        self.events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup) 
    
    def tearDown(self) -> None:
        self.events.append("tearDown")
    
    async def asyncTearDown(self) -> None: 
        await self._async_connection.close()
        self.events.append("asyncTearDown")
    
    async def on_cleanup(self): 
        self.events.append("on_cleanup")
    
if __name__ == '__main__': 
    unittest.main()
    
    



