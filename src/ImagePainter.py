import FractalFactory
import sys
from tkinter import PhotoImage


def paint(config_dict, myGradient, imagename):
    img_size = int(config_dict["pixels:"])
    fractal = FractalFactory.makeFractal(config_dict)
    center_x = float(config_dict["centerx:"])
    center_y = float(config_dict["centery:"])
    axis_length = float(config_dict["axislength:"])
    grad_size = int(config_dict["iterations:"])
    img = PhotoImage(width=img_size, height=img_size)

    minimum = ((center_x - (axis_length / 2.0)),
               (center_y - (axis_length / 2.0)))
    maximum = ((center_x + (axis_length / 2.0)),
               (center_y + (axis_length / 2.0)))

    pixelsize = abs(maximum[0] - minimum[0]) / img_size
    load_chunck = 64
    portion = int(img_size / load_chunck)
    for col in range(img_size):
        if col % portion == 0:
            # Update the status bar each time we complete 1/64th of the rows
            pips = col // portion
            pct = col / img_size
            print(f"{imagename} ({img_size}x{img_size}) {'=' * pips}{'_' * (64 - pips)} {pct:.0%}", end='\r', file=sys.stderr)
        for row in range(img_size):
            x = minimum[0] + col * pixelsize
            y = minimum[1] + row * pixelsize
            #print(fractal.count(complex(x, y), grad_size))
            color = myGradient[fractal.count(complex(x, y), grad_size)]
            img.put(str(color), (col, row))
    print(f"{imagename} ({img_size}x{img_size}) ================================================================ 100%",
          file=sys.stderr)
    return img
