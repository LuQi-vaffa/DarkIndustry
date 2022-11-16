import socket

def getIP(domain):
    myaddr = socket.getaddrinfo(domain, 'http')
    return myaddr[0][4][0]



ip = getIP("www.douban.com")
print(ip)