def StringToDict(s):
    RES = dict()
    for e in set(s):
        RES[e] = 0
    for e in s:
        RES[e] += 1
    return RES
