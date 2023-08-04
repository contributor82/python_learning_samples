import socket

#  Class for Socket calls
class SocketCalls: 
    sock : socket.socket
    msg_len: int = 0
    is_connection_made = False

    # Initializing sock variable with socket object
    def __init__(self, sock: socket.socket = None):
        
        if sock is None: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else: 
            self.sock = sock
    
    # Establishing socket connection with given host & port
    def connect(self, host : str, port: int): 
        try: 
            self.sock.connect((host,port))
            self.is_connection_made = True
            self.sock.setblocking(False)
        except Exception as ex: 
            print("Connect: ", ex)
    
    # Sending message to established socket connection
    def send_message(self, msg : bytearray): 
        self.msg_len = len(msg)
        totalsent =0
        try: 
            while totalsent < self.msg_len: 
                sent = self.sock.send(msg)
                if sent == 0: 
                    raise RuntimeError("Socket connection broken. ")
                totalsent += sent
        except Exception as ex: 
            print("send_message: ", ex)
    
    # Receiving message from established socket connection
    # Receiving error as of now while receiving message from socket connection
    def receive_message(self): 
        chunks = []
        bytes_received =0
        try: 
            while bytes_received < self.msg_len: 
                # min(bytes_received - self.msg_len, 2048) 
                chunk = self.sock.recv(self.msg_len)
                if chunk == b'': 
                    raise RuntimeError("Socket conneciton broken. ")
                chunks.append(chunk)
                bytes_received += len(chunk)
            return b''.join(chunks)
        except Exception as ex:
            print("receive_message: ", ex)


if __name__ == '__main__':

    sc_instance = SocketCalls()
    # host and port specified
    sc_instance.connect("localhost",80) 

    if  sc_instance.is_connection_made == True:
        msg_data = bytearray("Hello, Socket calls.", encoding='utf-8')
        sc_instance.send_message(msg_data)
        received_msg = sc_instance.receive_message()
        print(" Socket received message as : ", received_msg)
    else: 
        print(" Since no connection has been established, no message send and receive possible. ")
