import random
import math
import numpy as np
from Particle import Particle
def generate(L,r,N,m,T):
    mean_v=math.sqrt((1.38e-23*T)/(m))
    print(mean_v)
    particle_list=[]
    particle_list.append(Particle([L/2,L/2,L/2],np.array([random.uniform((0.9*mean_v),(1.1*mean_v)),random.uniform((0.9*mean_v),(1.1*mean_v)),random.uniform((0.9*mean_v),(1.1*mean_v))]),r,m,0))
    while len(particle_list) < N:
        initial_position=np.array([random.uniform(0,L),random.uniform(0,L),random.uniform(0,L)])
        initial_velocity=np.array([random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v))])
        new_particle=Particle(initial_position,initial_velocity,r,m,0)
        for particles in particle_list:
            pos_diff=np.linalg.norm(particles.position-initial_position)
            if pos_diff >= (2*r):
                Allowed=True
            else:
                Allowed=False
        for k in range(0,3):
            left_position=new_particle.position[k]-r
            right_position=new_particle.position[k]+r
            if 0 >= left_position:
                Allowed=False
            if right_position >= L:
                Allowed=False
        if Allowed==True:
            particle_list.append(new_particle)
            new_particle.name=particle_list.index(new_particle)
    return particle_list