import numpy as np
import pandas as pd
data = pd.read_excel('Data.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(data)
columns = data.columns
print(len(columns))
class Player:
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return "player {0}".format(self.name)
    

class Friend:
    def __init__(self,name,responses=[]):
        self.name = name
        self.rsp = responses
    def __str__(self):
        return "friend {0}".format(self.name)


player = Player(input("What's your name?"))
print(player)
friends = []
numfriends = int(input("How many friends do you want?"))
for i in range(numfriends):
    friend = Friend(input("What's your number{0} virtual friend's name? ".format(i+1)))
    friends.append(friend)
    print(friend)
#print(friend, ": ", end="")
#you = input("Hi, what's your name?")
inputs = []
replies = []
inputs.append(input("You: "))