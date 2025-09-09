import socket

Host = '127.0.0.1'
Port = 50007


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, Port))
        s.sendall(b'hello world')
        data = s.recv(1024)
    print('Received', repr(data))


if __name__ == '__main__':
    main()
