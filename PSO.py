from numpy import array
from random import random
from math import sqrt, exp, cos, pi


iter_max = 1000
particle_number = 100
dimensions = 2
c1 = 2
c2 = 2


class Particle:
    pass

#Rosenbrock function
def rosenbrock_function(x):
    fitness=pow((1-x[0]),2)+100*pow((x[1]-x[0]*x[0]),2)
    return fitness
#Ackley function
def ackley_function(param):
    a=[w*w for w in param]
    b=[cos(2*pi*w) for w in param]
    fitness=-20*exp(-0.2*sqrt(0.5*sum(a)))-exp(0.5*sum(b))+20+exp(1)
    return fitness
#sphere function
def sphere_function(param):
    fitness=sum([w*w for w in param])
    return fitness

#initialize the particles
def initialize(f):
    particles = []
    for i in range(particle_number):
         p = Particle()
         p.params = array([random() for i in range(dimensions)])
         p.v = 0.0
         p.best=p.params
         p.fitness=f(p.params)
         particles.append(p)
    return particles

# let the first particle be the global best
def pso_main(f,particles):
    gbest = particles[0]
    i=0
    while i < iter_max :
        for p in particles:
            fitness = f(p.params)
            #print fitness
            if fitness < p.fitness:
                p.fitness = fitness
                p.best = p.params

            if fitness < gbest.fitness:
                gbest = p
            v = p.v + c1 * random() * (p.best - p.params) + c2 * random() * (gbest.params - p.params)
            p.params = p.params + v
        i  += 1
    return gbest

if __name__ == '__main__':
    particles=initialize(rosenbrock_function)
    gbest=pso_main(rosenbrock_function,particles)
    print 'function        :  rosenbrock_function'
    print 'gbest fitness   : ', gbest.fitness
    print 'gbest params    : ', gbest.params
    particles=initialize(ackley_function)
    gbest=pso_main(ackley_function,particles)
    print 'function        :  ackley_function'
    print 'gbest fitness   : ', gbest.fitness
    print 'gbest params    : ', gbest.params
    particles=initialize(sphere_function)
    gbest=pso_main(sphere_function,particles)
    print 'function        :  sphere_function'
    print 'gbest fitness   : ', gbest.fitness
    print 'gbest params    : ', gbest.params



