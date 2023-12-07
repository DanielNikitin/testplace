import socket
import pickle

from _thread import *

from server_config import *
from server_func import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)


try:
    s.bind((server_ip, port))
except socket.error as e:
    print(str(e))

s.listen(24)
print("SERVER STARTED")


def threaded_client(conn, player, cube):  # Ожидание подключения клиентов
    conn.send(pickle.dumps((player_respawn(player), cube_respawn())))  # Клиенту отправляется начальное состояние игрока через pickle

    while True:  # Сервер ожидает и принимает данные от клиента,
        # обновляет состояние игрока и отправляет обновленные данные всем клиентам
        try:
            data = pickle.loads(conn.recv(2048))  # получаем данные от клиента которые уже сериализованны pickle

            players_list[player] = data[0]  # записываем состояние игрока в player
            print(data)

            cubes_list[cube] = data[1]
            print(data)

            if not data:
                print(f"NOT DATA, DISCONNECTED: {player}")
                break
            else:
                # Отправляем обновленные данные всем клиентам
                reply = list(players_list.values()), list(cubes_list.values())
                conn.sendall(pickle.dumps(reply))

        except:
            break

    print(f"Disconnected: {player}")
    #del players_list[player]  # удаляем игрока из мира
    #players_list[player].status = "sleep"  # Устанавливаем статус "sleep"

    conn.close()

currentPlayer = 0
cube_count = 0
while True:  # ожидаем желаемых для подключения к серверу
    conn, addr = s.accept()  # принимаем их запрос на подключение
    print(f"Connected: {addr}")

    # Запускаем новый поток для каждого клиента
    start_new_thread(threaded_client, (conn, currentPlayer, cube_respawn()))

    # Увеличиваем счетчик для следующего игрока
    currentPlayer += 1
    cube_count += 1
