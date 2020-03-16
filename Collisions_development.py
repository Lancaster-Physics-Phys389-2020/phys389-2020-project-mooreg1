import numpy as np
from Particle_development import Particle
from Particle_development import Oxygen
from Particle_development import Nitrogen
from Box import Container

class method:
    def __init__(self,particle_list,Box):
        self.particles=particle_list
        self.box=Box

    def particle_collision_check(self,i):
        Collision=False
        particle=self.particles[i]
        for other_particles in self.particles:
            if particle.name==other_particles.name:
                continue
            pos_diff=np.linalg.norm(particle.position-other_particles.position)
            if pos_diff <= (2*particle.radius):
                Collision=True
                return Collision, other_particles.name
            return Collision, "place_holder"

    def collide(self,i,j):
        r_ij=(i.position-j.position)/(np.linalg.norm(i.position-j.position))
        p_transfered=-2*(i.mass*j.mass)/(i.mass+j.mass)*(np.dot(i.velocity-j.velocity,r_ij))*r_ij
        i.velocity+=p_transfered/i.mass
        j.velocity-=p_transfered/j.mass
        

    def update(self,delta_t):
        for i in self.particles:
            i.update(delta_t)
            particle_check=self.particle_collision_check(i.name)
            if particle_check[0]==True:
                other_particle_to_collide=self.particles[particle_check[1]]
                self.collide(other_particle_to_collide,i)
                print("Collision")
            wall_check=self.box.check(i.position)
            if wall_check[0]==True:
                self.box.collide(i,wall_check[1],delta_t)