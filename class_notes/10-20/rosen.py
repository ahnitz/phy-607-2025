import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import rosen

# Create a grid of points in the x-y plane
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)

# Initialize an array to store Rosenbrock function values
Z = np.zeros_like(X)

# Calculate the Rosenbrock function for each point on the grid
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = rosen([X[i, j], Y[i, j]])

# Create the plot
plt.figure(figsize=(8, 6))
plt.pcolormesh(X, Y, Z, cmap='plasma')
plt.title('Rosenbrock Function (using scipy.optimize.rosen)')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='f(x, y)')
plt.show()
