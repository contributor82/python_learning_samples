import sys 
import smtplib

# Sending an email from python script
# This is as per the python documentation
class EmailOperations: 
    host: str = ""
    port: int = 0

    # Initializing host and port
    def __init__(self, host_address:str , port_num: int) -> None:
        self.host = host_address
        self.port = port_num

    # Send email - causing connection error and not sending message as expected.
    def send_email(self) -> bool: 
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
            server.quit()
            return True
        except Exception as ex: 
            print(ex)
            return False

    # Receive email
    def receive_email(self) -> None: 
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
    except Exception as ex:
        print(ex)