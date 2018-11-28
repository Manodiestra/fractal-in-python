from Fractal import Fractal


class mandelbrot3(Fractal):

    def __init__(self):
        super().__init__()

    def count(self, c, iterations):
        z = complex(0, 0) # z0
        for i in range(iterations):
            z = z * z * z + c
            if abs(z) > 2:
                return i
        return iterations - 1

