a = "cool"
b = "coooooool"
c = "cooooll"
d = "loooooooovvvvvvvvvvveee"

def shorten_word(word):
    b = (None,None)
    new_word = []

    for char in word:
        if not b[0]:
            new_word.append(char)
        elif (b[1], char) != b:
            new_word.append(char)

        b = (b[1], char)

    return ''.join(new_word)

print(shorten_word(a))
print(shorten_word(b))
print(shorten_word(c))
print(shorten_word(d))