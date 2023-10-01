""" Module for socket functionality """
import socket


class SocketCalls:
    """ Socket calls class """
    sock: socket.socket
    conn: socket.socket
    addr: object
    msg_len: int = 0
    is_connection_made: bool = False
    host: str = ''
    port: int = 0

    def __init__(self, host_address: str, port_number: int) -> None:
        """ Initializing sock variable with socket object """
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Following line not considering as a socket
        # self.sock = socket.socket(socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
        # Following not considering giving an error - Invalid argument was supplied.
        # self.sock = socket.socket(socket.AF_UNSPEC, socket.SOCK_STREAM)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        self.host = host_address
        self.port = port_number

    def socket_connect(self) -> None:
        """ Establishing socket connection with given host & port """
        try:
            # Approach one : settimeout, connect, accept
            # Currently causing connection error
            self.sock.settimeout(300) ## in Seconds
            self.sock.connect((self.host, self.port))
            self.conn, self.addr =  self.sock.accept()

            # Approach two : bind, listen, accept
            # Currently causing connection error
            # self.sock.bind((self.host, self.port))
            # self.sock.listen(5)  # number of connect requests
            # self.conn, self.addr =  self.sock.accept()
            print("Connected to address : ", self.addr)
            self.is_connection_made = True
            self.sock.setblocking(False)
        except ConnectionError as conn_error:
            print("Connect: ", conn_error)

    def socket_disconnect(self) -> None:
        """ Close socket connection """
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except socket.error as socket_error:
            print(socket_error)

    def send_message(self, msg: bytearray) -> None:
        """ Sending message to established socket connection """
        self.msg_len = len(msg)
        # totalsent: int = 0
        try:
            # Sending message at one go.
            self.conn.sendall(msg)

            # Sending same message repetatively.
            # while totalsent < self.msg_len:
            #     sent: int = self.sock.send(msg)
            #     if sent == 0:
            #         raise RuntimeError("Socket connection broken. ")
            #     totalsent += sent
        except OSError as os_error:
            print("send_message: ", os_error)

    def receive_message(self) -> bytes | str | None:
        """ Function to receive message from socket """
        # Receiving message from established socket connection
        # Receiving error as of now while receiving message from socket connection
        result: bytes | str | None
        chunks: list[bytes] = [bytes()] # Creating a lit of bytes
        # bytes_received = 0
        # buff_obj = bytearray(self.msg_len) # Creating a byte array.
        try:
            # Receiving message by passing message length.
            chunk: bytes = self.sock.recv(self.msg_len)
            chunks.append(chunk)
            result = b''.join(chunks)
            # Run loop if needed based on how message has been sent.
            #self.sock.recv_into(buff_obj, self.msg_len) # type: ignore
            # while bytes_received < self.msg_len:
            #     # min(bytes_received - self.msg_len, 2048)
            #     chunk: bytes = self.sock.recv(self.msg_len)
            #     if chunk == b'':
            #         raise RuntimeError("Socket conneciton broken. ")
            #     chunks.append(chunk)
            #     bytes_received += len(chunk)
            # result = b''.join(chunks)

        except OSError as os_error:
            print("receive_message: ", os_error)
            result = os_error.args[0]
        return result



if __name__ == '__main__':
    try:
        host_name: str = socket.gethostbyname(socket.gethostname())
        sc_instance = SocketCalls(host_name, 3000)
        # host and port specified
        sc_instance.socket_connect()

        if sc_instance.is_connection_made is True:
            msg_data = bytearray("Hello, Socket calls.", encoding='utf-8')
            sc_instance.send_message(msg_data)
            received_msg: bytes | str | None = sc_instance.receive_message()
            print(" Socket received message as : ", received_msg)
            sc_instance.socket_disconnect()
        else:
            print(" Since no connection has been established," +
                  "no message send and receive possible. ")
    except OSError as main_os_error:
        print(main_os_error)
