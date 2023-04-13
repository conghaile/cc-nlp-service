import json
import re
import requests

class Thread:
    def __init__(self, thread):
        self.thread = thread

    def analyze(self, model): 
        for post in self.thread.keys():
            self.thread[post]['time'] = str(int(self.thread[post]['time']) / 1000)
            self.thread[post]['coins'] = []
            sentences = [sen for sen in re.split(r"^>>\d{,}|[.?!]\s|\n", self.thread[post]["text"]) if len(sen) > 0]
            for sen in sentences:
                possibleCoins = [*set([str(coin) for coin in list(model(sen).ents)])]
                if len(possibleCoins) > 0:
                    for coin in possibleCoins:
                        if len(coin) > 1:
                            self.thread[post]['coins'].append(coin)
                    self.thread[post]['coins'] = [*set(self.thread[post]['coins'])]
                    print(self.thread[post]['coins'])

                            # try:
                            #     realCoin = requests.get(f"http://localhost:5002/search/?coin={coin}").json()
                            #     print(realCoin)
                            #     # if realCoin["Real coin"] != "Not found":
                            #     #     self.thread[post]['coins'].append(realCoin["Real coin"])
                            # except requests.exceptions.Timeout:
                            #     print("Timeout")
                            # except requests.exceptions.RequestException as e:
                            #     print(e)
        return "Done."
    
    # def saveToDB(self):
    #     for post in self.thread.keys():
    #         time = self.thread[post]['time']
    #         if len(self.thread[post]['coins']) > 0:
    #             for coin in self.thread[post]['coins']:
    #                 print([post, time, coin])
    