from Particle import Particle
import numpy as np
import math

class Container:
    def __init__(self,Length,radius,particle_list,time_step,momentum,area,number):
        self.Length=Length
        self.radius=radius
        self.particle=particle_list
        self.time=time_step
        self.momentum=0
        self.area=0
        self.number=number

    def check(self,position):
        wall_collision, axis=False, "nil"
        if (np.greater(position,np.array([self.Length,self.Length,self.Length])).any() or np.less(position,np.array([0,0,0])).any()) == True:
            wall_collision=True
            if np.greater(position,np.array([self.Length,self.Length,self.Length])).any()==True:
                axis=np.where(np.greater(position,np.array([self.Length,self.Length,self.Length]))==True)[0][0]
            else:
                axis=np.where(np.less(position,np.array([0,0,0]))==True)[0][0]
        return wall_collision, axis

    def line(self,init_pos,final_pos,k,k_star,end_pos):
        y=init_pos[k]+((final_pos[k]-init_pos[k])/(final_pos[k_star]-init_pos[k_star]))*(end_pos-init_pos[k_star])
        return y 

    def collide(self,particle,k):
        old_pos=particle.position
        particle.update(self.time)
        new_pos=particle.position
        new_position=[0,0,0]
        if old_pos[k]+self.radius >= self.Length:
            intersect=self.Length-self.radius
        if old_pos[k]-self.radius <= 0:
            intersect=self.radius
        new_position[k]=intersect
        new_position[k-1]=self.line(old_pos,new_pos,k-1,k,intersect)
        new_position[k-2]=self.line(old_pos,new_pos,k-2,k,intersect)

        particle.position=np.array(new_position)
        velocity=particle.velocity
        velocity[k]=-1*velocity[k]
        momentum_change=2*velocity[k]*particle.mass
        if momentum_change < 0:
            momentum_change=-1*momentum_change
        particle.velocity=velocity

        self.momentum+=momentum_change
        self.area+=math.pi*((self.radius/2)**2)




