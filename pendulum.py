import math

def spherical_pendulum(azimuthal_angle, polar_angle, length, gravity, mass, time_step, time_max):
	# function to numerically simulate a spherical pendulum

	# constants
	azimuthal_momentum = 1 # constant of motion
	time = [0]
	polar_derivative = 0
	x = [length*math.sin(azimuthal_angle[0])*math.cos(polar_angle[0])]
	y = [length*math.sin(azimuthal_angle[0])*math.sin(polar_angle[0])]
	z = [length*math.cos(azimuthal_angle[0])]
	azimuthal_derivative = azimuthal_momentum/(mass*length**2*math.sin(polar_angle[0]))
	alpha = 1/2*math.sin(polar_angle[0])**2*math.cos(polar_angle[0])*azimuthal_derivative**2 - gravity/length * math.sin(polar_angle[0])

	i = 1
	while (time[-1] < time_max):
		polar_derivative += alpha*time_step
		polar_angle.append((polar_derivative*time_step + polar_angle[i-1]) % 2*math.pi)
		azimuthal_angle.append((azimuthal_derivative*time_step + azimuthal_angle[i-1]) % 2*math.pi)
		alpha = 1/2*math.sin(polar_angle[i-1])**2*math.cos(polar_angle[i-1]) - gravity/length*math.sin(polar_angle[i-1])
		x.append(length*math.sin(azimuthal_angle[i])*math.cos(polar_angle[i]))
		y.append(length*math.sin(azimuthal_angle[i])*math.sin(polar_angle[i]))
		z.append(length*math.cos(azimuthal_angle[i]))
		i += 1
		time.append(time[-1] + time_step)
	
	return (azimuthal_angle, polar_angle)
