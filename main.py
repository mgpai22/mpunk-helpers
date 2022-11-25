import math
import time

import requests
import json

import discord


class Miner:
    def __init__(self, address, score):
        self.address = address
        self.score = score

    def print(self):
        return {'address': self.address, 'score': self.score}


class Scores:
    def __init__(self, pings):
        self.pings = pings
        self.arr = []
        for x in pings:
            self.arr.append(Miner(x, pings[x]))

    def sort(self):
        self.arr.sort(key=lambda i: i.score, reverse=True)


while True:

    url = "https://mpunkspool.com/score.txt"
    request = requests.get(url)

    pings = request.json()['pings']

    my_address = "0x18ed95e4039ebcfE720a870Ede6E02789BBa427b"

    obj = Scores(pings)
    obj.sort()
    counter = 0
    score = 0
    for x in obj.arr:
        counter += 1
        if x.print()['address'] == my_address:
            score = x.print()['score']
            break
            # print("score:", x.print()['score'])
            # print("line position:", counter)

    print("score:", score)
    print("line position:", counter)
    discord.discordCall(counter, round(score))
    time.sleep(60)
