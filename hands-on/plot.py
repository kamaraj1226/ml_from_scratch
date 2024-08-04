"""
For plotting
"""

try:
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.interpolate import make_interp_spline

    # from matplotlib.animation import FuncAnimation as fnca

except ImportError as ImpErr:
    raise ImportError("Missing Required packages") from ImpErr


class Plot:
    """
    For plotting
    """

    # pylint: disable= import-outside-toplevel
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.graph = None
        self.pause = 1

    def plot_2d(self, x, y):
        """
        2 Dimension plotting
        """
        x = np.array(x)
        y = np.array(y)
        x_y_splint = make_interp_spline(x, y)

        x_ = np.linspace(x.min(), x.max(), 500)
        y_ = x_y_splint(x_)

        if not self.graph:
            self.graph = self.ax.plot(x_, y_)

        plt.show()

        # def update(frame):


def main():
    """
    Main function to test this module
    """
    x1_values = [60, 67, 71, 75, 78]
    x2_values = [22, 24, 15, 20, 16]

    p = Plot()
    p.plot_2d(x1_values, x2_values)


if __name__ == "__main__":
    main()
