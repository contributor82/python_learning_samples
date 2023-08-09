"""Module for internet URL access """
from urllib.error import URLError
from urllib.request import urlopen, Request


class InternetAccess:
    """Internet acccess class """

    def open_url(self, input_request: str | Request) -> None:
        """Open internet url and read data method """
        try:
            with urlopen(input_request) as response:
                for line in response:
                    line = line.decode() # Convert bytes to a str
                    if line.startswith('datetime'):
                        print(line.rstrip())
        except URLError as url_error:
            print(url_error)
            print('Exception occurred : No internet access. ')


if __name__ == '__main__':
    internet_access_instance = InternetAccess()
    input_url: str | Request = 'http://worldtimeapi.org/api/timezone/etc/UTC.txt'
    internet_access_instance.open_url(input_url)
