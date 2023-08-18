"""Module for Email operations """
import sys
import smtplib
from email.message import EmailMessage

# Sending an email from python script
# This is as per the python documentation
class EmailOperations:
    """ Email operations class """
    host: str = ""
    port: int = 0
    server: smtplib.SMTP

    def __init__(self, host_address: str, port_num: int) -> None:
        """ Initializing host and port """
        # Connection error causing send message not working - DO NOT USE
        try:
            self.host = host_address
            self.port = port_num
            self.server = smtplib.SMTP(self.host, self.port)
        except smtplib.SMTPConnectError as connection_error:
            print(connection_error)

    def quit_server(self) -> None:
        """ Quit server """
        try:
            self.server.quit()
        except smtplib.SMTPServerDisconnected as con_disconnected_error:
            print(con_disconnected_error)


    def send_message_from_file(self, file_name: str, sender: str, recipient: str) -> bool:
        """ Function to send message from file """

        is_send_msg: bool = False
        try:
            with open(file_name, encoding="UTF-8") as file_handle:
                msg = EmailMessage()
                msg.set_content(file_handle.read())

                msg['Subject'] = f'the contents of {file_name}'
                msg['From'] = sender
                msg['To'] = recipient

                self.server.send_message(msg)
                is_send_msg = True
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
            is_send_msg = False
        except smtplib.SMTPDataError as data_error:
            print(data_error)
            is_send_msg = False
        return is_send_msg


    def send_email(self) -> bool:
        """ Function to send email by accepting sender, receiver and message from command line """
        # Send email - causing connection error and not sending message as expected.
        is_send_email: bool = False
        try:
            fromaddr: str = input("From: ")
            toaddrs: list[str] = input("To: ").split(",")
            print("Enter message end with ^D: ")
            msg: str = ""
            line: str = ""
            line_cnt: int = 0
            while True:
                line = sys.stdin.readline()
                line_cnt += 1
                msg += line
                if line_cnt == 2:
                    break

            # The actual mail send
            self.server.sendmail(fromaddr, toaddrs, msg)
            is_send_email = True
        except smtplib.SMTPDataError as data_error:
            print(data_error)
            is_send_email = False
        return is_send_email

    # Receive email
    def receive_email(self) -> None:
        """ Function to receive reply from server """

        try:
            reply = self.server.getreply()
            print(reply)
        except smtplib.SMTPResponseException as response_ex:
            print(response_ex)
        except smtplib.SMTPException as ex:
            print(ex)

if __name__ == '__main__':
    try:
        eo_instance = EmailOperations('localhost', 25)
        if eo_instance.send_email() is True:
            eo_instance.receive_email()
            eo_instance.quit_server()

        eo_from_file_instance = EmailOperations('localhost', 25)
        msg_txt_file: str = "C:\\Data\\msg_file.txt"
        sender_email: str = "private.user1@test.com"
        receiver_email:str = "private.user2@test.com"
        if eo_from_file_instance.send_message_from_file(msg_txt_file, sender_email,
                                                        receiver_email) is True:
            eo_from_file_instance.receive_email()
            eo_from_file_instance.quit_server()

    except smtplib.SMTPException as smtp_exception:
        print(smtp_exception)
