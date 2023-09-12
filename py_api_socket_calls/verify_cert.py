"""Module for Certificates verification """
# import urllib3.request
from urllib.error import URLError
import urllib.request
import ssl

class UrlUsingCert:
    """Url using certificates """
    ssl_context: ssl.SSLContext | None
    url: str
    cert_file_path: str
    url_contents = list[str]

    def __init__(self, input_url: str, cert_file: str) -> None:
        """Initialize certification file path """
        self.ssl_context = None
        self.url = input_url
        self.cert_file_path = cert_file
        self.url_contents = ['']

    def disable_all_cert_verification(self)-> None:
        """Disable all certificates verification """
        self.context = ssl._create_unverified_context() #type: ignore

    def enable_http_cert_verification(self)-> None:
        """Enable http cert verification by creating context"""
        try:
            self.ssl_context = ssl.create_default_context(cafile= self.cert_file_path)
        except OSError as enable_http_cert_os_error:
            print(enable_http_cert_os_error)

    def enable_https_cert_verification(self)-> None:
        """Enable https cert verification by creating context """
        try:
            self.ssl_context = ssl._create_default_https_context(cafile= self.cert_file_path) #type:ignore
        except OSError as enable_https_cert_os_error:
            print(enable_https_cert_os_error)

    def open_url_with_cert(self) -> None:
        """Open internet url and read data method """
        try:
            with urllib.request.urlopen(self.url, context=self.ssl_context) as response:
                self.response_object = response
                for line in response:
                    line = line.decode() # Convert bytes to a str
                    # if line.startswith('datetime'):
                    self.url_contents.append(line.rstrip()) # type: ignore
                print('Contents: ', self.url_contents)
        except URLError as url_error:
            print(url_error)
            print('Exception occurred : No internet access. ')
        except NameError as url_name_error:
            print(url_name_error)
        except AttributeError as url_attr_error:
            print(url_attr_error)

if __name__ == '__main__':
   url_using_cert_instance =  UrlUsingCert('https://localhost:443',
                                           'C:\\Users\vaibh\\.cert\\localhost.pfx')
   url_using_cert_instance.enable_http_cert_verification()
   url_using_cert_instance.open_url_with_cert()
