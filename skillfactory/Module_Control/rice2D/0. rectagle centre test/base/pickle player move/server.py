import socket
import pickle

from _thread import *
from server_func import *

from player import Player

server_ip = "localhost"
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

try:
    s.bind((server_ip, port))
except socket.error as e:
    print(str(e))


s.listen(5)
print("SERVER STARTED")

spawn_tree()
spawn_ore()

def threaded_client(conn, player):
    # отправляем данные клиенту об этом
    conn.send(pickle.dumps({"trees": tree_list, "ores": ore_list, "players": player_respawn(player)}))

    while True:
        try:
            rec_data = conn.recv(2048)  # получили байты
            loaded_data = pickle.loads(rec_data)  # переводим в нормальный текст
            player_list[player] = player_data

            if not rec_data:
                print("Disconnected")
                break
            else:

                print("Received: ", rec_data)
                print("Sending : ", (tree_list, ore_list, player_list))
                player_data = list(player_list.values())

            conn.sendall(pickle.dumps((tree_list, ore_list)))

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected:", addr)

    # Assuming you have a player instance here, replace it with your actual Player creation logic
    current_player = Player(0, 0, 50, 50, (255, 0, 0), 1)

    start_new_thread(threaded_client, (conn, current_player))