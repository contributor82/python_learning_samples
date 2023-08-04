import sys 
import smtplib
from email.message import EmailMessage

# Sending an email from python script
# This is as per the python documentation
class EmailOperations: 
    host: str = ""
    port: int = 0
    server: smtplib.SMTP

    # Initializing host and port
    # Connection error causing send message not working - DO NOT USE
    def __init__(self, host_address:str , port_num: int) -> None:
        self.host = host_address
        self.port = port_num
        self.server = smtplib.SMTP(self.host)

    def quit_server(self)-> None: 
        self.server.quit()


    def send_message_from_file(self, file_name: str, sender: str, recipient: str) -> bool: 
        ### Function to send message from file ###

        is_send_msg: bool = False
        try: 

            with open(file_name) as file_handle: 
                msg = EmailMessage()
                msg.set_content(file_handle.read())

                msg['Subject'] = f'the contents of {file_name}'
                msg['From'] = sender
                msg['To'] = recipient

                self.server.send_message(msg)
                is_send_msg = True
        except Exception as ex: 
            print(ex)
            is_send_msg = False
        return is_send_msg

    # Send email - causing connection error and not sending message as expected.
    def send_email(self) -> bool: 
        ### Function to send email by accepting sender, receiver and message from command line ### 

        is_send_email: bool = False
        try:
            fromaddr = input("From: ")
            toaddrs = input("To: ").split(",")
            print("Enter message end with ^D: ")
            msg = ''
            lineCount =0
            while True: 
                line = sys.stdin.readline()
                lineCount += 1
                msg += line
                if lineCount == 2: 
                    break
                
            # The actual mail send
            server = smtplib.SMTP(self.host,self.port)
            server.sendmail(fromaddr, toaddrs, msg)
            is_send_email = True
        except Exception as ex: 
            print(ex)
            is_send_email = False
        return is_send_email

    # Receive email
    def receive_email(self) -> None: 
        ### Function to receive reply from server ###

        try: 
            server = smtplib.SMTP(self.host)
            reply = server.getreply()
            print(reply)
        except Exception as ex: 
            print(ex)
        
if __name__ == '__main__': 
    try: 
        eo_instance = EmailOperations('localhost',25)
        if eo_instance.send_email() == True : 
            eo_instance.receive_email()
            eo_instance.quit_server()

        eo_from_file_instance = EmailOperations('localhost', 25)
        if eo_from_file_instance.send_message_from_file("C:\\Data\\msg_file.txt", "private.user1@test.com", "private.user2@test.com") == True: 
            eo_from_file_instance.receive_email()
            eo_from_file_instance.quit_server()

    except Exception as ex:
        print(ex)