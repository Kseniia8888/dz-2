def first_word(text):
    word = ""
    started = False

    for ch in text:
        if ch.isalpha() or ch == "'":
            word += ch
            started = True
        else:
            if started:
                break

    return word


assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print("OK")