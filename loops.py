for x in range(100):
    print("1: " + str(x))
    for y in range(200):
        print("2: " + str(x))
        if y == 50:
            print("3: " + str(x))
            break
    print("4: " + str(x))
