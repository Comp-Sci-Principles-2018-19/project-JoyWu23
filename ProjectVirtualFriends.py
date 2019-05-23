print("loading...")
import numpy as np
import pandas as pd
data = pd.read_excel('Data.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
#print(data)
columns = data.columns
#print(data['Questions'].tolist())
#print(len(columns))

print("Your virtual friends are", end=" ")
for (i,v) in enumerate(columns):
    if i>0 and i!=len(columns)-1:
        print(v,end=", ")
    elif i==len(columns)-1:
        print(v,end=".\r")

class Player:
    def __init__(self,name,msgs=""):
        self.name = name
        self.msgs = msgs
        
    #def __str__(self):
    #    return "player: {0}".format(self.name)
    

class Friend:
    def __init__(self,name,responses=[]):
        self.name = name
        self.rsp = responses
    #def __str__(self):
    #    return "friend {0}".format(self.name)

player = Player(input("What's your name? "))
#print(player)
friends = []
numfriends = int(input("How many virtual friends do you want? "))
for i in range(numfriends):
    friend = input("What's your virtual friend {0}'s name? ".format(i+1))
    if friend not in columns:
        friends.append(friend)
        column = [friend]
        data[friend] = 'default'
        data.to_excel('Data.xlsx', index = False, sheet_name='Sheet1')
    #print(friend)
#print(friend, ": ", end="")
#you = input("Hi, what's your name?")
inputs = []
replies = []
while True:
    msg = input("You: ")
    #for i in data.index.values:
     #   if i == msg:
      #      print(msg)
    if msg not in data['Questions'].tolist():
        #newrow = pd.DataFrame({'Questions':[]})
        #data.append(newrow)
        #print(data)
        data.loc[len(data)]=[msg]+["default"]*(len(columns)-1)
        data.to_excel('Data.xlsx', index = False, sheet_name='Sheet1')
        print(friend, end = ": ")
        #reply = input()
        data[friend][len(data)-1] = input()
        data.to_excel('Data.xlsx', index = False, sheet_name='Sheet1')
    for (i,q) in enumerate(data['Questions'].tolist()):
        if msg == q:
            print(friend,":", data[friend].tolist()[i])
            if data[friend].tolist()[i] == 'default' or data[friend].tolist()[i] == '':
                print(friend,end = ": ")
                data[friend][i] = input()
                data.to_excel('Data.xlsx', index = False, sheet_name='Sheet1')
                break