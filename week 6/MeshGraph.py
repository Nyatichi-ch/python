import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#use seaborn style for better aesthetics
sns.set(style="darkgrid")

#create a fucntion to plot a mesh graph
def plot_mesh_graph(x, y, z):
    plt.figure(figsize=(8,6))
    X, Y = np.meshgrid(x, y)

    #plot the surface
    surf = plt.pcolormesh(X, Y, z, shading='auto', cmap='viridis', edgecolor='k')
#axes labels and title
    ax.set_xlabel('X-distance')
    ax.set_ylabel('Y-distance')
    

    plt.title('Mesh Graph Example')
    plt.show()

    