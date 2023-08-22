""" Isolated Asynchronous IO test """
import unittest
from unittest import IsolatedAsyncioTestCase
from urllib.request import urlopen

# Incomplete due to connection object and its properties.

class Test(IsolatedAsyncioTestCase):
    """Test class """
    events: list[str] = ['']
    _async_connection : object


    def setUp(self) -> None:
        self.events.append('setUp')

    async def async_connection(self, url: str) -> object:
        """ Async connection method """
        # Connection can't be formed since there is no connection object to be generated.
        with urlopen(url) as url_open_return:
            response = url_open_return
        return response

    async def async_set_up(self) -> None:
        """ Asynchronous set up method """
        self._async_connection = await self.async_connection('https://example.com')
        self.events.append('asyncSetUp')

    async def test_response(self) -> None:
        """ Test response method """
        test_result : bool| int | AttributeError
        try:
            self.events.append('test_response')
            response = await self._async_connection('https://example.com') # type: ignore
            with self.assertRaises(AttributeError):
                test_result = True
                test_result = 200
            self.assertEqual(response.status_code, 200) # type: ignore
            self.addAsyncCleanup(self.on_cleanup)
        except AttributeError as attribute_error:
            test_result = attribute_error
            self.assertEqual(str(test_result.args[0]),
                             "'Test' object has no attribute '_async_connection'")

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
