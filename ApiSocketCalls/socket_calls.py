import socket

#  Class for Socket calls


class SocketCalls:
    sock: socket.socket
    msg_len: int = 0
    is_connection_made: bool = False

    # Initializing sock variable with socket object
    def __init__(self) -> None:

        # , sock: socket.socket
        # if sock is None:
        #     self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # else:
        #     self.sock = sock
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establishing socket connection with given host & port
    def connect(self, host: str, port: int) -> None:
        try:
            # self.sock.bind((socket.gethostname(), 9000))
            self.sock.connect((host, port))
            self.sock.bind((host, port))
            self.sock.listen(5)  # number of connect requests
            # self.sock.connect((host,port))
            self.is_connection_made = True
            self.sock.setblocking(False)
        except Exception as ex:
            print("Connect: ", ex)

    # Sending message to established socket connection
    def send_message(self, msg: bytearray) -> None:
        self.msg_len = len(msg)
        totalsent: int = 0
        try:
            while totalsent < self.msg_len:
                sent: int = self.sock.send(msg)
                if sent == 0:
                    raise RuntimeError("Socket connection broken. ")
                totalsent += sent
        except Exception as ex:
            print("send_message: ", ex)

    # Receiving message from established socket connection
    # Receiving error as of now while receiving message from socket connection
    def receive_message(self) -> bytes | str | None:
        ### Function to receive message from socket ###
        result : bytes | str | None
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
            
        except Exception as ex:
            print("receive_message: ", ex)
            result = ex.__str__()
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


# https://stackoverflow.com/questions/2778840/socket-error-errno-10013-an-attempt-was-made-to-access-a-socket-in-a-way-forb
# to know if another process listening to the same port

# netstat -ban

# netstat -ano | find ":5000"
# taskkill /f /pid process_id

# net stop http

# VS Code
# Open terminal -> ports tab , delete the port allocated by remote host

# net stop winnat
# net start winnat

# Firewall - Outbound rule - SQL Server instance MSSQLServer

# python file_name runserver localhost:port_number
