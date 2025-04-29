import numpy as np  # math
import matplotlib.pyplot as plt  # plotting
import matplotlib.image as mpimg  # loading images
import pandas  # handling csv data

# Create figure with more space at bottom for colorbar
fig = plt.figure(figsize=(12, 8))

# loading a table with pandas
data_frame = pandas.read_csv("spread_data.csv")
img = mpimg.imread('germany.png')

height = img.shape[0]
width = img.shape[1]

max_einwohner = data_frame['Einwohner'].max()

print(data_frame)

# Create two subplots side by side with equal width
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# Display the same image in both subplots
ax1.imshow(img, extent=[0, width, 0, height], aspect='equal')
ax2.imshow(img, extent=[0, width, 0, height], aspect='equal')

ax1.axis('off')
ax2.axis('off')

ax1.set_frame_on(True)
ax2.set_frame_on(True)

x = data_frame['x_pos']
y = data_frame['y_pos'] * -1 + height
residents = data_frame['Einwohner']
seven_day_infections = data_frame['Anzahl Inf. 7T']

# Draw circles on the first subplot
# areas 2 uses Steven's area judgement scale with alpa = 300
a = 1/300
areas_1 = seven_day_infections * 0.05
areas_2 = a * ((seven_day_infections)**(1.4))

ax1.scatter(x, y, s=areas_1)
colors = (seven_day_infections / residents) * 100000
scatter_2 = ax2.scatter(x, y, s=areas_2, cmap="magma", c=colors, vmin=0, vmax=250)

ax1.set_title("Fälle in 7 Tagen = Punktgröße (Fläche)")
ax2.set_title("Fälle in 7 Tagen = Punktgröße (Steven)")

# Add colorbar below the second subplot with proper sizing
cbar_ax = fig.add_axes([0.53, 0.05, 0.4, 0.03])
cbar = fig.colorbar(scatter_2, cax=cbar_ax, orientation='horizontal')
cbar.set_label('Fälle je 100000 Einwohner (7 Tage)')

# save, becasue it doesnt show on my pc
# plt.savefig('task3_1.png', dpi=300, bbox_inches='tight')
# Run show, to make sure everything is displayed.
plt.show()