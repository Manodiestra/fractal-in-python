import Config
import ImagePainter
import GradientFactory
import sys
from tkinter import Tk, Canvas, mainloop


def getSize(config_dict):
    return config_dict["pixels:"]


def getGradient(config_dictionary):
    steps = int(config_dictionary["iterations:"])
    gradient = GradientFactory.makeGradient()
    return gradient.gradient(steps)


def nameImage():
    tempString = sys.argv[1]
    tempList = tempString.split(".")
    return tempList[0]


# Run functions and gather data
image = nameImage()
config_dict = Config.getConfigDict()
img_size = int(getSize(config_dict))
myGradient = getGradient(config_dict)

# Generate the image
window = Tk()
img = ImagePainter.paint(config_dict, myGradient, image)

# Display the image on the screen
canvas = Canvas(window, width=img_size, height=img_size, bg=myGradient[0])
canvas.pack()
canvas.create_image((img_size//2, img_size//2), image=img, state="normal")

# Save the picture to a file
img.write(image + ".bmp")
print(f"Wrote picture {image}.bmp")
mainloop()
