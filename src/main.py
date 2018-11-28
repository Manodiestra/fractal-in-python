import Config
import ImagePainter
import Gradient
import Color
from tkinter import Tk, Canvas, mainloop


def makeConfigDict(frac):
    return Config.makeObj(frac)


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
            print("The supported file extension are .png or .gif\n")
    return extension_name


def getGradient(config_dictionary):
    steps = int(config_dictionary["iterations:"])
    start_color = Color.Color(255, 0, 0)
    end_color = Color.Color(0, 0, 277)
    return Gradient.gradient(start_color, end_color, steps)


def nameImage():
    getting_name = True
    while getting_name:
        image_name = input("\nWhat do you want to\nname the output file?\n(do not include the extension)\n")
        if type(image_name) == str:
            print("You selected " + image_name)
            getting_name = False
        else:
            print("The file name cannot be a number or symbol.")
    return image_name

# Run finctions and gather data
frac_name = Config.getConfig()
image = nameImage()
config_dict = makeConfigDict(frac_name)
img_size = int(getSize(config_dict))
file_extension = getFileExtension()
myGradient = getGradient(config_dict)

# Generate the image
window = Tk()
img = ImagePainter.paint(config_dict, myGradient, image)

# Display the image on the screen
canvas = Canvas(window, width=img_size, height=img_size, bg=myGradient[0])
canvas.pack()
canvas.create_image((img_size//2, img_size//2), image=img, state="normal")

# Save the picture to a file
img.write(image + file_extension)
print(f"Wrote picture {image}.gif")
mainloop()
