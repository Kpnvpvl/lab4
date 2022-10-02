import asyncio
import sys


class ChatClass:
    __slots__ = (
        'server_name',
        'server',
        'relations',
        'type'
    )

    def __init__(self, room, port, loop, type_of_room):
        self.type = type_of_room
        self.server_name = room
        self.relations = {}
        self.server = loop.run_until_complete(
            asyncio.start_server(
                self.accept_connection, "127.0.0.1", port))

    async def broadcast(self, message):
        for reader, writer in self.relations.values():
            writer.write((message + "\n").encode("utf-8"))
            await writer.drain()

    async def prompt_username(self, reader, writer):
        while True:
            writer.write("Enter username: ".encode("utf-8"))
            await writer.drain()
            data = (await reader.read(100)).decode("utf-8")
            if not data:
                return None
            username = data.strip()
            print(username)
            if username and username not in self.relations:
                self.relations[username] = (reader, writer)
                return username
            writer.write("Take another username.\n".encode("utf-8"))
            await writer.drain()

    async def handle_connection(self, username, reader):
        while True:
            data = (await reader.readline()).decode("utf-8")
            if not data:
                del self.relations[username]
                return None
            await self.broadcast(username + ": " + data.strip())

    async def accept_connection(self, reader, writer):
        writer.write((str(self.server_name) + '\n').encode("utf-8"))
        await writer.drain()
        username = (await self.prompt_username(reader, writer))
        if username is not None:
            await self.broadcast(f"User {username} has joined the room")
            await self.handle_connection(username, reader)
            await self.broadcast(f"User {username} has left the room")
        await writer.drain()


def main(argv):
    loop = asyncio.new_event_loop()
    room = ChatClass("Room", 8000, loop, 'public')
    try:
        loop.run_forever()
    except Exception as e:
        pass
    finally:
        loop.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
