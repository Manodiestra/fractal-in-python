from .Color import Color


def gradient(start, stop, steps):
    dRed = (stop.r - start.r) / (steps - 1)
    dGrn = (stop.g - start.g) / (steps - 1)
    dBlu = (stop.b - start.b) / (steps - 1)
    return list(
        map(lambda n: Color((n * dRed) + start.r, (n * dGrn) + start.g, (n * dBlu) + start.b), range(steps)))
