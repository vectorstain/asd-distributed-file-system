# Echo server program
import socket
import chunker

HOST = '127.0.0.1'        # Symbolic name meaning all available interfaces
PORT = 50001              # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    fileN = "./transfered/" + "test.txt"
    fileT = open(fileN, "wb")
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            fileT.write(data)
            if not data: break
            print("Received"+repr(data)+"\n")
    fileT.close()