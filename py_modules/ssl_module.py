"""ssl Module"""

import ssl


class SslModule:
    """SSL Module class """

    def __init__(self) -> None:
        pass

    def get_ssl_cert_info(self, hostaddress: tuple[str, int]) -> str:
        """Get SSL Cert Info"""
        server_certificate: str = ''
        try:
            server_certificate = ssl.get_server_certificate(hostaddress)
        except ssl.SSLError as get_ssl_cert_ssl_error:
            print(get_ssl_cert_ssl_error)
        except OSError as get_ssl_cert_os_error:
            print(get_ssl_cert_os_error)
        return server_certificate

    def get_ssl_ca_file_path(self) -> ssl.DefaultVerifyPaths | None:
        """Get SSL Ca file & path info"""
        default_verify_file_path: ssl.DefaultVerifyPaths | None
        try:
            default_verify_file_path = ssl.get_default_verify_paths()
        except OSError as get_ssl_ca_os_error:
            print(get_ssl_ca_os_error)
            default_verify_file_path = None
        return default_verify_file_path


if __name__ == '__main__':
    ssl_module_instance = SslModule()
    host_address: tuple[str, int] = ('localhost', 3000)

    server_cert: str = ssl_module_instance.get_ssl_cert_info(host_address)
    # print(' Server certificate for host_address',
    #      host_address, ' Cert info : ', server_cert)

    default_ca_file_path: ssl.DefaultVerifyPaths | None = ssl_module_instance.get_ssl_ca_file_path()

    if not default_ca_file_path is None:
        print(' SSL ca file: ', default_ca_file_path.cafile,
              ' SSL ca path: ', default_ca_file_path.capath)
    else:
        print('Default SSL ca file path not found. ')
