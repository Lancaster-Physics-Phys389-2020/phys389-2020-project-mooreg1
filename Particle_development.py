import numpy as np

class Particle:
    def __init__(self, initialPosition, initialVelocity, radius, mass,name):
        self.velocity=np.array(initialVelocity)
        self.position=np.array(initialPosition)
        self.radius=radius
        self.mass=mass
        self.name=name

    def __repr__(self):
        return 'Radius: %10s, Mass: %.5e, Position: %s, Velocity: %s, Name: %s'%(self.radius,self.mass,self.position,self.velocity,self.name)

    def update(self,delta_t):
        self.position=self.position+(delta_t*self.velocity)

    def reverse(self,delta_t):
        self.position=self.position-(delta_t*self.velocity)

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

class Oxygen(Particle):
    def __init__(self,initialPosition,initialVelocity,name):
        mass=5.32e-26
        radius=292e-12
        super().__init__(initialPosition, initialVelocity, radius, mass,name)
        self.velocity=np.array(initialVelocity)
        self.position=np.array(initialPosition)
        self.radius=radius
        self.mass=mass
        self.name=name

class Nitrogen(Particle):
    def __init__(self,initialPosition,initialVelocity,name):
        mass=4.65e-26
        radius=300e-12
        super().__init__(initialPosition, initialVelocity, radius, mass,name)
        self.velocity=np.array(initialVelocity)
        self.position=np.array(initialPosition)
        self.radius=radius
        self.mass=mass
        self.name=name