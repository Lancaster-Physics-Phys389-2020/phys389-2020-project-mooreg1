from Particle_development import Particle
from Particle_development import Oxygen
from Particle_development import Nitrogen
from Generate_development import generate_oxygen
from Generate_development import generate_nitrogen
from Generate_development import generate_new
from Collisions_development import method
from Box_development import Container

import matplotlib.pyplot as plt
import math 
import numpy as np
import pandas as pd

length,n_oxy,n_nit,temp,delta_t=1e-8,300,300,300,1e-12

def function(delta_t):
    box=Container(length)
    particle_list=generate_oxygen(n_oxy,[],300,box)
    particle_list_final=generate_nitrogen(n_nit,particle_list,300,box)

    system=method(particle_list_final,box)
    print("initialised")

    x=[]
    y=[]
    lhs=[]
    rhs=[]
    n_velocities=[]
    o_velocities=[]
    iteration=0
    while box.collision_no <= 150000:
        system.update(delta_t)
        iteration+=1
        timestep_velocities_o=[]
        timestep_velocities_n=[]
        number_left,number_right=0,0
        for particle in particle_list:
            if particle.position[0] >= (box.Length/2):
                number_right += 1
            else:
                number_left += 1
            x.append(particle.position[0])
            y.append(particle.position[1])
            if particle.type=="Oxygen":
                timestep_velocities_o.append(np.linalg.norm(particle.velocity))
            if particle.type=="Nitrogen":
                timestep_velocities_n.append(np.linalg.norm(particle.velocity))
        lhs.append((number_left/len(particle_list)))
        rhs.append((number_right/len(particle_list)))
        o_velocities.append(timestep_velocities_o)
        n_velocities.append(timestep_velocities_n)

    np.save("Left",lhs)
    np.save("Right",rhs)
    np.save("Velocity_data_o",o_velocities)
    np.save("Velocity_data_n",n_velocities)

    pressure=box.total_momentum/(6*(box.Length**2)*delta_t*iteration)
    pressure_oxygen=box.oxygen_momentum/(6*(box.Length**2)*delta_t*iteration)
    pressure_nitrogen=box.nitrogen_momentum/(6*(box.Length**2)*delta_t*iteration)
    print(pressure)
    print(pressure_oxygen)
    print(pressure_nitrogen)
    print(box.collision_no)
    print(iteration)
    np.save("Iteration",iteration)
    
    our_data=pd.read_pickle("Macro_data.csv")
    our_data.append( pd.DataFrame({'Pressure Oxygen':[pressure_oxygen],'Pressure Nitrogen':[pressure_nitrogen],'Pressure Total':[pressure],'Volume':[(box.Length)**3],'Number Oxygen':[n_oxy],'Number Nitrogen':[n_nit],'Number Total':[n_oxy+n_nit],'Temperature':[temp]}))
    print(our_data)
    our_data.to_pickle("Macro_data.csv")
    

if __name__=="__main__":
    function(delta_t)

