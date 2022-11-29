import time
import requests
import discord
from dotenv import load_dotenv
import os
load_dotenv()


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
    try:
        url = "https://mpunkspool.com/score.txt"
        request = requests.get(url)
        pings = request.json()['pings']

        my_address = os.getenv("ADDRESS")

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
        time.sleep(600)
    except Exception as e:
        time.sleep(600)
        pass



