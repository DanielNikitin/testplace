import pygame
from network import Network
from hud import *

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

pygame.init()

def redrawWindow(players, trees, ores, traps,
                 info_data, other_data, hp_data):

    screen.fill('gray25')

    for player in players:
        player.draw(screen)
        draw_huds(screen, info_data, other_data, hp_data)

    for tree in trees:
        tree.draw(screen)

    for ore in ores:
        ore.draw(screen)

    for trap in traps:
        trap.draw(screen)

    pygame.display.update()

def main():
    run = True

# -------- CLIENT KEY CONDITIONS
    client_up = False  # W
    client_left = False  # A
    client_down = False  # S
    client_right = False  # D
    client_crouch = False  # C

    server = Network()
    conn_status = server.connect()

    try:
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)

            data = server.send({"dev_data": conn_status})  # send and reply

            if data is not None:
                (players, trees, ores, traps,
                 info_data, other_data, hp_data) = data
                #print(f"GET DATA :: {data}")

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

                    # -------- KEYDOWN
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:  # W
                            print("w is pressed")
                            client_up = True
                        if event.key == pygame.K_a:  # A
                            print("a is pressed")
                            client_left = True
                        if event.key == pygame.K_s:  # S
                            print("s is pressed")
                            client_down = True
                        if event.key == pygame.K_d:  # D
                            print("d is pressed")
                            client_right = True
                        if event.key == pygame.K_c:  # C
                            print("c is pressed")
                            client_crouch = True

                        if event.key == pygame.K_g:
                            print('change_text')
                            server.send({"client_hud": "change_text"})


                    # -------- KEYUP
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:  # W
                            print("w is unpressed")
                            client_up = False
                        if event.key == pygame.K_a:  # A
                            print("a is unpressed")
                            client_left = False
                        if event.key == pygame.K_s:  # S
                            print("s is unpressed")
                            client_down = False
                        if event.key == pygame.K_d:  # D
                            print("d is unpressed")
                            client_right = False
                        if event.key == pygame.K_c:  # C
                            print("c is unpressed")
                            client_crouch = False

                # -------- SENDING TO SERVER
                if client_up:
                    server.send({"client_action": "move", "direction": "Up"})  # W
                if client_left:
                    server.send({"client_action": "move", "direction": "Left"})  # A
                if client_down:
                    server.send({"client_action": "move", "direction": "Down"})  # S
                if client_right:
                    server.send({"client_action": "move", "direction": "Right"})  # D
                if client_crouch:
                    server.send({"client_action": "mode", "position": "Crouch"})  # C


                redrawWindow(players, trees, ores, traps,
                             info_data, other_data, hp_data)

    except Exception as e:
        print(f"Client Error :: {e}")

main()
