import socket

Host = ''
port = 50007


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('connected by :', addr)
            # print(s.getpeername())
            print(s.getsockname())
            print(s.gettimeout())
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


if __name__ == '__main__':
    main()
