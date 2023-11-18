import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import to_rgba

# List of texts, font sizes, boldness values, and colors to cycle through
texts = ['1', '2', '3','...']
font_sizes = [12, 28, 72, 42]
boldness_values = [False, True, False, True]
colors = ['red', 'green', 'blue', 'black']

# Function to update the text for each frame
def update(frame):
    index = frame % len(texts)
    text.set_text(texts[index])  # Cycle through the list of texts
    text.set_fontsize(font_sizes[index])  # Change font size
    text.set_weight('bold' if boldness_values[index] else 'normal')  # Change boldness
    text.set_color(to_rgba(colors[index]))  # Change text color
    return text,

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Create a text element
text = ax.text(0.5, 0.5, 'Initial Text', ha='center', va='center', fontsize=12, weight='normal', color='black')

# Set up the animation
animation = FuncAnimation(fig, update, frames=None, interval=1000, blit=True)

# Show the animated plot
plt.show()
