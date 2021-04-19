testDisplay = [
    [True, True, True, True, True, True, True, False, True, True],
    [True, False, False, False, True, True, True, False, False, False],
    [True, True, False, False, True, True, False, True, True, False],
    [True, True, False, False, False, False, True, True, False, False],
    [False, True, False, False, True, True, True, False, True, False],
    [False, True, True, True, True, True, True, True, False, True],
    [True, True, True, True, False, False, False, True, False, True],
    [False, False, True, True, True, True, False, True, True, False],
    [True, False, False, False, False, True, False, True, False, True],
    [False, True, False, True, True, True, False, True, True, True],
    #[False, True, True, True, False, True, False, True, False, True],
]

char = "⠁".encode()
chars = []
bmp={}
for i in range(128, 192):
    chars.append((char[:2] + bytes([i])).decode())
out = "charDict = {\n"
for i, j in zip(range(1000), chars):
    print(
        "⠿ ⠿ ⠿\n"
        f"⠿ {j} ⠿\n"
        "⠿ ⠿ ⠿\n"
    )
    inp=input()
    if len(inp) != 6: print("error")
    ch=[]
    for j in inp:
        if j=="n":
            ch.append(True)
        if j==" ":
            ch.append(False)
    out += f"    \"{chars[i]}\": [\n"
    out +=  "        {},\n".format(str([ch[0], ch[1]]))
    out +=  "        {},\n".format(str([ch[2], ch[3]]))
    out +=  "        {},\n".format(str([ch[4], ch[5]]))
    out +=  "    ],\n"
    print(out)