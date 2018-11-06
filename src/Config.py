import glob
files = ["elephants.frac", "fulljulia.frac", "fullmandelbrot.frac", "hourglass.frac", "lakes.frac", "leaf.frac", "seahorse.frac", "spiral0.frac", "spiral1.frac"]


def getConfig():
#    files = glob.glob('../data/*.frac')
    getting_name = True
    while getting_name:
        config_name = input("\nWhat is the name of the\nconfig file you want to use?\n")
        if config_name in files:
            print("You selected " + config_name)
            getting_name = False
        else:
            print("You have to pick an internal config file\n")
            for names in files:
                print(names)
    return config_name


def makeObj(name):
    config_dict = {}
    file = open("data/" + name, "r")
    for line in file:
        parts = line.split(' ')
        config_dict[parts[0]] = parts[len(parts)-1].replace("\n", "")
    return config_dict

