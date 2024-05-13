"""Creates subplots from the plots made in R"""
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# List of your image paths
image_paths1 = [
    'plots/NSAA1_Stand.png',
    'plots/NSAA1_Walk.png',
    'plots/NSAA1_Rise_From_Floor.png',
    'plots/NSAA1_Run.png',
    'plots/NSAA1_Stand_on_Heels.png',
    'plots/NSAA1_Jump.png' ,
    'plots/NSAA1_Lifts_Head.png' ,
    'plots/NSAA1_Stand_Up From_Chair.png',
    'plots/NSAA1_Get_to_Sitting.png'
]

image_paths2 = [
    'plots/NSAA1_Climb_Box_Step_Left.png',
    'plots/NSAA1_Climb_Box_Step_Right.png',
    'plots/NSAA1_Descend_Box_Step_Left.png',
    'plots/NSAA1_Descend_Box_Step_Right.png',
    'plots/NSAA1_Hop_Left_Leg.png',
    'plots/NSAA1_Hop_Right_Leg.png',
    'plots/NSAA1_Stand_on_One_Leg_Left.png',
    'plots/NSAA1_Stand_on_One_Leg_Right.png'
]

# Create a figure with subplots in a 2x2 grid
fig1, ax1 = plt.subplots(nrows=3, ncols=3, figsize=(50, 80), dpi=300)
fig2, ax2 = plt.subplots(nrows=4, ncols=2, figsize=(50, 100), dpi=300)

# Flatten the axes array for easier iteration
axes1 = ax1.flatten()
axes2 = ax2.flatten()

# Loop through the image paths and axes to display each image
for ax1, img_path1 in zip(axes1, image_paths1):
    # Open the image file
    img = Image.open(img_path1)
    # Show the image on the respective subplot
    ax1.imshow(img, aspect='auto')
    # Remove axis ticks
    ax1.set_xticks([])
    ax1.set_yticks([])
    # Optionally set titles or adjust aspects
    #ax.set_title(img_path.split('/')[-1].replace('.png', ''))

# Adjust layout
plt.tight_layout()

for ax2, img_path2 in zip(axes2, image_paths2):
    # Open the image file
    img2 = Image.open(img_path2)
    # Show the image on the respective subplot
    ax2.imshow(img2, aspect='auto')
    # Remove axis ticks
    ax2.set_xticks([])
    ax2.set_yticks([])
    # Optionally set titles or adjust aspects
    #ax.set_title(img_path.split('/')[-1].replace('.png', ''))

# Adjust layout
plt.tight_layout()

# Optionally, save the figure to a new file
fig1.savefig('plots/combined_plots1.png', bbox_inches='tight')
fig2.savefig('plots/combined_plots2.png', bbox_inches='tight')