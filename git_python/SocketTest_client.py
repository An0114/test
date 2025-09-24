import socket

Host = '127.0.0.1'
Port = 50007


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, Port))
        msg = 'Hello World!'
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
    print('Received', repr(data.decode('utf-8')))


if __name__ == '__main__':
    main()
