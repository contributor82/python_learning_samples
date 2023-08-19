""" Isolated Asynchronous IO test """
import unittest
from unittest import IsolatedAsyncioTestCase

# Incomplete due to connection object and its properties.

class Test(IsolatedAsyncioTestCase):
    """Test class """
    events: list[str] = ['']
    _async_connection =  None


    def setUp(self) -> None:
        self.events.append('setUp')

    async def async_connection(self) -> None:
        """ Async connection method """
        # Connection can't be formed since there is no connection object to be generated.
        return None

    async def async_set_up(self) -> None:
        """ Asynchronous set up method """
        self._async_connection = await self.async_connection()
        self.events.append('asyncSetUp')

    async def test_response(self) -> None:
        """ Test response method """
        self.events.append('test_response')
        response = await self._async_connection.get('https://example.com') # type: ignore
        self.assertEqual(response.status_code, 200) # type: ignore
        self.addAsyncCleanup(self.on_cleanup)

    def tear_down(self) -> None:
        """Tear down method """
        self.events.append('tearDown')

    async def async_tear_down(self) -> None:
        """ Async tear down method """
        await self._async_connection.close() # type: ignore
        self.events.append('asyncTearDown')

    async def on_cleanup(self) -> None:
        """On clean up method"""
        self.events.append('on_cleanup')

if __name__ == '__main__':
    unittest.main()
