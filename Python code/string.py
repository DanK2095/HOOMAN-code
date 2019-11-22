def isstring(x):
    y = 0 
    w = []
    for i in x:
        if ord(i) <= 57 and ord(i) >= 48:
            w.append(1)
        else:
            w.append(0)
    for i in w:
        if i != y:
            return False    
        else:
            continue
    
    return True



