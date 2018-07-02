import socket
import threading

def listenToClient(client, address):
    BUFSIZE = 4096
    try:
        # send() + recv()
        req = client.recv(BUFSIZE).decode('utf-8')
        # parse req

        reqParse = req.split()
        reqMethod = reqParse[0]
        reqFile = reqParse[1]
        reqUrlParse = reqFile.split('/')

        # GET
        if reqMethod == 'GET':
            if reqFile == '/':
                reqFile = '/index.html'

            sendReply = False
            if reqFile.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if reqFile.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if reqFile.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if reqFile.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if reqFile.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if reqFile.endswith(".mp4"):
                mimetype = 'video/mp4'
                sendReply = True

            if reqUrlParse[1] == 'video':
                # send status
                client.send("HTTP/1.1 200 OK\n")
                # send header
                client.send("Content-Type: video/mp4\n")
                client.send("\n")
                # connect to server
                serclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                serclient.connect((RSERHOST, RSERPORT))
                # fetch file and write it
                myfile = open('video/testfile.mp4', 'w')
                while True:
                    data = serclient.recv(BUFSIZE)
                    if not data: break
                    myfile.write(data)
                myfile.close()
                print 'finished writing file'
                serclient.close()
                # send the file
                file = open('video/testfile.mp4')
                output = file.read()
                file.close()
                for i in range(0, len(output)):
                    client.send(output[i])
                # close()
                client.close()
                address.close()
            elif sendReply:
                # open file and read
                file = open('build'+reqFile)
                output = file.read()
                file.close()

                # send status
                client.send("HTTP/1.1 200 OK\n")
                # send header
                client.send("Content-Type: "+mimetype+"\n")
                client.send("\n")
                # sned body
                for i in range (0, len(output)):
                    client.send(output[i])
                # close()
                client.close()
                address.close()
            else:
                client.send("HTTP/1.1 404 Not Found")
                # close()
                client.close()
                address.close()
        # POST
        elif reqMethod == 'POST':
            if reqFile == '/createVideo':
                bytes = open(videofile).read()
                serclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                serclient.connect((WSERHOST, WSERPORT))
                serclient.send(bytes)
                serclient.close()
            # send status
            client.send("HTTP/1.1 200 OK\n")
            # send header
            client.send("Content-Type: text/plain\n")
            client.send("\n")
            # sned body
            client.send('success')
            # close()
            client.close()
            address.close()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        client.close()
        address.close()
    except:
        print("except")

if __name__ == "__main__":
    CLIHOST, CLIPORT = '', 8080
    WSERHOST, WSERPORT = 'localhost', 5000
    RSERHOST, RSERPORT = 'localhost', 4000
    videofile = "video/Lemon.mp4"

    # socket()
    clis = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clis.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind()
    clis.bind((CLIHOST, CLIPORT))

    # listen()
    clis.listen(10)
    print("The Web Server is running..")
    print("PORT "+str(CLIPORT))

    while(True):
        # accept()
        client, address = clis.accept()
        print(str(address)+" connected")
        threading.Thread(target = listenToClient, args = (client, address)).start()