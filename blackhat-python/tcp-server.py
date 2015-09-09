import socket
import threading

bind_addr = "0.0.0.0"
bind_port = 3000
bind_tuple = (bind_addr, bind_port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(bind_tuple)

server.listen(5)

print "[*] Listening on %s: %d" % bind_tuple

def handle_client(client):
    request = client.recv(1024)
    print "[*] Received: %s" % request
    client.send("ACK!")
    client.close()

while True:
    client, addr = server.accept()
    print "Client is {}".format(client)
    print "Addr is {}".format(addr)
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    handler = threading.Thread(target=handle_client, args=(client,))
    handler.start()
