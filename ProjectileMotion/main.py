import numpy as np
import matplotlib.pyplot as plt

# -- Constants --
g = 9.81
dt = 0.01 

## -- User Input --
v_0 = float(input("Enter the initial velocity (m/s): "))
theta = float(input("Enter the launch angle (degrees): "))

# -- Function --
def projectile_motion(v_0, theta, dt):
    # -- Calculations --
    v_0x = v_0 * np.cos(np.radians(theta)) 
    v_0y = v_0 * np.sin(np.radians(theta))

    s_y = (v_0y**2) / (2*g)

    t_up = v_0y / g
    t_D = np.sqrt(2*s_y/g)
    t_T = t_up + t_D

    s_x = v_0x * t_T

    # -- Time Array --
    t = np.arange(0, t_T + dt, dt)

    # -- Position Arrays --
    x = v_0x * t
    y = v_0y * t - 0.5 * g * t**2
   
    return x, y, t

x, y, t = projectile_motion(v_0, theta, dt)
print(x)

# -- Plotting --
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()