import requests
import sys
import json
import socket


def print_request():
    print()
    print(f"Script name: {sys.argv[0]}")
    print()

    if len(sys.argv) == 1:
        print("Default URI address: https://www.wp.pl")
        request = requests.get('https://www.wp.pl')
    else:
        print(f"URI address: {sys.argv[1]}")
        try:
            request = requests.get(sys.argv[1])
        except Exception:
            print(f"Incorrect URL address: {sys.argv[1]}")
            sys.exit()

    print()
    print(f"Status code: {request.status_code}")
    print()
    print(f"Request time: {request.elapsed}")
    print()
    print(f"Encoding: {request.encoding}")
    print()
    print("Cookies:")

    for key, value in request.cookies.items():
        print(f"{key}:{value}")

    print()
    print("Headers:")

    with open('headers.json') as json_file_headers:
        headers = json.load(json_file_headers)

    for key, value in request.headers.items():
        if key.lower() in headers:
            print(f"{key}:{value}: {headers[key.lower()]}")
        else:
            print(f"{key}:{value}: {headers['unknown']}")

    print()


if __name__ == '__main__':
    print_request()
