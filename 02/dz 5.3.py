import string

text = input("Enter a string: ")

# Remove punctuation and split into words
for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()

# Capitalize each word
hashtag = "#" + "".join(word.capitalize() for word in words)

# Limit length to 140 characters
hashtag = hashtag[:140]

print(hashtag)