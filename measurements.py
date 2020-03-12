from Particle import Particle
import numpy as np
import matplotlib.pyplot as plt
import math
from Main import mass
from Main import temp
from Main import number
from Main import timestep
from scipy.optimize import leastsq
import statistics

def fitfunc(constant, velocities):
    results = []
    for v in velocities:
        results.append(constant[0]*4*math.pi*(v**2)*((mass/(2*math.pi*1.38e-23*temp))**(3/2))*math.exp((-1*mass*(v**2))/(2*1.38e-23*temp)))

    return results


def v_distribution(time,bins):
    data=np.load("Velocity_data.npy")
    velocities=data[time]
    histogram=plt.hist(velocities,bins,label="My data")

    errfunc  = lambda k, x, y: (y - fitfunc(k, x))

    diff=(histogram[1][1]-histogram[1][0])/2
    x_values=[]
    for i in range(len(histogram[1])-1):
        x_values.append(histogram[1][i]+diff)
    y_values=histogram[0]
    init=[number]
    out=leastsq(errfunc,init,args=(x_values,y_values))
    c=out[0]

    mean=statistics.mean(velocities)
    exp_mean=math.sqrt((8*8.31*temp)/(math.pi*mass*6.02e23))
    v_2=[]
    for v in velocities:
        v=v*v
        v_2.append(v)
    rms=math.sqrt(statistics.mean(v_2))
    exp_rms=math.sqrt((3*8.31*temp)/(mass*6.02e23))

    plt.plot(x_values,fitfunc(c,x_values),label="Theoretical plot")
    plt.legend()
    plt.text(0.75*max(velocities),0.5*max(histogram[0]),"our mean="+str(mean)+ "\n Theoretical mean="+str(exp_mean)+"\n Our rms speed="+str(rms)+"\n Theoretical rms speed="+str(exp_rms))
    return histogram

def density():
    data=np.load("Left.npy")
    x=[]
    for timestep in range(0,len(data)):
        x.append(timestep)
    plot=plt.plot(x,data[x])

    data=np.load("Right.npy")
    x=[]
    for timestep in range(0,len(data)):
        x.append(timestep)
    plot=plt.plot(x,data[x])
    return plot

plt.figure(1)
plot=v_distribution(1,25)
plt.figure(2)
plot_2=v_distribution(int(timestep/2),25)
plt.figure(3)
plot_3=v_distribution(timestep-1,25)
plt.figure(4)
plot_4=density()
plt.show()