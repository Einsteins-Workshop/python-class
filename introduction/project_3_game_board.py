import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the data for the sine wave
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

# Create the figure and axes
fig, ax = plt.subplots()
line, = ax.plot(x, y, 'b-')  # Plot the sine wave
point, = ax.plot([], [], 'ro') # Initialize an empty plot for the moving point

# Set plot limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    return point,

# Animation function: this is called sequentially
def animate(i):
    # Update the position of the moving point
    point_x = x[i % len(x)]
    point_y = y[i % len(y)]
    point.set_data(point_x, point_y)
    return point,

# Create the animation
# FuncAnimation takes:
# - fig: The figure object
# - func: The function to call each frame
# - frames: The number of frames in the animation (or an iterable)
# - init_func: An optional function to run once at the start
# - blit: Whether to use blitting for faster rendering (True is generally better)
ani = animation.FuncAnimation(fig, animate, frames=len(x), init_func=init, blit=True, interval=50)

# Display the animation

plt.show()