""" Module for socket functionality """
import socket


class SocketCalls:
    """ Socket calls class """
    sock: socket.socket
    msg_len: int = 0
    is_connection_made: bool = False

    def __init__(self) -> None:
        """ Initializing sock variable with socket object """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host: str, port: int) -> None:
        """ Establishing socket connection with given host & port """
        try:
            # self.sock.bind((socket.gethostname(), 9000))
            self.sock.connect((host, port))
            self.sock.bind((host, port))
            self.sock.listen(5)  # number of connect requests
            # self.sock.connect((host,port))
            self.is_connection_made = True
            self.sock.setblocking(False)
        except ConnectionError as conn_error:
            print("Connect: ", conn_error)

    def send_message(self, msg: bytearray) -> None:
        """ Sending message to established socket connection """
        self.msg_len = len(msg)
        totalsent: int = 0
        try:
            while totalsent < self.msg_len:
                sent: int = self.sock.send(msg)
                if sent == 0:
                    raise RuntimeError("Socket connection broken. ")
                totalsent += sent
        except OSError as os_error:
            print("send_message: ", os_error)

    def receive_message(self) -> bytes | str | None:
        """ Function to receive message from socket """
        # Receiving message from established socket connection
        # Receiving error as of now while receiving message from socket connection
        result: bytes | str | None
        chunks: list[bytes] = [bytes()]
        bytes_received = 0
        try:
            while bytes_received < self.msg_len:
                # min(bytes_received - self.msg_len, 2048)
                chunk: bytes = self.sock.recv(self.msg_len)
                if chunk == b'':
                    raise RuntimeError("Socket conneciton broken. ")
                chunks.append(chunk)
                bytes_received += len(chunk)
            result = b''.join(chunks)

        except OSError as os_error:
            print("receive_message: ", os_error)
            result = os_error.args[0]
        return result


if __name__ == '__main__':

    sc_instance = SocketCalls()
    # host and port specified
    sc_instance.connect("127.0.0.1", 3000)

    if sc_instance.is_connection_made is True:
        msg_data = bytearray("Hello, Socket calls.", encoding='utf-8')
        sc_instance.send_message(msg_data)
        received_msg: bytes | str | None = sc_instance.receive_message()
        print(" Socket received message as : ", received_msg)
    else:
        print(" Since no connection has been established, no message send and receive possible. ")
