import numpy as np
from numpy.lib.npyio import load
import pandas as pd
import random


def getIndexes(data,query):
    '''
    Get all index of an interable equal to "query". Returns generator
    '''
    for i,d in enumerate(data):
        if d == query:
            yield i

def loadData(path):
    '''
    Load the cities and distances from a csv file
    '''
    csv = np.genfromtxt(path, delimiter=",",dtype=None, encoding=None)
    cities = csv[0][:].tolist()
    cities.pop(0)

    distances = np.delete(csv,0,0)
    distances = np.delete(distances,0,1)
    distances = pd.DataFrame(distances, columns = cities, index = cities)

    return cities, distances

def calcTotalDist(order, data):
    '''
    Calculate the total distance in the cities sequence given
    '''
    sume = 0
    for i in range(len(order)):
        if(not i == len(order) - 1):
            a = order[i]
            b = order[i+1]
            sume += float(data.loc[a,b])
    return sume

def swapPositions(list, pos1, pos2):
    '''
    Swap two elements in a list
    '''
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

class Genes:
    '''
    Genes class. It contains the genomes (cities order), distance table and cost.
    '''
    def __init__(self, order, distances):
        self.genomes = order
        self.cost = calcTotalDist(order, distances)
        self.distances = distances

    # Representation and comparison functions between instances
    def __repr__(self):
        return str(self.genomes)
    def __str__(self):
        return str(self.genomes)

    def __eq__(self, other):
        return self.cost == other.cost
    def __lt__(self, other):
        return self.cost < other.cost
    def __gt__(self, other):
        return self.cost > other.cost
    def __le__(self, other):
        return self.cost <= other.cost
    def __ge__(self, other):
        return self.cost >= other.cost
        
    # Returns a copy of the instance
    def copy(self):
        return Genes(self.genomes,self.distances)


    # Mutation function. With a probability of mutationThresh% changes two elements in the city order
    def mutate(self):
        mutationThresh = 80
        prob = random.randint(0,100)
        if(prob < mutationThresh):
            i = random.randint(0,len(self.genomes)-1)
            j = i
            while(j == i):
                j = random.randint(0,len(self.genomes)-1)
            self.genes = swapPositions(self.genomes,i,j)
        
        return prob < mutationThresh

    # Swap two genomes
    def swapGenomes(self,a,b):
        swapPositions(self.genomes,a,b)
    
    # Compare two genome sequences
    def comparePositions(self, other):
        x = np.array(self.genomes)
        y = np.array(other.genomes)
        diff = x == y
        return diff

    # Crossover function. Not used, in this problem it doesn't give good results
    # Compares two genes and changes two genomes in which they differ.
    def crossWith(self, other):
        son = self.copy()
        diff = self.comparePositions(other)
        id = list(getIndexes(diff,False))
        # Change genomes with respect to the similarities
        a = random.choice(id)
        id.remove(a)
        b = random.choice(id)
        son.swapGenomes(a,b)
        return son
        
        

def randomOrder(cities):
    '''
    Random order of cities to initialize a population
    '''
    c = cities.copy()
    random.shuffle(c)
    return c

def crossGenes(genes):
    '''
    Function to cross the population.
    '''
    # Iterate through pairs of genes and change the genomes that are different
    newGenes=[]
    for i in range(0,len(genes),2):
        a = genes[i]
        b = genes[i+1]
        try:
            c = a.crossWith(b)
            newGenes.append(c)
        except:
            newGenes.append(a)
    return newGenes




if __name__ == "__main__":
    cities, distances = loadData('distances.csv')

    # Create a population of NGENES individuals
    NGENES = 1000
    genes = []
    # Inital genes
    for i in range(NGENES):
        rndCities = randomOrder(cities)
        testGene = Genes(rndCities, distances)
        testGene.mutate()
        genes.append(testGene)

    # Sort the population by cost (increasing)
    genes.sort()
    # Print the best and worst
    print(genes[0].cost, genes[-1].cost)

    # Generations to compute
    maxGen = 200
    generation = 0

    # Main loop
    while(generation < maxGen):
        generation += 1

        # Get the best genes untouched
        # The best are not mutated in order not to get worse results
        threshold = 0.1
        newPool = []
        for i in range(int(NGENES*threshold)):
            newPool.append(genes[i].copy())
        bestSize = len(newPool)

        # Get the rest and mutate them
        freeSlots = NGENES - bestSize
        for i in range(freeSlots):
            new = genes[int(NGENES*threshold)+i]
            new.mutate()
            newPool.append(new.copy())

        # Copy to the population and sort again
        genes = newPool.copy()
        genes.sort()
        print(generation, genes[0].cost, genes[-1].cost)

    print("Best oder: ",genes[0], " - With cost: ", genes[0].cost)



