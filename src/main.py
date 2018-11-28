import Config
import ImagePainter
import Gradient
import Color
import FractalFactory
import sys
from tkinter import Tk, Canvas, mainloop


def getSize(config_dict):
    return config_dict["pixels:"]


def getFileExtension():
    getting_type = True
    while getting_type:
        extension_name = input("\nWhat file type would\nyou like to save the image as?\n")
        if extension_name == ".png" or extension_name == ".gif":
            print("You selected " + extension_name)
            getting_type = False
        else:
            print("Supported file extensions are .png or .gif\n")
    return extension_name


def getGradient(config_dictionary):
    steps = int(config_dictionary["iterations:"])
    start_color = Color.Color(255, 0, 0)
    end_color = Color.Color(0, 0, 277)
    return Gradient.gradient(start_color, end_color, steps)


def nameImage():
    tempString = sys.argv[1]
    tempList = tempString.split(".")
    return tempList[0]


# Run functions and gather data
image = nameImage()
config_dict = Config.getConfigDict()
fractal = FractalFactory.makeFractal(config_dict)
img_size = int(getSize(config_dict))
file_extension = getFileExtension()
myGradient = getGradient(config_dict)

# Generate the image
img = ImagePainter.paint(config_dict, myGradient, image)

# Display the image on the screen
window = Tk()
canvas = Canvas(window, width=img_size, height=img_size, bg=myGradient[0])
canvas.pack()
canvas.create_image((img_size//2, img_size//2), image=img, state="normal")

# Save the picture to a file
img.write(image + file_extension)
print(f"Wrote picture {image}.gif")
mainloop()
