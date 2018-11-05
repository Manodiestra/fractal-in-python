from .Config import makeObj
from .ImagePainter import paint
from .Gradient import gradient
from .Color import Color
from tkinter import Tk, Canvas, PhotoImage, mainloop


def makeConfigDict():
    return makeObj()


def getSize(config_dict):
    return config_dict["pixels:"]


def getFileExtension():
    getting_type = True
    while getting_type:
        extension_name = input("What file type would\nyou like to save the image as?\n")
        if extension_name == ".png" or extension_name == ".gif":
            print("You selected " + extension_name)
            getting_type = False
        else:
            print("The supported file extension are .png or .gif\n")
    return extension_name




config_dict = makeConfigDict()
img_size = getSize(config_dict)
file_extension = getFileExtension()
start_color = Color(200, 0, 200)
end_color = Color(11, 300, 22)
this_step = config_dict["Iterations:"]
paint()




window = Tk()
img = PhotoImage(width=img_size, height=img_size)
makePicture(images[image], image)

# Display the image on the screen
canvas = Canvas(window, width=img_size, height=img_size, bg=gradient[0])
canvas.pack()
canvas.create_image((img_size//2, img_size//2), image=img, state="normal")

# Save the picture to a file
img.write(image + file_extension)
print(f"Wrote picture {i}.gif")
mainloop()
