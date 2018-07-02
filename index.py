import socket
from streaming_form_data import StreamingFormDataParser
from streaming_form_data.targets import ValueTarget, FileTarget

HOST, PORT = "", 8080

# socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind()
s.bind((HOST, PORT))

# video data
keys = []
urls = []

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
            req = client.recv(4096).decode('utf-8')
            # print(req)
            # parse req
            if not req:
            #     print('send fail******************')
            #     req = client.recv(4096).decode('utf-8')

            # else :
            #     print('send success****************')

            reqParse = req.split()
            reqMethod = reqParse[0]
            reqFile = reqParse[1]

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

                if reqFile.split('/')[1] == 'video':
                    # send status
                    client.send("HTTP/1.1 200 OK\n")
                    # send header
                    client.send("Content-Type: video/mp4\n")
                    client.send("\n")
                    # send body
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
                print(reqFile)
                if reqFile == '/createVideo':
                    names = [n for n in reqParse if n.startswith('name')]
                    blobs = [b for b in reqParse if b.startswith('blob')]
                    print(len(names))
                    print(len(blobs))
                    name = names[0].split('\"')[1]
                    blob = blobs[0]
                    print(name)
                    print(blob)
                    keys.append(name)
                    urls.append(blob)
                    print(keys)
                    print(urls)
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