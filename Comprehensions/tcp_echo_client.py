import asyncio


class TcpClient:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter
    data: bytes

    # if connection established with host and port then returned reader & writer instances
    # Currently couldn't establish connection : Error : The remote computer refused the network connection
    # Due to which reader & writer instances have not been formed.
    async def establish_connection(self, host: str | None, port: int | str | None) -> None:
        try:
            self.reader, self.writer = await asyncio.open_connection(host, port)
            print("Connection established..")
        except ConnectionError as ex:
            print(ex)

    # Writing message using writer instance
    async def send_message(self, message: str) -> None:
        try:
            print(f'Send: {message!r}')
            self.writer.write(message.encode())
            await self.writer.drain()
            print("Message sent.. ")
        except Exception as ex:
            print(ex)

    # reading message using reader instance
    async def receive_message(self) -> None:
        try:
            self.data = await self.reader.read(100)
            print(f'Received: {self.data.decode()!r}')
        except Exception as ex:
            print(ex)

    # closing connection to host and port.
    async def close_connection(self) -> None:
        try:
            print('Close the connection')
            self.writer.close()
            await self.writer.wait_closed()

        except ConnectionError as ex:
            print(ex)


if __name__ == '__main__':
    tcpClientInstance = TcpClient()
    asyncio.run(tcpClientInstance.establish_connection('localhost', 8080))
    asyncio.run(tcpClientInstance.send_message('Hello World!'))
    asyncio.run(tcpClientInstance.receive_message())
    asyncio.run(tcpClientInstance.close_connection())
