# -*- coding:utf-8 -*-

import socket





def handle_request(client):
    buf = client.recv(1024)
    print(buf.decode("utf8"))
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    with open('index.html','rb') as f:
        date=f.read()
    client.send(date)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':

    main()