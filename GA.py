import numpy as np
import random
import time
import matplotlib.pyplot as plt
random.seed(time.time())
N = 4 * 3  # dna length
M = 15 # individual number
MAX_EPOCH = 1000
Pc = 0.1
Pm = 0

def Main():
    indList = [genotype() for i in range(M)]
    initFit = [g.evaluate() for g in indList]
    fitRecord = []
    fitRecord.append(initFit)
    print('Initial Value:', initFit)

    for epoch in range(MAX_EPOCH):
        children = []
        random.shuffle(indList)
        for ind in indList:
            children.append(ind.mutation())
        for i in range(M//2):
            if flip(Pc):
                children += indList[i].cross1(indList[i + M//2])
            if flip(Pc):
                children += indList[i].cross2(indList[i + M//2])
        children += indList

        fitness = [- g.evaluate() for g in children]
        indList = random.choices(children, fitness, k=M)
        fitRecord.append([g.evaluate() for g in indList])

    # Result and Visualize
    [print(l) for l in fitRecord]
    print(np.min(np.min(fitRecord)))
    plt.plot(list(range(MAX_EPOCH+1)), [np.max(x) for x in fitRecord])
    plt.show()



def target(x1, x2, x3):
    return 2 * x1 ** 2 - 3 * x2 ** 2 - 4 * x1 + 5 * x2 + x3

def flip(r):
    return random.random() < r

class genotype:
    def __init__(self):
        self. gene = []
        for i in range(N):
            self.gene.append(1 if flip(0.5) else 0)
        self.fitness = 0

    def evaluate(self):
        x1 = '0b' + ''.join(str(x) for x in self.gene[ :4])
        x2 = '0b' + ''.join(str(x) for x in self.gene[4:8])
        x3 = '0b' + ''.join(str(x) for x in self.gene[8:12])
        x1, x2, x3 = int(x1, 2), int(x2, 2), int(x3, 2)
        self.fitness = target(x1,x2,x3)
        return self.fitness

    def mutation(self):
        newInd = genotype()
        for i in range(len(self.gene)):
            if flip(Pm):
                newInd.gene[i] = (self.gene[i] + 1) % 2
            else:
                newInd.gene[i] = self.gene[i]
        return newInd

    def cross1(self, pair):
        newInd1 = genotype()
        newInd2 = genotype()
        crossPoint = random.randint(1, len(self.gene) - 2)
        newInd1.gene[:crossPoint] = self.gene[:crossPoint].copy()
        newInd2.gene[:crossPoint] = pair.gene[:crossPoint].copy()
        newInd1.gene[crossPoint:] = pair.gene[crossPoint:].copy()
        newInd2.gene[crossPoint:] = self.gene[crossPoint:].copy()
        return newInd1, newInd2


    def cross2(self, pair):
        newInd1 = genotype()
        newInd2 = genotype()
        P1 = random.randint(1, len(self.gene) - 2)
        P2 = random.randint(1, len(self.gene) - 2)
        if P1>P2:
            P1, P2 = P2, P1
        newInd1.gene[:P1] = self.gene[:P1].copy()
        newInd2.gene[:P1] = pair.gene[:P1].copy()
        newInd1.gene[P1:P2] = pair.gene[P1:P2].copy()
        newInd2.gene[P1:P2] = self.gene[P1:P2].copy()
        newInd1.gene[P2:] = self.gene[P2:].copy()
        newInd2.gene[P2:] = pair.gene[P2:].copy()
        return newInd1, newInd2

Main()