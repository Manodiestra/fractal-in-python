from tkinter import Tk, Canvas, PhotoImage, mainloop
from .MyMandelbrot import pixelPicker
from .MyJulia import pixelPicker2

def paint(fractal, imagename, config_dict):
    img_size = config_dict["pixels:"]
    img_type = config_dict["type:"]

    minimum = ((fractal['centerX'] - (fractal['axisLength'] / 2.0)),
               (fractal['centerY'] - (fractal['axisLength'] / 2.0)))
    maximum = ((fractal['centerX'] + (fractal['axisLength'] / 2.0)),
               (fractal['centerY'] + (fractal['axisLength'] / 2.0)))

    pixelsize = abs(maximum[0] - minimum[0]) / img_size
    load_chunck = 64
    portion = int(img_size / load_chunck)
    for col in range(img_size):
        if col % portion == 0:
            # Update the status bar each time we complete 1/64th of the rows
            pips = col // portion
            pct = col / img_size
            print(f"{imagename} (640x640) {'=' * pips}{'_' * (64 - pips)} {pct:.0%}", end='\r', file=sys.stderr)
        for row in range(640):
            x = minimum[0] + col * pixelsize
            y = minimum[1] + row * pixelsize
            if img_type == "mandelbrot":
                color = gradient[pixelPicker(complex(x, y))]
            else:
                color = pixelPicker2(complex(x, y))
            img.put(color, (col, row))
    print(f"{imagename} ({img_size}x{img_size}) ================================================================ 100%",
          file=sys.stderr)
    return img
