# Программа клиента, передающего серверу сообщения при каждом запросе на соединение
from socket import *

with socket(AF_INET, SOCK_DGRAM) as s:        # Определяем UDP-протокол
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while True:
        msg = 'Запрос на соединение!'
        s.sendto(msg.encode('utf-8'), ("127.0.0.1", 8888))