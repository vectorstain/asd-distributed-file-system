# Echo client program
import socket
import chunker
from io import BytesIO

HOST = '127.0.0.1'    # The remote host
PORT = 50001          # The same port as used by the server

chunk = chunker.chunk_file("test.txt")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i = 0
    while i <= chunk :
        # Open a temporary file and write a chunk of bytes
        file = open("./chunked/chunk"+ str(i) + "_" + "test.txt", "rb")
        s.sendall(file.read())
        file.close()
        i += 1
    s.close()