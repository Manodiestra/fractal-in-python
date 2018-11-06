def pixelPicker2(z, iterations):
    c = complex(-1, 0) # c0
    for i in range(iterations):
        z = z * z + c
        if abs(z) > 2:
            return i
    return iterations - 1