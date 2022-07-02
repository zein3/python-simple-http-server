#!/usr/bin/env python3

class Request:
    def __init__(self, req: str):
        request_line, *header_lines = req.split('\r\n')

        # parse request line
        self.method, self.url, self.version = request_line.split(' ')

        # parse header lines
        self.headers = dict()
        for line in header_lines:
            if line.strip() != '':
                key, val = line.split(': ')
                self.headers[key] = val

    def get_method(self) -> str:
        return self.method

    def get_url(self) -> str:
        return self.url

    def get_version(self) -> str:
        return self.version

    def get_header(self, header: str) -> str:
        if header in self.headers:
            return self.headers[header]
        else:
            return ''

    def __str__(self) -> str:
        representation = f'Method: {self.method}\n'
        representation += f'URL: {self.url}\n'
        representation += f'Version: {self.version}\n'
        return representation
