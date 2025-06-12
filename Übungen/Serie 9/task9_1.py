import numpy as np
import matplotlib.pyplot as plt

# Given is a vector field v(x,y) = (-y, x)^T.
# Utility to sample a given position [x,y]:


def v(pos):
    return np.array([-pos[1], pos[0]])


# Show the vector field using a quiver plot
X, Y = np.meshgrid(np.arange(-8, 8), np.arange(-8, 8))
U = -Y
V = X

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()
ax.set_title(r'$v(x,y) =  (-y \quad x)^T$')
ax.quiver(X, Y, U, V)


####################
# Task 1           #
####################

start_x = 1
start_y = 0

delta_t = 0.7
t_max = 2 * np.pi


# 1: Euler Integration
# s(t + delta_t) = s(t) + delta_t * v(s(t))
def euler_integration(start_pos, delta_t, t_max):
    t = 0
    pos = np.array(start_pos, dtype=float)
    positions = [pos.copy()]

    while t < t_max:
        pos += delta_t * v(pos)
        positions.append(pos.copy())
        t += delta_t

    return np.array(positions)

# 2: Runge-Kutta-2 Integration
# s(t + delta_t) = s(t) + delta_t * v_mid
# v_mid = v(t + delta_t * v(t)/2)
def runge_kutta_2_integration(start_pos, delta_t, t_max):
    t = 0
    pos = np.array(start_pos, dtype=float)
    positions = [pos.copy()]

    while t < t_max:
        v_mid = v(pos + delta_t * v(pos) / 2)
        pos += delta_t * v_mid
        positions.append(pos.copy())
        t += delta_t

    return np.array(positions)

# 3: Runge-Kutta-4 Integration
# s(t + delta_t) = s(t) + delta_t * (k1 + 2*k2 + 2*k3 + k4) / 6
# k1 = v(t)
# k2 = v(t + delta_t * k1 / 2)
# k3 = v(t + delta_t * k2 / 2)
# k4 = v(t + delta_t * k3)
def runge_kutta_4_integration(start_pos, delta_t, t_max):
    t = 0
    pos = np.array(start_pos, dtype=float)
    positions = [pos.copy()]

    while t < t_max:
        k1 = v(pos)
        k2 = v(pos + delta_t * k1 / 2)
        k3 = v(pos + delta_t * k2 / 2)
        k4 = v(pos + delta_t * k3)
        pos += delta_t * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        positions.append(pos.copy())
        t += delta_t

    return np.array(positions)


# Perform the integrations
positions_euler = euler_integration((start_x, start_y), delta_t, t_max)
positions_rk4 = runge_kutta_4_integration((start_x, start_y), delta_t, t_max)
positions_rk2 = runge_kutta_2_integration((start_x, start_y), delta_t, t_max)

# Plot the results
ax.plot(positions_euler[:, 0], positions_euler[:, 1], label='Euler', color='steelblue')
ax.plot(positions_rk2[:, 0], positions_rk2[:, 1], label='RK2', color='orange')
ax.plot(positions_rk4[:, 0], positions_rk4[:, 1], label='RK4', color='green')


ax.legend()
ax.grid()
plt.show()
