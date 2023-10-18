max_iter = 80
scale = 200

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

out = []
if __name__ == "__main__":
    for imaginary in range(-scale, scale):
        line = []
        for real in range(-int(scale * 1.5), int(scale * 0.5)):
            line.append(mandelbrot(complex(real / 200, imaginary / 200)) == max_iter)
        out.append(line)

    for j in range(0, len(out), 4):
        for i in range(0, len(out[0]), 2):
            try:
                char = bytearray([0b11100010, 0b10100000, 0b10000000])
                char[2] = (char[2] & ~0b1)      | 0b1      if out[j][i]         else char[2]
                char[2] = (char[2] & ~0b1000)   | 0b1000   if out[j][i + 1]     else char[2]
                char[2] = (char[2] & ~0b10)     | 0b10     if out[j + 1][i]     else char[2]
                char[2] = (char[2] & ~0b10000)  | 0b10000  if out[j + 1][i + 1] else char[2]
                char[2] = (char[2] & ~0b100)    | 0b100    if out[j + 2][i]     else char[2]
                char[2] = (char[2] & ~0b100000) | 0b100000 if out[j + 2][i + 1] else char[2]
                char[1] = (char[1] & ~0b1)      | 0b1      if out[j + 3][i]     else char[1]
                char[1] = (char[1] & ~0b10)     | 0b10     if out[j + 3][i + 1] else char[1]
                print(char.decode("utf-8"), end="")
            except IndexError:
                print("#", end="")
        print()