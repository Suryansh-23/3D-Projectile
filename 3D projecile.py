import matplotlib.pyplot as plt
import mplcursors as mpt
import numpy as np

plt.style.use("dark_background")


class Projectile:
    def __init__(self):
        self.u, self.theta, self.phi = self.inp()
        self.g = 9.80665
        self.Range, self.timePeriod, self.height = self.precalc()
        self.x = []
        self.y = []
        self.z = []

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")

    def inp(self):
        u = float(input("Give me the initial Velocity (in m/s), u : "))
        theta = np.radians(
            float(input("Give me the polar angle of throw (in degrees), θ : "))
        )
        phi = np.radians(
            float(input("Give me the azimuthal angle of throw (in degrees), φ : "))
        )
        return (u, theta, phi)

    def precalc(self):

        Range = (self.u ** 2) * np.sin(2 * self.theta) / self.g
        timePeriod = 2 * self.u * (np.sin(self.theta)) / self.g
        height = ((self.u * np.sin(self.theta)) ** 2) / (2 * self.g)

        return (Range, timePeriod, height)

    def mainloop(self):

        x = []
        y = []
        z = []
        v = []
        vThrow = self.u * np.cos(self.theta)

        for i in np.arange(0, self.timePeriod, 0.1):

            throwCoord = self.u * np.cos(self.theta) * i
            x.append(throwCoord * np.cos(self.phi))
            y.append(throwCoord * np.sin(self.phi))
            z.append(self.u * np.sin(self.theta) * i - (self.g * (i ** 2)) / 2)
            vDown = self.u * np.sin(self.theta) - self.g * i

            v.append(str(round((vThrow ** 2 + vDown ** 2) ** 0.5, 2)) + " m/s")

        return (x, y, z, v)

    def mainplot(self):

        self.x, self.y, self.z, self.v = self.mainloop()
        main = self.ax.plot(self.x, self.y, self.z, color="red")
        xx, yy = np.meshgrid(range(int(self.Range) + 2), range(int(self.Range) + 2))
        zz = np.zeros((int(self.Range) + 2, int(self.Range) + 2), int)
        self.ax.plot_surface(xx, yy, zz, color="green")

        cr = mpt.cursor(main)
        cr.connect(
            "add",
            lambda sel: sel.annotation.set_text(self.v[round(int(sel.target.index))]),
        )

        plt.show()


if __name__ == "__main__":

    Projectile().mainplot()
