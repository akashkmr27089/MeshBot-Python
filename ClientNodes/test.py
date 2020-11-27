import socket
import Model.ClientNodeModal
from ClientComm import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'[231,123,234,234,22545,False]')
    s.sendall(str([111,222,333,444,22545,False]).encode('utf-8'))
    # s.sendall(b'Hello, world')
    data = s.recv(1024)
    dataToList = str(data).strip('b').strip("/'/'").strip('[]').split(',')
    ListToInt = map(int, dataToList)
    print('Received', [x for x in ListToInt])