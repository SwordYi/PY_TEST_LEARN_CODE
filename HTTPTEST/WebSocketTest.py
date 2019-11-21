import websocket
url = "ws://127.0.0.1:8080"
ws = websocket.create_connection(url)
ws.send("{\"request\":1111, \"service\":1001, \"name\":\"xxxx\"}")
new_msg = ws.recv()
print(new_msg)

ws.send("{\"request\":\1111,\"service\":1003,\"name\":\"x\",\"message\":\"1111111\"}")
new_msg1 = ws.recv()
print(new_msg)
