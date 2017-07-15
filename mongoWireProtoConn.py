from struct import *
import socket

buffer_size=1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 27017))

message = bytearray()
ss = bytes("Where is Mongo?", 'utf-8')    # Or other appropriate encoding
message.extend(pack("<iiii16sh", 16+len(ss)+1,1,0,1000, ss, 0))

s.send(message)
data = s.recv(buffer_size)
print(data)

s.close()
