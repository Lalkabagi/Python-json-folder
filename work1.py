import os
import json

with open("data.json", "r", encoding="UTF-8") as f:
    text = json.load(f)

index1 = 0
index2 = 0

for i in range(len(text)):
    y = text[index1]
    index1 += 1
    print("Player : {0} \n" "Games : {1} \n" "Wins : {2}\n".format(y[0],y[1],y[2]))