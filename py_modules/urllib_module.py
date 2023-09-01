"""Module for internet URL access """
# import http
# from http.client import HTTPResponse
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
import tempfile
import shutil
import os


class InternetAccess:
    """Internet acccess class """
    url: str | Request
    url_contents: list[str]
    response_object: object = None

    def __init__(self, input_request: str | Request) -> None:
        self.url = input_request
        self.url_contents = ['']

    def open_url(self) -> None:
        """Open internet url and read data method """
        try:
            with urlopen(self.url) as response:
                self.response_object = response
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
            print('Url: ', self.url)
            print('Contents: ', self.url_contents)

    def copy_response_to_temp(self, user_provided_temp_file: str) -> None:
        """Copy received response to temp file """
        # Direct object writing is not working.
        # Temporary file creation is failing even though file path is appearing.
        # Therefor, applied alternative of creating temp file first, writing contents in it
        # and then, copying file to user given file.
        # but due to temporary file wrapper use, file copy operation is failing.
        try:
            self.open_url()
            if not self.response_object is None and self.response_object.code == 200: # type: ignore
                if user_provided_temp_file != '' and os.path.isfile(user_provided_temp_file):
                    with open(user_provided_temp_file, mode='wb+') as user_temp_file:
                            print('User Temp file name: ', user_provided_temp_file)
                            with tempfile.NamedTemporaryFile(mode='wb+', prefix='response_') as new_temp_file:
                                print('Temp file name: ', new_temp_file.name)
                                for url_content_line in self.url_contents:
                                    encoded_data = url_content_line.encode("utf-8")
                                    bytes_array = bytearray(encoded_data)
                                    new_temp_file.write(bytes_array) # type: ignore
                                shutil.copyfile(new_temp_file, user_temp_file) # type: ignore
                            # shutil.copyfileobj(self.url_contents,user_temp_file) # type: ignore
                else:
                    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                            print('Temp file name: ', temp_file.name)
                            shutil.copyfileobj(self.response_object, temp_file) # type: ignore
                            shutil.copyfileobj(self.url_contents,temp_file) # type: ignore
                    print(' Response copied successfully. ')
            else:
                raise HTTPError(str(self.url),-1,'Response Error','Empty headers', None) # type: ignore
        except AttributeError as temp_file_attribute_error:
            print(temp_file_attribute_error)
        except ValueError as temp_file_value_error:
            print(temp_file_value_error)
        except FileNotFoundError as temp_file_not_found_error:
            print(temp_file_not_found_error)
        except OverflowError as obj_overflow_error:
            print(obj_overflow_error)
        except OSError as copy_response_os_error:
            print(copy_response_os_error)

if __name__ == '__main__':
    internet_access_instance = InternetAccess('http://worldtimeapi.org/api/timezone/etc/UTC.txt')
    internet_access_instance.open_url()
    internet_access_instance.display_url_contents()
    internet_access_instance.copy_response_to_temp('C:\\Data\\response_holder_file.txt')
    internet_access_instance.copy_response_to_temp('')


