import socket

HOST, PORT = 'localhost', 4000
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind((HOST,PORT))
serv.listen(5)

print 'listening ...'

while True:
    conn, addr = serv.accept()
    print 'client connected ... ', addr
    file = open('video/testfile.mp4')
    bytes = file.read()
    conn.send(bytes)
    conn.close()
    file.close()
    print 'client disconnected'
