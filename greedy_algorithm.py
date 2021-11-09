
import copy
"""
the moving company needs to move the furnitures from one home to the other. the 
moving company are paid by the hour and has a limited weight capacity per trip.
what is the most efficient trip that can make the bang of their buck for their
hourly service while transfering the most valued possessions

"""
class Item(object):
    def __init__(self, name, weight, value):
            self.name = name
            self.weight = weight
            self.value = value

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def __str__(self):
        return "{}".format(self.getName())
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        if isinstance(other, Item):
            if self.name == other.name and \
                self.value == other.value and \
                self.weight == other.weight:
                return True
        return False
def generateItems():
    # items = [
    #     {
    #         "name": "sofa",
    #         "weight": 85,
    #         "value": 9,
    #     },
    #     {
    #         "name": "bed frame",
    #         "weight": 90,
    #         "value": 10,
    #     },
    #     {
    #         "name": "cabinet",
    #         "weight": 90,
    #         "value": 7,
    #     },
    #     {
    #         "name": "kitchen table",
    #         "weight": 75,
    #         "value": 7,
    #     },
    #     {
    #         "name": "office desk",
    #         "weight": 25,
    #         "value": 5,
    #     },
    #     {
    #         "name": "book shelf",
    #         "weight": 10,
    #         "value": 3,
    #     },
    #     {
    #         "name": "painting",
    #         "weight": 2,
    #         "value": 9,
    #     },
    # ]
    items = [
        {
            "name": "sofa",
            "weight": 85,
            "value": 9,
        },
        {
            "name": "painting",
            "weight": 2,
            "value": 9,
        },
    ]
    result = []
    for item in items:
        result.append(Item(item["name"], item["weight"], item["value"]))
    return result

def greedy(items, limit, keyFunction):
    '''
    returns the items to be that will provide the most value while at the same
    time is withing the limit
    '''
    sortedItems = sorted(items, key = keyFunction, reverse = True)
    result = []
    runningLimit = 0
    runningValue = 0
    for item in sortedItems:
        if runningLimit + item.getWeight() <= limit:
            result.append(item)
            runningValue += item.getValue()
            runningLimit += item.getWeight()
    return (runningValue, result)

def greedyTrips(items, limit, keyFunction):
    '''
    returns a list of lists of the most efficient trips in applying greedy
    '''
    itemCopy = items[:]

    result = []
    while len(itemCopy) > 0:
        trip = greedy(itemCopy, limit, keyFunction)
        tripItems = trip[1]
        result.append(tripItems)
        for tripItem in tripItems:
            for index in range(len(itemCopy)):
                if tripItem == itemCopy[index]:
                    del itemCopy[index]
                    break
    return result

def getPowerSet(items):
    #create a new list and add an empty list in the beginning
    powerSet = []
    powerSet.append([])
    for item in items:
        print("item "+ str(item))
        print("current powerset "+ str(powerSet))
        copyPowerSet = copy.deepcopy(powerSet)
        for set in copyPowerSet:
            set.append(item)
        print("current copy "+ str(copyPowerSet))
        powerSet = powerSet + copyPowerSet
        print("set after "+ str(powerSet))
    return powerSet

def bruteForce(items, limit, keyFunction):
    itemCopy = items[:]



def byValue(item):
    return item.getValue()
def byDensity(item):
    return item.getValue()/item.getWeight()

items = generateItems()
limit = 100
# greedyResult = greedyTrips(items, limit, byValue)
result = getPowerSet(items)
print(result)