#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from .request import Request
from .response import handle_request, bad_request

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
            request = Request(connection.recv(2048).decode())
        except Exception as ex:
            connection.send(bad_request().encode())
            print('Failed to handle request:', ex)
        else:
            connection.send(handle_request(request).encode())
        finally:
            connection.close()

if __name__ == '__main__':
    main()
