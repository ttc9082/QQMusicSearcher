# Created by TTc9082 on 6/20/16
import socket
import time


def interact(sock):
    command = ''
    while command != 'exit':
        command = raw_input('$ ')
        sock.send(command + '\n')
        time.sleep(.5)
        print sock.recv(0x10000)
    return


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9999))
    s.listen(5)
    interact(s.accept()[0])
