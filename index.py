import socket

HOST, PORT = "", 8080

# socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind()
s.bind((HOST, PORT))

while(True):
    # listen()
    s.listen(10)
    print("The Web Server is running..")
    print("PORT "+str(PORT))

    while(True):
        # accept()
        client, address = s.accept()
        print(str(address)+" connected")

        try:
            # send() + recv()
            request = client.recv(1024).decode('utf-8')
            # print(request)
            
            reqFile = request.split()[1];
            print(reqFile)
            if reqFile == '/':
                reqFile = '/index.html'
            print(reqFile)

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

            print(sendReply)

            if sendReply:
                print('check')
                file = open('build'+reqFile)
                # file = open('build'+reqFile)
                output = file.read()
                file.close()

                client.send("HTTP/1.1 200 OK\n")
                client.send("Content-Type: "+mimetype+"\n")
                client.send("\n")
                for i in range (0, len(output)):
                    client.send(output[i])

            else:
                client.send("HTTP/1.1 404 Not Found")
                # close()
                client.close()
                address.close()
        except KeyboardInterrupt:
            print '^C received, shutting down the web server'
            client.close()
            address.close()
        except:
            print("except")