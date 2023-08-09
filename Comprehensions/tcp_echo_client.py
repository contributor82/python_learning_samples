"""Module for Tcp client """
import asyncio


class TcpClient:
    """ Tcp client class """

    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter
    data: bytes

    async def establish_connection(self, host: str | None, port: int | str | None) -> None:
        """ Connection establishment """
        # if connection established with host and port then returned reader & writer instances
        # Currently couldn't establish connection :
        # Error : The remote computer refused the network connection
        # Due to which reader & writer instances have not been formed.
        try:
            self.reader, self.writer = await asyncio.open_connection(host, port)
            print("Connection established..")
        except ConnectionError as ex:
            print(ex)


    async def send_message(self, message: str) -> None:
        """ sending message method """
        # Writing message using writer instance
        try:
            print(f'Send: {message!r}')
            self.writer.write(message.encode())
            await self.writer.drain()
            print("Message sent.. ")
        except Exception as ex:
            print(ex)


    async def receive_message(self) -> None:
        """ receiving message method """
        # reading message using reader instance
        try:
            self.data = await self.reader.read(100)
            print(f'Received: {self.data.decode()!r}')
        except Exception as ex:
            print(ex)


    async def close_connection(self) -> None:
        """ closing connection method """
        # closing connection to host and port.
        try:
            print('Close the connection')
            self.writer.close()
            await self.writer.wait_closed()

        except ConnectionError as con_error:
            print(con_error)

if __name__ == '__main__':
    tcp_client_instance = TcpClient()
    asyncio.run(tcp_client_instance.establish_connection('localhost', 8080))
    asyncio.run(tcp_client_instance.send_message('Hello World!'))
    asyncio.run(tcp_client_instance.receive_message())
    asyncio.run(tcp_client_instance.close_connection())
