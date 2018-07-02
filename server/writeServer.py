import socket

HOST, PORT = 'localhost', 5000
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind((HOST,PORT))
serv.listen(5)

print 'listening ...'

while True:
    conn, addr = serv.accept()
    print 'client connected ... ', addr
    myfile = open('video/testfile.mp4', 'w')

    while True:
        data = conn.recv(BUFSIZE)
        if not data: break
        myfile.write(data)
        print 'writing file ....'

    myfile.close()
    print 'finished writing file'
    conn.close()
    print 'client disconnected'