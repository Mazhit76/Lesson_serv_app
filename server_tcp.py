# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата.
# Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
# Функции клиента:
# сформировать presence-сообщение;
# отправить сообщение серверу;
# получить ответ сервера;
# разобрать сообщение сервера;
# параметры командной строки скрипта client.py <addr> [<port>]:
# addr — ip-адрес сервера;
# port — tcp-порт на сервере, по умолчанию 7777.
# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> — TCP-порт для работы (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

# Программа сервера для получения приветствия отклиента

from socket import *
import time, click, json

@click.command()
@click.option('--adress', default ='', help='ip adress')
@click.option('--port', default ='7777')  # prompt='Enter port'
def server_tcp(adress, port, user={}):
    user = {
        "C0deMaver1ck": {"password": "CorrectHorseBatterStaple",
                         "time_authenticate": ''}
    }
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((adress, int(port)))
        s.listen(5)



        while True:
            client, addr = s.accept()
            timestr = time.ctime(time.time())
            data_out = {}
            # Блок принятия и парсинга сообщений

            data_b = client.recv(1000000)
            data_in = json.loads(data_b)
            msg_dict = data_in.pop(0)

            # Блок проверки 'action'
            if 'action' in msg_dict:

                # Блок проверки сообщения клиента о связи
                if msg_dict.get('action') =='presence':
                    print(msg_dict)
                #     # Блок проверки наличия пользователя
                #     #Это данные из сообщения
                #     msg_user = msg_dict.get('user')
                #     msg_account_name = msg_user.get('account_name')


                # Блок Авторизация
                if msg_dict.get('action') =='authenticate':
                    # Блок проверки наличия пользователя и пароля
                    #Это данные из сообщения
                    msg_user = msg_dict.get('user')
                    msg_account_name = msg_user.get('account_name')
                    msg_password = msg_user.get('password')


                    # Ищем пользователя и проверяем пароли
                    if msg_account_name in user:

                        # Это данные из словаря сервера
                        user_data = user.get(msg_account_name)
                        user_password = user_data.get('password')


                        # Проверка пароля и заполнение данных с ответом
                        if msg_password == user_password:
                            print('пароль совпал')
                            # записываем время авторизации в базу пользователя
                            user_data['time_authenticate'] = timestr
                            data_out = {
                                "response": '200',
                                "alert": 'Авторизован',
                                "time_authenticate": user_data['time_authenticate']
                            }

                        else:
                            print('пароль не совпал')
                            data_out = {
                                "response": '402',
                                "alert": 'Неверный пароль',
                                "time": timestr
                            }
                    else:
                        print('пользователь не найден')
                        data_out = {
                            "response": '401',
                            "alert": 'Пользователь не авторизован',
                            "time": timestr
                        }


            # блок отправки сообщений

            msg = []
            msg.append(data_out)
            msg_json = json.dumps(msg, sort_keys=True, indent=4)
            client.send(msg_json.encode('utf-8'))

            client.close()
if __name__=='__main__':
    server_tcp()


