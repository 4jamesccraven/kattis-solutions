CODEC = {
         'a': '.-',
         'b': '-...',
         'c': '-.-.',
         'd': '-..',
         'e': '.',
         'f': '..-.',
         'g': '--.',
         'h': '....',
         'i': '..',
         'j': '.---',
         'k': '-.-',
         'l': '.-..',
         'm': '--',
         'n': '-.',
         'o': '---',
         'p': '.--.',
         'q': '--.-',
         'r': '.-.',
         's': '...',
         't': '-',
         'u': '..-',
         'v': '...-',
         'w': '.--',
         'x': '-..-',
         'y': '-.--',
         'z': '--..',
         '0': '-----',
         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.'
}


def morse(character):
    return CODEC.get(character, '')


def morse_word(word):
    new = ''
    for char in word:
        new = new + morse(char)

    return new


def main():
    inp = input().lower()
    keys = [k for k in CODEC.keys()]

    valid = False

    for char in inp:
        if char in keys:
            valid = True
            break

    if not valid:
        print(0)
        return

    morse_string = morse_word(inp)

    length = len(morse_string)
    even = length % 2 == 0

    sub_len = (length // 2)

    first_string = morse_string[0:sub_len]

    last_start = sub_len if even else sub_len + 1

    last_string = (morse_string[last_start:])
    last_string = last_string[::-1]

    print(1 if first_string == last_string else 0)


if __name__ == '__main__':
    main()
