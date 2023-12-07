import random

from player import *
from cube import *

#  Кортеж для хранения игроков
players_list = {}

# Кортеж для хранения кубов
cubes_list = []

# Список имён
names_list = ["DDFan", "Bob", "typesen", "kotik", "pups", "Bob2"]

def player_respawn(_id):  # создаем персонажа и спавним его в мире
    x, y = 50, 50
    width = 50
    height = 60
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    name = random.choice(names_list)

    return Player(x, y, width, height, color, name, _id)  # получаем все данные после респавна

def cube_respawn():  # создаем кубик и спавним его в мире
    x, y = 100, 100
    width = 20
    height = 20
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    return Cube(x, y, width, height, color)  # получаем все данные после спавна