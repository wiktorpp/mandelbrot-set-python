MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

out1 = []
if __name__ == "__main__":
    for imaginary in range(-200, 200):
        out2 = []
        for real in range(-300, 100):
            out2.append(mandelbrot(complex(real / 200, imaginary / 200)) == MAX_ITER)
        out1.append(out2)

    from semigraphics import braille
    for i in range(0, len(out1), 5):
        for j in range(0, len(out1[0]), 2):
            try:
                x = tuple([tuple(k[j:j+2]) for k in tuple(out1[i:i+4])])
                print(braille[x], end='')
            except:
                print("#", end='')
        print()