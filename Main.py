from Particle import Particle
from generate import generate 
from Collisions import method
from Box import Container
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math 
import numpy as np
import pandas as pd

length,radius,number,mass,temp,delta_t,timestep=1e-8,3e-10,250,5e-26,300,0.1,10000
def function(delta_t,timestep):
    particle_list=generate(length,radius,number,mass,temp)
    #particle_list.apppend(Particle(np.array([5e-9,5e-9,50]),np.array([-5,0,0]),3e-9,10,250))
    box=Container(length,radius,particle_list,0.1,0,0,number)
    system=method(particle_list,box)
    print("initiailised")

    x=[]
    y=[]
    lhs=[]
    rhs=[]
    velocities=[]
    for timestep in range (0,timestep):
        system.update(delta_t)
        timestep_velocities=[]
        number_left,number_right=0,0
        for particle in particle_list:
            if particle.position[0] >= (box.Length/2):
                number_right += 1
            else:
                number_left += 1
            x.append(particle.position[0])
            y.append(particle.position[1])
            timestep_velocities.append(np.linalg.norm(particle.velocity))
        lhs.append((number_left/box.number))
        rhs.append((number_right/box.number))
        velocities.append(timestep_velocities)
    np.save("Left",lhs)
    np.save("Right",rhs)
    np.save("Velocity_data",velocities)
#    scatter=plt.scatter(x,y,s=math.pi*5*5*5)
    if box.area==0:
        pressure=0
    else:
        pressure=box.momentum/((box.area)*delta_t*timestep)
    print(box.momentum,box.area)
    print(pressure)
    plt.show()

#df=pd.DataFrame({'Pressure':pressure,})
if __name__=="__main__":
    function(1e-12,30000)

