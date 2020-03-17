from Particle import Particle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from new_main import temp
from scipy.optimize import curve_fit
import statistics

iteration=np.load("Iteration.npy")

def fitfunc(x,a,b):
    results=[]
    for v in x:
        results.append(a*(v**2)*math.exp(-1*b*(v**2)))
    return results

def integral(x,mass,number):
    b=4*math.pi*((mass/(2*math.pi*1.38e-23*temp))**(3/2))
    a=mass/(2*1.38e-23*temp)
    sqrta = math.sqrt(a)
    normalisation = b/(4*a**(1.5))
    term1 = math.sqrt(math.pi)*math.erf(sqrta*x)
    term2 = 2*sqrta*x*math.exp(-1*a*x*x)
    #out= (b/4*(a**(3/2)))*((math.sqrt(math.pi)*math.erf(math.sqrt(a)*x))-(2*math.sqrt(a)*x*math.exp(-1*a*(x**2))))
    out = normalisation*(term1-term2)*number
    return out

def theoretical_plot(data,bins,mass,number):
    edges=np.histogram_bin_edges(data,bins)
    diff=(edges[1]-edges[0])/2
    x_values=[]
    y_values=[]
    for i in range(len(edges)-1):
        x_values.append(edges[i]+diff)
        y_values.append(math.fabs(integral(edges[i],mass,number)-integral(edges[i+1],mass,number)))
    return x_values,y_values

def v_distribution(time,bins,oxygen_hist,nitrogen_hist,oxygen_theory,nitrogen_theory,oxygen_fit,nitrogen_fit):

    oxygen_data=np.load("Velocity_data_o.npy")
    nitrogen_data=np.load("Velocity_data_n.npy")
    oxygen_velocities=oxygen_data[time]
    nitrogen_velocities=nitrogen_data[time]
    oxygen_number=len(oxygen_velocities)
    nitrogen_number=len(nitrogen_velocities)
    if oxygen_hist ==True:
        histogram=plt.hist(oxygen_velocities,bins,label="Simulated oxygen velocities")
    if nitrogen_hist==True:
        histogram=plt.hist(oxygen_velocities,bins,label="Simulated oxygen velocities")

    if oxygen_fit==True:
        y_values=np.array(np.histogram(oxygen_velocities,bins)[0])
        x_values=np.array(theoretical_plot(oxygen_data,bins,5.32e-26,oxygen_number)[0])
        consts=(curve_fit(fitfunc,x_values,y_values,p0=[1,1.2e-6]))[0]
        if oxygen_hist==False:
            histogram=plt.plot(x_values,fitfunc(x_values,consts[0],consts[1]),'r--',label="Fitting for simulated data")
        else:
            plt.plot(x_values,fitfunc(x_values,consts[0],consts[1]),'r--',label="Fitting for simulated data")

    if nitrogen_fit==True:
        y_values=np.array(np.histogram(nitrogen_velocities,bins)[0])
        x_values=np.array(theoretical_plot(nitrogen_data,bins,4.65e-26,nitrogen_number)[0])
        consts=np.array(curve_fit(fitfunc,x_values,y_values,p0=[1,1.2e-6])[0])
        if nitrogen_hist==False:
            histogram=plt.plot(x_values,fitfunc(x_values,consts[0],consts[1]),'g--',label="Fitting for simulated data")
        else:
            plt.plot(x_values,fitfunc(x_values,consts[0],consts[1]),'g--',label="Fitting for simulated data")
    """
    mean=statistics.mean(velocities)
    exp_mean=math.sqrt((8*8.31*temp)/(math.pi*mass*6.02e23))
    v_2=[]
    for v in velocities:
        v_2.append(v*v)
    print(v)
    print(statistics.mean(v_2))
    rms=math.sqrt(statistics.mean(v_2))
    exp_rms=math.sqrt((3*8.31*temp)/(mass*6.02e23))

    #fitfunc(c,x_values)

    plt.legend()
    plt.text(0.75*max(velocities),0.5*max(histogram[0]),"our mean="+str(mean)+ "\n Theoretical mean="+str(exp_mean)+"\n Our rms speed="+str(rms)+"\n Theoretical rms speed="+str(exp_rms))
    """

    if oxygen_theory ==True:
        result=theoretical_plot(oxygen_data,bins,5.32e-26,oxygen_number)
        plt.plot(result[0],result[1],'r-',label="Theoretical plot for Oxygen")
    
    if nitrogen_theory ==True:
        result=theoretical_plot(nitrogen_data,bins,4.65e-26,nitrogen_number)
        plt.plot(result[0],result[1],'g-',label="Theoretical plot for Nitrogen")

    plt.legend()
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
plot=v_distribution(1,25,True,False,True,False,False,False)
plt.figure(2)
plot_2=v_distribution(int(iteration/2),25,False,False,True,False,True,False)
plt.figure(3)
plot_3=v_distribution(iteration-1,25,False,False,True,True,True,True)
plt.figure(4)
plot_4=density()
plt.show()

our_data=pd.read_pickle("Macro_data.csv")
print(our_data)