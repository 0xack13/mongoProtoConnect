from struct import *
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 27017))

message = bytearray()
testMsg1 = "HELLO!".encode('utf-8')
testMsg2 = bytes.fromhex("00")
#mongodb uses little-endian
message.extend(pack('<4shhhhh',testMsg1,0,16+len(testMsg1),1,0,1000))

s.send(message)

s.close()
