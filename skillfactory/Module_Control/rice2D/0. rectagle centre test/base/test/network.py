import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 10000
        self.addr = (self.server, self.port)
        self.server_bridge = self.conn_load_data()
        print(f"Server Bridge :: {self.server_bridge}")


    def get_data(self):  # получаем дату от сервера
        return self.server_bridge  # через функцию connect


#   ----------- CONNECT / LOAD DATA -----------
    def conn_load_data(self):  #  устанавливает соединение с сервером
        try:
            self.client.connect(self.addr)  # подключаемся к серверу
            print(self.addr)
            return pickle.loads(self.client.recv(2048)) # получаем данные клиента
        except socket.error:
            self.client.close()
            print("** SERVER IS SHUTTED DOWN **")

#   -------- SEND DATA
    def send_data(self, rec_data):
        try:
            print(f"Sending to server :: {rec_data}")
            self.client.send(pickle.dumps(rec_data))
            return  # Убираем попытку получения ответа
        except socket.error as e:
            print(e)
#   --------------------------------------

    # pickle dumps преобразовать в байты для отправки
    # pickle loads получить байты и преобразовать в нормальный вид
    # trees = loaded_data.get("trees", []) - залить дату в переменную