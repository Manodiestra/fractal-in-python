import Gradient
import Color


class RedBlue(Gradient):

    def gradient(start, stop, steps):
        start = 0
        stop = 255
        dRed = (stop.r - start.r) / (steps - 1)
        dGrn = (stop.g - start.g) / (steps - 1)
        dBlu = (stop.b - start.b) / (steps - 1)
        return list(
            map(lambda n: Color.Color((n * dRed) + start.r, (n * dGrn) + start.g, (n * dBlu) + start.b), range(steps)))
