out={}
for i, char in enumerate(range(10240, 10496)): 
    print(i)
    print("⣿⣿⣿")
    print(f"⣿{chr(char)}⣿")
    print("⣿⣿⣿")
    inp=list(reversed(("000000000000000" + bin(i)[2:])[-8:]))
    out[(
        (inp[0] == "1", inp[3] == "1"),
        (inp[1] == "1", inp[4] == "1"),
        (inp[2] == "1", inp[5] == "1"),
        (inp[6] == "1", inp[7] == "1"),
    )]=chr(char)
    print(out)