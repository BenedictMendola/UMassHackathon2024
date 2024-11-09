import math
import VectorMath



def makeItTo0TO1(x): return 1/(1 + pow(math.e,-x))

def isInBounds(point:VectorMath.Vector3,barriers):
    for barrier in barriers:
        barrierHalfWidth = barrier.sr.surface.get_width() /2 * barrier.transform.scale.x
        barrier2HalfHeight = barrier.sr.surface.get_height() /2 * barrier.transform.scale.y
        barrierPos = barrier.transform.position
        if((barrierPos.y - barrier2HalfHeight <point.y < barrierPos.y + barrier2HalfHeight) and (barrierPos.x - barrierHalfWidth < point.x < barrierPos.x +barrierHalfWidth)):
            return True
    return False

class Network():
    
    def __lt__(self,other):
        return self.score < other.score

    def __init__(self, weightsRow1,weightsRow2,weightsRow3,WeightsRow4,score = 0): # lowest score is best
        self.weights1 = weightsRow1
        self.weights2 = weightsRow2
        self.weights3 = weightsRow3
        self.weights4 = WeightsRow4
        self.score = score
    def setScore(self,positon):
        self.score += math.sqrt(pow(1280-positon.x,2)+ pow(720-positon.y,2))
    
    def getInputs(position: VectorMath.Vector3,gameObjects,velocity=VectorMath.Vector3(0,0,0)): #Idea, have a point go out until it is within a colider -  checks what is the closes barrier and what type for all directins
        barriers = [ob for ob in gameObjects if ob.name != 'Player']
        cursor = VectorMath.Vector3(position.x,position.y,0)
        #right
        #print(cursor.y)
        while(not isInBounds(cursor,barriers)):
            cursor.x += 15
        right = cursor.x -position.x
        cursor = VectorMath.Vector3(position.x,position.y,position.z)
        while(not isInBounds(cursor,barriers)):
            cursor.x -= 15
        left =position.x - cursor.x
        cursor = VectorMath.Vector3(position.x,position.y,position.z)
        while(not isInBounds(cursor,barriers)):
            cursor.y -= 15
        up = position.y - cursor.y
        cursor = VectorMath.Vector3(position.x,position.y,position.z)
        while(not isInBounds(cursor,barriers)):
            cursor.y += 15
        down = cursor.y - position.y
        cursor = VectorMath.Vector3(position.x,position.y,position.z)
        #print([makeItTo0TO1(right/1000),makeItTo0TO1(left/1000),makeItTo0TO1(up/1000),makeItTo0TO1(down/1000)])
        

        return (makeItTo0TO1(right/1000),makeItTo0TO1(left/1000),makeItTo0TO1(up/1000),makeItTo0TO1(down/1000),velocity.normalized().x,velocity.normalized().y,
                makeItTo0TO1(position.x),makeItTo0TO1(position.y))
            


    def weightedSumForAllOfWeight(inputs:list,weight:float):
        sumOfWeights = sum([(value * weight) for value in inputs])
        return makeItTo0TO1(sumOfWeights)


    def calculateInput(self,inputs) -> float: #gives a float beetween 0 and 1, each input is the distance to the nearest wall, or (0 = up killbox,.33 = right,.66 =down, 1 = left) 0 = normal wall
        readyForRow2Inputs = [Network.weightedSumForAllOfWeight(inputs,weight) for weight in self.weights1]
        readyForRow3Inputs = [Network.weightedSumForAllOfWeight(readyForRow2Inputs,weight) for weight in self.weights2]
        readyForRow4Inputs = [Network.weightedSumForAllOfWeight(readyForRow3Inputs,weight) for weight in self.weights3]
        #finalValue = [Network.weightedSumForAllOfWeight(readyForRow4Inputs,weight) for weight in self.weights4]
        #print(sum(readyForRow3Inputs))
        #print(sum(finalValue))
        return (sum(readyForRow4Inputs))
    
    def to_dict(self):
        return {
            'weights1': self.weights1,
            'weights2': self.weights2,
            'weights3': self.weights3,
            'weights4': self.weights4,
        }

    @staticmethod
    def from_dict(data):
        return Network(
            data['weights1'],
            data['weights2'],
            data['weights3'],
            data['weights4'],
        )
    
#def choose(dir)
