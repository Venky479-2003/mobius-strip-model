import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1, w=0.3, n=100, twists=1):
        self.R, self.w, self.n, self.twists = R, w, n, twists
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
        u, v, t = self.U, self.V, self.twists
        phi = t * u / 2
        x = (self.R + v * np.cos(phi)) * np.cos(u)
        y = (self.R + v * np.cos(phi)) * np.sin(u)
        z = v * np.sin(phi)
        return x, y, z

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='plasma', edgecolor='none')
        ax.set_title(f"{self.twists}-Twist Möbius Strip")
        plt.tight_layout()
        plt.show()


strip = MobiusStrip(R=1, w=0.5, n=200, twists=1)  
strip.plot()