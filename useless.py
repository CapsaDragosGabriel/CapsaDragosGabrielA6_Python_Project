def getNameHard(path):
    """
    obtine numele procesului din calea executabilului
    """
    i = 1
    ok = False
    while path[-i] != "\\" and i < len(path):
        i += 1
        if path[-i] == "\\":
            ok = True
    if ok:
        poz = len(path) - i + 1
        numeProces = path[poz:]
        # print("NUME PROCES",numeProces[:len(numeProces)-4])
    else:
        numeProces = path
    return numeProces