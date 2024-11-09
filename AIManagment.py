import GameRunner
import AINetworking
import random
import json
import os
import csv
#settings
totalBots = 64
evoFactor = .9



# usefull methods

def GenNetwork():
    weights1 = [round(random.randint(-20,20)/20.0 * .1,5) for i in range(16)]
    weights2 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]
    weights3 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]
    weights4 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]

    return AINetworking.Network(weights1,weights2,weights3,weights4)

def saveData(fName,networks):
    with open (fName,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for network in networks:
            writer.writerow([[writer.writerow(weight for weight in network.weights1)],
                            [writer.writerow(weight for weight in network.weights2)],
                            [writer.writerow(weight for weight in network.weights3)],
                            [writer.writerow(weight for weight in network.weights4)]])

def loadData(fName):
    returnList = []
    with open(fName, newline='' ) as cvsfile:
        reader = csv.reader(cvsfile)
        for i in range(64):
            weights1 = next(reader)
            for i in range(len(weights1)):
                weights1[i] = float(weights1[i])
            weights2 = next(reader)
            for i in range(len(weights2)):
                weights2[i] = float(weights2[i])
            weights3 = next(reader)
            for i in range(len(weights3)):
                weights3[i] = float(weights3[i])
            weights4 = next(reader)
            for i in range(len(weights4)):
                weights4[i] = float(weights4[i])
            returnList.append(AINetworking.Network(weights1,weights2,weights3,weights4))
            next(reader)
    return returnList

allNetworks = []
try :
    allNetworks = loadData("savedNetworks.csv")
    print(allNetworks[0].weights1)
except:
    allNetworks = [GenNetwork() for i in range(totalBots)]

#Runner Code starts Here

running = True

while running:
    results = GameRunner.AIGame(allNetworks) # put all newtworks inside the game, get a list of tuples that each have 0 for the network, and 1 for the score index
    if(results == "STOP"):
        running = False
        saveData("savedNetworks.csv",allNetworks)
        break

    results = sorted(results)
    #print([result.score for result in results])
    
    halfNetworks = results[:int(totalBots/2)]
    #print([result.score for result in halfNetworks])
    newNetworks = []
    for i in range(int(totalBots/2)):
        weights1 = [(halfNetworks[i].weights1[j] - ((random.random()- .5) * evoFactor)) for j in range(8)]
        weights2 = [(halfNetworks[i].weights1[j] - ((random.random() - .5) * evoFactor)) for j in range(8)]
        weights3 = [(halfNetworks[i].weights1[j] - ((random.random() - .5) * evoFactor)) for j in range(8)]
        weights4 = [(halfNetworks[i].weights1[j] - ((random.random() - .5) * evoFactor)) for j in range(8)]
        newNetwork = AINetworking.Network(weights1,weights2,weights3,weights4)
        halfNetworks.append(newNetwork)

    allNetworks = halfNetworks + newNetworks
    print(len(allNetworks))

