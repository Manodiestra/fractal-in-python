import mandelbrot
import mandelbrot3
import julia
import random

def makeFractal(config_dict):
    # Make and return a fractal object
    witch = random.randint(0, 2)
    type = config_dict["type:"].lower()
    if type == mandelbrot:
        if witch == 0:
            m = mandelbrot.Mandelbrot()
        else:
            m = mandelbrot3.mandelbrot3()
        return m
    else:
        j = julia.julia()
        return j
        
