import numpy as np
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
random.seed(time.time())

w = 0.2
c1 = 2
c2 = 2
N = 100
MAX_EPOCH = 10

def Main():
    particles = [Particle(random.random()*15, random.random()*15, random.random()*15) for x in range(N)]
    curve = []

    for epoch in range(MAX_EPOCH):
        if 1:
            x = [p.pos[0] for p in particles]
            y = [p.pos[1] for p in particles]
            z = [p.pos[2] for p in particles]
            plt.ion()
            fig = plt.figure(epoch+1)
            ax = fig.gca(projection='3d')
            plt.xlim(0,15)
            plt.ylim(0,15)
            ax.scatter(x,y,z)
            ax.set_zlim(0, 15)
            plt.show()

        particles[0].eval()
        maxFit = particles[0].fitness
        maxPos = particles[0].pos
        for p in particles[1:]:
            p.eval()
            if maxFit < p.fitness:
                maxFit = p.fitness
                maxPos = p.pos

        for p in particles:
            p.move(maxPos)
        curve.append(maxFit)
        print(maxPos,maxFit)
        print(np.mean([p.v for p in particles]))

    fig = plt.figure(0)
    plt.plot(curve)
    plt.pause(9999)




def eq(x1, x2, x3):
    return 2 * x1 ** 2 - 3 * x2 ** 2 - 4 * x1 + 5 * x2 + x3

def target(x1, x2, x3):
    t = eq(x1, x2, x3)
    return t

class Particle:
    def __init__(self, x1, x2, x3):
        self.pos = np.array([x1,x2,x3]).astype(np.float64)
        self.v = np.array([0,0,0]).astype(np.float64)
        self.fitness = target(*self.pos)
        self.posBest = np.array([x1,x2,x3])
        self.fitnessBest = target(*self.pos)

    def eval(self):
        self.fitness = target(*self.pos)
        if self.fitness>self.fitnessBest:
            self.fitnessBest = self.fitness
            self.posBest = self.pos.copy()
        return self.fitness

    def move(self, GlobalBest=None):
        self.v = w * self.v
        self.v += c1 * random.random() * (self.posBest - self.pos)
        self.v += c2 * random.random() * (GlobalBest - self.pos)

        self.pos += self.v
        self.pos[self.pos<0] = 0
        self.pos[self.pos>15] = 15
        self.eval()
        return self.fitness

Main()
