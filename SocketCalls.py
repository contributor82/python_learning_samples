

import socket

class SocketCalls: 
    sock = None
    MSGLEN = 0
    IsConnectionMade = False

    # Initializing sock variable with socket object
    def __init__(self, sock=None):
        
        if sock is None: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else: 
            self.sock = sock
    
    # Establishing socket connection with given host & port
    def connect(self, host, port): 
        try: 
            self.sock.connect((host,port))
            self.IsConnectionMade = True
            self.sock.setblocking(False)
        except Exception as ex: 
            print("Connect: ", ex)
    
    # Sending message to established socket connection
    def send_message(self, msg): 
        self.MSGLEN = len(msg)
        totalsent =0
        try: 
            while totalsent < self.MSGLEN: 
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
            while bytes_received < self.MSGLEN: 
                # min(bytes_received - self.MSGLEN, 2048) 
                chunk = self.sock.recv(self.MSGLEN)
                if chunk == b'': 
                    raise RuntimeError("Socket conneciton broken. ")
                chunks.append(chunk)
                bytes_received += len(chunk)
            return b''.join(chunks)
        except Exception as ex:
            print("receive_message: ", ex)


scInstance = SocketCalls()
scInstance.connect("127.0.0.1",80) 

if  scInstance.IsConnectionMade == True:
    msg_data = bytearray("Hello, Socket calls.", encoding='utf-8')
    scInstance.send_message(msg_data)
    received_msg = scInstance.receive_message()
    print(" Socket received message as : ", received_msg)
else: 
    print(" Since no connection has been established, no message send and receive possible. ")
