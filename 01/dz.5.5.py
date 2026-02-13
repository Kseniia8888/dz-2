import keyword

name = input()

def check_name(name):
    if not name:
        return False

    if name.count("_") > 1:
        return False

    if name[0].isdigit():
        return False

    for ch in name:
        if not (ch.islower() or ch.isdigit() or ch == "_"):
            return False

    if name in keyword.kwlist:
        return False

    return True


print(check_name(name))