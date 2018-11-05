from .MyMandelbrot import pixelPicker
from .MyJulia import pixelPicker2
from tkinter import PhotoImage


def paint(config_dict, myGradient):
    img_size = config_dict["pixels:"]
    img_type = config_dict["type:"]
    center_x = config_dict["centerX:"]
    center_y = config_dict["centerY:"]
    axis_length = config_dict["axisLength:"]
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
            print(f"{imagename} (640x640) {'=' * pips}{'_' * (64 - pips)} {pct:.0%}", end='\r', file=sys.stderr)
        for row in range(640):
            x = minimum[0] + col * pixelsize
            y = minimum[1] + row * pixelsize
            if img_type == "mandelbrot":
                color = myGradient[pixelPicker(complex(x, y))]
            else:
                color = myGradient[pixelPicker2(complex(x, y))]
            img.put(color, (col, row))
    print(f"{imagename} ({img_size}x{img_size}) ================================================================ 100%",
          file=sys.stderr)
    return img
