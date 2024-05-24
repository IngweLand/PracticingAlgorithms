import matplotlib.pyplot as plt

# Set the size of the figure
plt.figure(figsize=(8, 8))

# Draw a 100x100 grid
plt.grid(True)
plt.xlim(0, 30)
plt.ylim(0, 30)

# Set the grid style
plt.gca().set_xticks(range(0, 31, 1), minor=True)
plt.gca().set_yticks(range(0, 31, 1), minor=True)
plt.gca().grid(which='minor', color='black', linestyle='-', linewidth=0.5)

plt.show()
