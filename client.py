
import asyncio
import sys


async def input_text(text=''):
    await asyncio.get_event_loop().run_in_executor(
        None, lambda s=text: sys.stdout.write(s + ' '))
    return await asyncio.get_event_loop().run_in_executor(
        None, sys.stdin.readline)





async def connection():
    r, w = await asyncio.open_connection('127.0.0.1', 8000)
    await asyncio.gather(get_data(r, w), send_data(w))

async def get_data(reader, writer):
    while True:
        try:
            data = await reader.read(100)
        except:
            return
        if writer.is_closing():
            return
        print(data.decode())


async def send_data(writer):
    while True:
        message = await input_text()
        writer.write(message.encode("UTF-8"))
        await writer.drain()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(connection())
loop.close()
