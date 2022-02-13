for k in range(97, 100):
    for x in range(3):
        for c in range(10, 13):
            if c == 12 and x == 1: break
            print(chr(k), x, c)
        else:
            print("Finally finished!")
            continue
        print("skip")
        break