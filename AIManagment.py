import GameRunner
import AINetworking
import random
import json
import os

#settings
totalBots = 64
evoFactor = .5

# usefull methods

def GenNetwork():
    weights1 = [round(random.randint(-20,20)/20.0 * .1,5) for i in range(16)]
    weights2 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]
    weights3 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]
    weights4 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]

    return AINetworking.Network(weights1,weights2,weights3,weights4)

# Loading from the JSON

allNetworks = [GenNetwork() for i in range(totalBots)]

#Runner Code starts Here

running = True

while running:
    results = GameRunner.AIGame(allNetworks) # put all newtworks inside the game, get a list of tuples that each have 0 for the network, and 1 for the score index
    if(results == "STOP"):
        running = False
        break

    results = sorted(results)
    #print([result.score for result in results])
    
    halfNetworks = results[:int(totalBots * evoFactor)]
    #print([result.score for result in halfNetworks])
    newNetworks = []
    for parent in halfNetworks:
        weights1 = [w - (random.uniform(-1, 1) * evoFactor) for w in parent.weights1]
        weights2 = [w - (random.uniform(-1, 1) * evoFactor) for w in parent.weights2]
        weights3 = [w - (random.uniform(-1, 1) * evoFactor) for w in parent.weights3]
        weights4 = [w - (random.uniform(-1, 1) * evoFactor) for w in parent.weights4]
        newNetwork = AINetworking.Network(weights1, weights2, weights3, weights4)
        newNetworks.append(newNetwork)

    allNetworks = halfNetworks + newNetworks

