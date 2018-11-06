def pixelPicker2(z):
    c = complex(-1, 0) # c0
    for i in range(100):
        z = z * z + c
        if abs(z) > 2:
            return i