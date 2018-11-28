import mandelbrot
import mandelbrot3
import julia

def makeFractal(config_dict):
    # Make and return a fractal object
    type = config_dict["type:"].lower()
    if type == "mandelbrot":
        print("Mandelbrot fractal picked")
        m = mandelbrot.Mandelbrot()
        return m
    elif type == "mandelbrot3":
        print("Mandelbrot3 fractal picked")
        m3 = mandelbrot3.mandelbrot3()
        return m3
    else:
        j = julia.julia()
        print("julia fractal picked")
        return j

