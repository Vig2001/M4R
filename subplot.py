"""Creates subplots from the plots made in R"""
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# List of your image paths
image_paths = [
    'plots/NSAA1_Stand.png',
    'plots/NSAA1_Walk.png',
    'plots/NSAA1_Rise_From_Floor.png',
    'plots/NSAA1_Run_10m.png'
]

# Create a figure with subplots in a 2x2 grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Loop through the image paths and axes to display each image
for ax, img_path in zip(axes, image_paths):
    # Open the image file
    img = Image.open(img_path)
    # Show the image on the respective subplot
    ax.imshow(img)
    # Remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    # Optionally set titles or adjust aspects
    ax.set_title(img_path.split('/')[-1].replace('.png', ''))

# Adjust layout
plt.tight_layout()

# Display the figure
plt.show()

# Optionally, save the figure to a new file
fig.savefig('combined_plots.png')