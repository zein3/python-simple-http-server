#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from . import request

PORT = 8080


def main():
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(('', PORT))
        server.listen(1)
    except Exception as ex:
        print('Cannot run server:', ex)
        return

    print(f'Listening on port {PORT}')
    while True:
        connection, _ = server.accept()
        try:
            req = request.Request(connection.recv(2048).decode())
        except Exception as ex:
            connection.send('Fail!'.encode())
            print('Fail to handle request:', ex)
        else:
            connection.send('OK!'.encode())
        finally:
            connection.close()

if __name__ == '__main__':
    main()
