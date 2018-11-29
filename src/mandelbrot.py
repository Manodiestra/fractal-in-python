from Fractal import Fractal


class Mandelbrot(Fractal):

    def __init__(self):
        super().__init__()
        self.z = complex(0, 0)
        self.c = complex(0, -1)

    def count(self, c, iterations):
        self.c = c
        self.z = complex(0, 0)
        for i in range(iterations):
            self.z = self.z * self.z + self.c
            if abs(self.z) > 2:
                return i
        return iterations - 1

