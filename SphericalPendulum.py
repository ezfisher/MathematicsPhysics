'''Using Hamilton's equations to plot the positoins of a spherical pendulum as a function of time'''
import matplotlib.pyplot as plt
import math

length = 1
gravity = 1
mass = 1
azimuthal_momentum = 1 # constant of motion
time_step = 0.01
time_max = 100
time = [0]
theta = [math.pi/2]
thetadot = 0
phi = [0]
x = [length*math.sin(phi[0])*math.cos(theta[0])]
y = [length*math.sin(phi[0])*math.sin(theta[0])]
z = [length*math.cos(phi[0])]
phidot = azimuthal_momentum/(mass*length**2*math.sin(theta[0]))
alpha = 1/2*math.sin(theta[0])**2*math.cos(theta[0])*phidot**2 - gravity/length * math.sin(theta[0])

i = 1
while (time[-1] < time_max):
	thetadot += alpha*time_step
	theta.append((thetadot*time_step + theta[i-1]) % 2*math.pi)
	phi.append((phidot*time_step + phi[i-1]) % 2*math.pi)
	alpha = 1/2*math.sin(theta[i-1])**2*math.cos(theta[i-1]) - gravity/length*math.sin(theta[i-1])
	x.append(length*math.sin(phi[i])*math.cos(theta[i]))
	y.append(length*math.sin(phi[i])*math.sin(theta[i]))
	z.append(length*math.cos(phi[i]))
	i += 1
	time.append(time[-1] + time_step)
	
plt.plot(time, z)
plt.title('z position vs time')
plt.xlabel('time')
plt.ylabel('z')
plt.show()

#plt.plot(time, y)
#plt.title('y position vs time')
#plt.xlabel('time')
#plt.ylabel('y')
#plt.show()

#plt.plot(time, x)
#plt.title('x position vs time')
#plt.xlabel('time')
#plt.ylabel('x')
#plt.show()
