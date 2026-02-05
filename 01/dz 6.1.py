import string

def letters_range(s):
    start, end = s.split('-')
    letters = string.ascii_letters
    start_index = letters.index(start)
    end_index = letters.index(end)
    return letters[start_index:end_index + 1]

s = input()
print(letters_range(s))