import GameRunner
import AINetworking
import random

#settings
totalBots = 64
evoFactor = .3

# usefull methods

def GenNetwork():
    weights1 = [round(random.randint(-20,20)/20.0 * .1,5) for i in range(16)]
    weights2 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]
    weights3 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]
    weights4 = [round(random.randint(-20,20)/20.0* .1,5) for i in range(16)]

    return AINetworking.Network(weights1,weights2,weights3,weights4)




#Runner Code starts Here

allNetworks = [GenNetwork() for i in range(int(totalBots))]
running = True

while running:
    results = GameRunner.AIGame(allNetworks) # put all newtworks inside the game, get a list of tuples that each have 0 for the network, and 1 for the score index
    if(results == "STOP"):
        running = False
        break

    results = sorted(results)
    #print([result.score for result in results])
    
    halfNetworks = results[:int(totalBots/2)]
    #print([result.score for result in halfNetworks])
    for i in range(int(totalBots/2)):
        weights1 = [(halfNetworks[i].weights1[j] - (random.randint(-20,20)/20.0 * evoFactor)) for j in range(8)]
        weights2 = [(halfNetworks[i].weights1[j] - (random.randint(-20,20)/20.0 * evoFactor)) for j in range(8)]
        weights3 = [(halfNetworks[i].weights1[j] - (random.randint(-20,20)/20.0 * evoFactor)) for j in range(8)]
        weights4 = [(halfNetworks[i].weights1[j] - (random.randint(-20,20)/20.0 * evoFactor)) for j in range(8)]

        newNetwork = AINetworking.Network(weights1,weights2,weights3,weights4)
        halfNetworks.append(newNetwork)

    
    