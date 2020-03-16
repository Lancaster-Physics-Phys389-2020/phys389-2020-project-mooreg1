import random
import math
import numpy as np
from Particle_development import Particle
from Particle_development import Oxygen
from Particle_development import Nitrogen
from Box_development import Container

def create(mass,radius,T,box):
    mean_v=math.sqrt((1.38e-23*T)/mass)
    initial_position=np.array([random.uniform(radius,(box.Length-radius)),random.uniform(radius,(box.Length-radius)),random.uniform(radius,(box.Length-radius))])
    initial_velocity=np.array([random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v))])
    return [initial_position,initial_velocity]

def check(new_particle,other_particle):
    position_difference=np.linalg.norm(new_particle.position-other_particle.position)
    if position_difference >= (new_particle.radius+other_particle.radius):
        Allowed=True
    else:
        Allowed=False
    return Allowed

def generate_oxygen(N,particle_list,T,box):
    while len(particle_list) < N:
        initial=create(5.32e-26,292e-12,T,box)
        new_particle=Oxygen(initial[0],initial[1],0)
        if len(particle_list)==0:
            Allowed=True
        else:
            Allowed=True
            for other_particle in particle_list:
                outcome=check(new_particle,other_particle)
                if outcome==False:
                    Allowed=False
        if Allowed==True:
            particle_list.append(new_particle)
            new_particle.name=particle_list.index(new_particle)
    return particle_list

def generate_nitrogen(N,particle_list,T,box):
    while len(particle_list) < N:
        initial=create(4.65e-26,300e-12,T,box)
        new_particle=Nitrogen(initial[0],initial[1],0)
        if len(particle_list)==0:
            Allowed=True
        else:
            Allowed=True
            for other_particle in particle_list:
                outcome=check(new_particle,other_particle)
                if outcome==False:
                    Allowed=False
        if Allowed==True:
            particle_list.append(new_particle)
            new_particle.name=particle_list.index(new_particle)
    return particle_list
    
def generate_new(N,particle_list,T,mass,radius,box):
    while len(particle_list) < N:
        initial=create(mass,radius,T,box)
        new_particle=Nitrogen(initial[0],initial[1],0)
        if len(particle_list)==0:
            Allowed=True
        else:
            Allowed=True
            for other_particle in particle_list:
                outcome=check(new_particle,other_particle)
                if outcome==False:
                    Allowed=False
        if Allowed==True:
            particle_list.append(new_particle)
            new_particle.name=particle_list.index(new_particle)
    return particle_list

"""
def generate(N_oxy,N_nit,T):
    particle_list=[]
    while len(particle_list) < N_oxy:
        mean_v=math.sqrt((1.38e-23*T)/(2.66e-23))
        initial_position=np.array([random.uniform((2*292e-12),L-(2*292e-12)),random.uniform((2*292e-12),L-(2*292e-12)),random.uniform((2*292e-12),L-(2*292e-12))])
        initial_velocity=np.array([random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v))])
        new_particle=Oxygen(initial_position,initial_velocity,0)
        if len(particle_list)=0:
            Allowed=True
        else:
            for particles in particle_list:
                pos_diff=np.linalg.norm(particles.position-initial_position)
                if pos_diff >= (particles.radius+new_particle.radius):
                    Allowed=True
                else:
                    Allowed=False
        if Allowed=True:
            particle_list.append(new_particle)
            new_particle.name=particle_list.index(new_particle)

    while len(particle_list) < (N_oxy+N_nit):
        mean_v=math.sqrt((1.38e-23*T)/(2.33e-23))
        initial_position=np.array([random.uniform((2*300e-12),L-(2*300e-12)),random.uniform((2*300e-12),L-(2*300e-12)),random.uniform((2*300e-12),L-(2*300e-12))])
        initial_velocity=np.array([random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v)),random.uniform(-(2*mean_v),(2*mean_v))])
        for for particles in particle_list:
                pos_diff=np.linalg.norm(particles.position-initial_position)
                if pos_diff >= (particles.radius+new_particle.radius):
                    Allowed=True
                else:
                    Allowed=False
        if Allowed=True:
            particle_list.append(new_particle)
            new_particle.name=particle_list.index(new_particle)


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
    """