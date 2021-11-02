# Программа вывода сообщений на стороне сервера при запросе от клиента
from socket import *
with socket(AF_INET, SOCK_DGRAM) as s:        # Определяем UDP-протокол
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Несколько приложений может слушать сокет
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) # Определяем широковещательные пакеты
    s.bind(('', 8888))

    while True:
        msg = s.recv(128)
        print(msg.decode('utf-8'))