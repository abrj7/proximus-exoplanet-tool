import matplotlib
matplotlib.use('Agg') # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import os

def generate_planet_image(planet_name, radius, temp, output_dir='static/generated'):
    """
    Generates a 3D sphere visualization of a planet using Matplotlib.
    """
    filename = f"{planet_name}.png"
    filepath = os.path.join(output_dir, filename)
    
    if os.path.exists(filepath):
        return filename

    # Create figure
    fig = plt.figure(figsize=(5, 5), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    # Sphere data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Color map based on temperature
    # Cold (Blue/White) -> Habitable (Green/Blue) -> Hot (Red/Orange)
    if temp < 250:
        colors = ['#ffffff', '#aaddff', '#004488'] # Ice world
    elif 250 <= temp <= 320:
        colors = ['#004488', '#228822', '#88aa00', '#ffffff'] # Earth-like
    else:
        colors = ['#440000', '#aa4400', '#ffcc00'] # Lava world
        
    cmap = LinearSegmentedColormap.from_list("planet_theme", colors)
    
    # Generate texture noise
    noise = np.random.rand(100, 100)
    
    # Plot surface
    ax.plot_surface(x, y, z, facecolors=cmap(noise), rstride=1, cstride=1, shade=True)
    
    # Remove axes
    ax.set_axis_off()
    
    # Save
    plt.savefig(filepath, bbox_inches='tight', pad_inches=0, facecolor='black')
    plt.close()
    
    return filename
