"""Module for internet URL access """
from urllib.error import URLError
from urllib.request import urlopen, Request


class InternetAccess:
    """Internet acccess class """
    url: str | Request
    url_contents: list[str]

    def __init__(self, input_request: str | Request) -> None:
        self.url = input_request
        self.url_contents = ['']

    def open_url(self) -> None:
        """Open internet url and read data method """
        try:
            with urlopen(self.url) as response:
                for line in response:
                    line = line.decode() # Convert bytes to a str
                    if line.startswith('datetime'):
                        self.url_contents.append(line.rstrip())
        except URLError as url_error:
            print(url_error)
            print('Exception occurred : No internet access. ')

    def display_url_contents(self)-> None:
        """Display URL contents """
        if len(self.url_contents) > 0:
            print("Url: ", self.url)
            print("Contents: ", self.url_contents)


if __name__ == '__main__':
    internet_access_instance = InternetAccess('http://worldtimeapi.org/api/timezone/etc/UTC.txt')
    internet_access_instance.open_url()
    internet_access_instance.display_url_contents()
