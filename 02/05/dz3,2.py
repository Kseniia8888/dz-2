ist = [3,6,9,26]
if len(ist) <= 1:
    print(ist)
else:
    last = ist.pop()
    ist.insert(0,last)
    print(ist)
