import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# import csv data
df_gdp = pd.read_csv('gdp_filtered.csv') # x-axis
df_life_expectancy = pd.read_csv('life_expectancy_filtered.csv') # y-axis
df_population = pd.read_csv('population_filtered.csv') # size of points
df_child_mortality = pd.read_csv('child_mortality_filtered.csv') # color of points

# a)
gdp_data = df_gdp.iloc[:, 1:].values
life_expectancy_data = df_life_expectancy.iloc[:, 1:].values
num_countries, num_years = gdp_data.shape
p = [np.stack([gdp_data[:, i], life_expectancy_data[:, i]], axis=1) for i in range(num_years)]

# b)
population_data = df_population.iloc[:, 1:].values
child_mortality_data = df_child_mortality.iloc[:, 1:].values
s = [(population_data[:, i] / 100000).astype('float64') for i in range(num_years)]
c = [child_mortality_data[:, i].astype('float64') for i in range(num_years)]

# we only need one subplot
fig, ax = plt.subplots(figsize=(13,8))

# fix axis limits to prevent jumpy animations
ax.set(xlim=(0, 80000), ylim=(15, 90), xlabel='GDP per Capita', ylabel='Life Expectancy')

# c)
scatterplot = ax.scatter(p[0][:,0], p[0][:,1], s=s[0], c=c[0], vmin=0.0, vmax=200.0)
fig.colorbar(scatterplot, label='Child Mortality Rate')

# animation parameters
time_res = 10 # interpolation steps between keyframes
time_speed = 0.1 # seconds between each keyframe 
time_steps = time_res*(len(p)-1) # number of global timesteps

def animate(i):
    # linear interpolation parameters
    t = i / time_res  # current point in time (e.g. 2.15)
    t_low = int(t)    # lower discrete time (e.g. 2)
    f = t - t_low     # interpolation factor (e.g. 0.15)

    if t_low + 1 >= len(p):
        return

    # d)
    # set the new positions
    p_interp = (1-f) * p[t_low] + f * p[t_low + 1]
    scatterplot.set_offsets(p_interp)

    # set the new sizes
    s_interp = (1-f) * s[t_low] + f * s[t_low + 1]
    scatterplot.set_sizes(s_interp)

    # set the new colors
    c_interp = (1-f) * c[t_low] + f * c[t_low + 1]
    scatterplot.set_array(c_interp)

    # e)
    year = 1900 + t_low + (1 if f > 0 else 0)
    ax.set_title(f'Year: {year}')


# show the animation with a call to FuncAnimation
# this needs to be stored in a variable (here: 'anim') to prevent garbage collection
anim = FuncAnimation(fig, animate, interval=(1000*time_speed)/time_res, frames=time_steps)
plt.show()