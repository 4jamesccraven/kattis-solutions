from string import ascii_uppercase
from sys import stdin

_chars = ascii_uppercase + '_.,?'

_morse = [
    '.-',
    '-...',
    '-.-.',
    '-..',
    '.',
    '..-.',
    '--.',
    '....',
    '..',
    '.---',
    '-.-',
    '.-..',
    '--',
    '-.',
    '---',
    '.--.',
    '--.-',
    '.-.',
    '...',
    '-',
    '..-',
    '...-',
    '.--',
    '-..-',
    '-.--',
    '--..',
    '..--',
    '---.',
    '.-.-',
    '----',
]

ENCODER = dict(zip(_chars, _morse))
DECODER = dict(zip(_morse, _chars))
TABLE = str.maketrans(ENCODER)


def decode(msg: str) -> str:
    lens = [len(ENCODER[val]) for val in msg][::-1]


    msg = msg.translate(TABLE)

    text = ''
    for length in lens:
        val = DECODER[msg[:length]]
        msg = msg[length:]
        text = text + val

    return text



def main() -> None:
    msgs: list[str] = [line.strip() for line in stdin]

    for msg in msgs:
        print(decode(msg))


if __name__ == '__main__':
    main()
