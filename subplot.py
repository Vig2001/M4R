import matplotlib.pyplot as plt
import numpy as np

# Define the triangle vertices
A1, A2, A3 = np.array([0, 1]), np.array([-1, 0]), np.array([1, 0])

# Point inside the triangle
P = np.array([0.2, 0.4])  # Adjust coordinates to position correctly

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plotting the triangle
ax.plot([A1[0], A2[0], A3[0], A1[0]], [A1[1], A2[1], A3[1], A1[1]], 'ko-')
ax.plot([P[0], A1[0]], [P[1], A1[1]], 'b-', label='$l_1$')
ax.plot([P[0], A2[0]], [P[1], A2[1]], 'b-', label='$l_2$')
ax.plot([P[0], A3[0]], [P[1], A3[1]], 'b-', label='$l_3$')
ax.text(A1[0], A1[1], '$A_1$', fontsize=12, ha='right', va='bottom')
ax.text(A2[0], A2[1], '$A_2$', fontsize=12, ha='right', va='top')
ax.text(A3[0], A3[1], '$A_3$', fontsize=12, ha='left', va='top')
ax.text(P[0], P[1], 'P', fontsize=12, color='blue', ha='center', va='center')

# Adjust layout and aspect ratio
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')  # Turn off the axis

# Save the figure
plt.savefig('plots/triangle_diagram_single.png', format='png', dpi=300)  # Saves the figure as a PNG file with 300 DPI

# Show the plot
plt.show()
