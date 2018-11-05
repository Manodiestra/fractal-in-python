def pixelPicker(c):
    z = complex(0, 0) # z0
    for i in range(100):
        z = z * z + c
        if abs(z) > 2:
            return i
