import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 3000))
client.send("HELLO")

print "{}".format(client.recv(4096))
