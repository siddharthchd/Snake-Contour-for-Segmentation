import matplotlib.pyplot as plt

circle = plt.Circle((0, 0), 0.2, color='black')

fig, ax = plt.subplots() 
ax.add_artist(circle)

