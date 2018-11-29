from Fractal import Fractal


class julia(Fractal):

    def __init__(self):
        super().__init__()
        self.z = complex(0, 0)
        self.c = complex(0, -1)

    def count(self, z, iterations):
        self.z = z
        self.c = complex(0, -1)
        for i in range(iterations):
            self.z = self.z * self.z + self.c
            if abs(self.z) > 2:
                return i
        return iterations - 1

