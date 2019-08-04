import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Insert the URL desiderable: ')
for line in host:
    url = host.split('/')
try:
    mysock.connect((url[2], 80))
    cmd = ('GET '+ host +' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

except:
    print('Invalid URL')
mysock.close()
