out={}
for i in range(10241, 10496): 
    print(chr(i))
    print("⣿⣿⣿")
    print(f"⣿{chr(i)}⣿")
    print("⣿⣿⣿")
    inp=list(reversed(("000000000000000" + bin(i)[2:])[-8:]))
    out[(
        (inp[0] == "1", inp[3] == "1"),
        (inp[1] == "1", inp[4] == "1"),
        (inp[2] == "1", inp[5] == "1"),
        (inp[6] == "1", inp[7] == "1"),
    )]=chr(i)
    print(out)