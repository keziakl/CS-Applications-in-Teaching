import math
import matplotlib.pyplot as plt
import numpy as np

#models the Time Period formula for an ideal spring
def time_period(mass, k):
    return 2*math.pi*np.sqrt(mass/k)

#models the displacement equation for SHM
def object_displacement(A, freq, time):
    return A*np.cos(2*math.pi*freq*time)

#inverts frequency to time or time to frequency and checks for division by zero
def inv_freq_time(x):
    if x != 0:
        return 1/x
    else:
        return -1
  
  
#answering the basic questions
#A horizontal spring with a spring constant of k = 300 N/m is attached to a frictionless surface. A block of mass 2kg is attached to the end of the spring.
#Calculate the period
time_period_of_spring = time_period(2, 300)
print("the time period of the spring is:")
print(time_period_of_spring)
#Calculate the frequency
freq_of_spring = inv_freq_time(time_period_of_spring)
print("the frequency of the spring is:")
print(freq_of_spring)


#modeling the first set of questions
#1) Given a maximum amplitude of 1.2 m for the spring above, what is the displacement of the spring at 3 seconds?
displacement_3 = object_displacement(1.2, freq_of_spring, 3)
print("the displacement of the spring at 3 seconds is:")
print(displacement_3)
#2) 5 seconds?
displacement_5 = object_displacement(1.2, freq_of_spring, 5)
print("at 5 seconds it is:")
print(displacement_5)
#3) 7 seconds?
displacement_7 = object_displacement(1.2, freq_of_spring, 7)
print("at 7 seconds it is:")
print(displacement_7)
#4) Graph the displacement as a function of time.
x = np.array(range(1, 100))
y = object_displacement(1.2, freq_of_spring, x)
fig, axs = plt.subplots(3)
fig.suptitle("Modelling Physics Equations")
#remove the "#" below to show title on graph
#axs[0].set_title("displacement as a function of time")
axs[0].plot(x, y)


#modeling the second set of questions
#1) What would happen to the period of the spring if k = 150 N/m?
time_period_changed_k = time_period(2, 150)
print("the new time period of a k=150N/m spring is:")
print(time_period_changed_k)
#2) If the mass was 1 kg?
time_period_changed_m = time_period(1, 300)
print("the new time period of a mass of 1kg is:")
print(time_period_changed_m)
#3) Graph the period as a function of k.
y = time_period(2, x)
#remove the "#" below to show title on graph
#axs[1].set_title("Period as a function of k")
axs[1].plot(x, y)
#4) Graph the period as a function of m.
y = time_period(x, 300)
#remove the "#" below to show title on graph
#axs[2].set_title("Period as a function of mass")
axs[2].plot(x, y)
 
#shows plotted graphs
plt.show()
 
 

