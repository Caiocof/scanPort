import socket


def scan(host):
    print('Processing...')
    for ports in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if s.connect_ex((host, ports)) == 0:
            print(f'Port {ports} open!')
            s.close()


if __name__ == '__main__':
    host = input('Write host for scan: ')
    scan(host)
