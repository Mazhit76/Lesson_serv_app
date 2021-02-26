from socket import *
import time, click, json
@click.command()
@click.option('--adress', default ='localhost', help='ip adress')
@click.option('--port', default ='7777')   # prompt='Enter port'
def client_tcp(adress, port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((adress, int(port)))


        c_time = time.ctime(time.time())+"\n"
        data = []

        user = {
            "account_name": "C0deMaver1ck",
            "password": "CorrectHorseBatterStaple",
            "time_authenticate": ''
        }

        msg = {
            "action": "authenticate",
            "time": c_time,
            "user": {
                "account_name": user.get('account_name'),
                "password": user.get('password'),
                "time_authenticate": user.get('time_authenticate')
            }
        }

        # Блок отправки сообщений
        msg_out(data, msg, s)

        # Блок получения и парсинга сообщений

        data_json = s.recv(1000000)
        data = json.loads(data_json)
        # print(data)
        # Если получен овет от сервера о статус 200 то
        # сообщаем что мы на линии и записываем время авторизации для того
        # чтобы подтверждать что это мы на линии и уже авторизованны
        data_in = data.pop(0)
        print(data_in)
        if 'response' in data_in:
            if data_in.get('response') =='200':
                user['time_authenticate'] = data_in['time_authenticate']
                presence = {
                    "action": "presence",
                    "time": c_time,
                    "type": "status",
                    "user": {
                        "account_name": user.get('account_name'),
                        "status": "Yep, I am here!",
                        "time_authenticate": user.get('time_authenticate')
                    }
                }
                msg_out(data, presence, s)
        s.close()
# Функция на входе принимает
# 1.список, 2. словарь к отправке, 3. соккет по которому работает
def msg_out(data, msg, s):
    data.append(msg)
    msg_json = json.dumps(data, sort_keys=True, indent=4)
    s.send(msg_json.encode('utf-8'))
    data = []
    print(msg_json)

if __name__=='__main__':
    client_tcp()