import string
import keyword

name = input()

def check_name(name):
    if not name:
        return False

    if name[0].isdigit():
        return False

    if any(c.isupper() for c in name):
        return False

    for c in name:
        if c == " ":
            return False
        if c in string.punctuation and c != "_":
            return False

    if name in keyword.kwlist:
        return False

    if set(name) == {"_"} and len(name) > 1:
        return False

    return True


print(check_name(name))