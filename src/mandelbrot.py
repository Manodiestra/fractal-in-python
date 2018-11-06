def pixelPicker(c, iterations):
    z = complex(0, 0) # z0
    for i in range(iterations - 1):
        z = z * z + c
        if abs(z) > 2:
            return i
    return iterations - 1