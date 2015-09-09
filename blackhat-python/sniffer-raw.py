import os
import socket

host = "192.168.0.22"

socket_proto = socket.IPPROTO_IP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW)

sniffer.bind((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, socket_proto)

try:
    while True:
        data, (addr, port) = sniffer.recvfrom(65565)
        print "+{}+".format(50*'-')
        print "From {}:{}".format(addr, port)
        print "DATA: {}".format(data)
        print
        print "HEX: {}".format(":".join('\\x' + c.encode('hex') for c in data))
except KeyboardInterrupt:
    print "Stopping.."

