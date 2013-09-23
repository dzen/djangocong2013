#!/usr/bin/env python

import tulip
import websockets
from relips import client

@tulip.coroutine
def hello(websocket, uri):
    redis_client = yield from client.connect()
    print("connected to redis")
    yield from redis_client.subscribe(['channel'])
    while websocket.open:
        _, _, event = yield from redis_client.next()
        websocket.send(event.decode())

start_server = websockets.serve(hello, 'localhost', 8085)

tulip.get_event_loop().run_until_complete(start_server)
tulip.get_event_loop().run_forever()
