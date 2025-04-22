import numpy as np # math
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # loading images
import pandas # handling csv data

fig = plt.figure(figsize=(12,7))

# loading a table with pandas
data_frame = pandas.read_csv("spread_data.csv")
img = mpimg.imread('germany.png')

height = img.shape[0]
width = img.shape[1]

max_einwohner = data_frame['Einwohner'].max()


print(data_frame)


# Create two subplots side by side
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

# Display the same image in both subplots
ax1.imshow(img, extent=[0, width, 0, height], aspect='equal')
ax2.imshow(img, extent=[0, width, 0, height], aspect='equal')


# Draw circles on the first subplot with red color

x = data_frame['x_pos']
y = data_frame['y_pos'] * -1 + height
seven_day_infections = data_frame['Anzahl Inf. 7T']
residents = data_frame['Einwohner']
colors = seven_day_infections / max_einwohner * 100000

areas_1 = seven_day_infections * 0.05
# areas 2 uses Steven’s area judgement scale with alpa = 300
areas_2 = (seven_day_infections / 300)**(7/5)

ax1.scatter(x, y, s=areas_1)
ax2.scatter(x, y, s=areas_2, cmap="magma", c=colors, alpha=0.5)


# Optional: set titles for each subplot
ax1.set_title("Fälle in 7 Tagen = Punktgröße (Fläche)")
ax2.set_title("Fälle in 7 Tagen = Punktgröße (Steven)")

plt.colorbar(ax2.collections[0], ax=ax2, label='Fälle je 100000 Einwohner (7 Tage)', shrink=0.5, orientation='horizontal', pad=0.02)
# Run show, to make sure everything is displayed.
plt.show()