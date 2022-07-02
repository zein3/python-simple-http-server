#!/usr/bin/env python3

import os
from datetime import datetime
from pathlib import Path
from .request import Request


def base_request() -> str:
    msg = ''
    msg += 'Connection: close\r\n'
    msg += f'Date: { datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT") }\r\n'
    msg += 'Server: Custom\r\n'
    return msg

def bad_request() -> str:
    msg = "HTTP/1.1 400 Bad Request\r\n" + base_request()
    return msg

def handle_request(request: Request) -> str:
    filename = request.get_url()[1:]
    if filename == '':
        filename = 'index.html'

    print(filename)
    path = Path(filename)
    if path.is_file():
        msg = "HTTP/1.1 200 OK\r\n" + base_request()
        msg += f"Last-Modified: {os.path.getmtime(path)}\r\n"
        msg += f"Content-Length: {os.path.getsize(path)}\r\n"
        msg += "Content-Type: text/html\r\n" # TODO determine content type based on file extension
        
        msg += "\r\n"
        
        with open(path, "r") as f:
            for line in f:
                msg += line

        return msg
    else:
        return "HTTP/1.1 404 Not Found\r\n" + base_request()

