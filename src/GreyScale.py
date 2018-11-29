from Gradient import Gradient
import Color


class GreyScale(Gradient):

    def __init__(self):
        super().__init__()
        self.start_b = 0
        self.start_r = 0
        self.start_g = 0
        self.stop_b = 255
        self.stop_r = 255
        self.stop_g = 255

    def gradient(self, steps):
        dRed = (self.stop_r - self.start_r) / (steps - 1)
        dGrn = (self.stop_g - self.start_g) / (steps - 1)
        dBlu = (self.stop_b - self.start_b) / (steps - 1)
        return list(
            map(lambda n: Color.Color((n * dRed) + self.start_r, (n * dGrn) + self.start_g, (n * dBlu) + self.start_b), range(steps)))
