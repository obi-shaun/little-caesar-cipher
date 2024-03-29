import argparse
import string

alphabet = [letter for letter in string.ascii_lowercase]

parser = argparse.ArgumentParser(description="apply caesar cipher")
parser.add_argument("--message", type=str, help="message to encode or decode", required=True)
parser.add_argument("--shift", type=int, help="value of shift", required=True)
args = parser.parse_args()


def apply_caesar_cipher(message, shift=1):
    for i in range(len(message)):
        if message[i].isalpha():
            position_in_alphabet = alphabet.index(message[i].lower())
            position_in_alphabet = (position_in_alphabet + shift) % len(alphabet)
            replacement_letter = alphabet[position_in_alphabet]
            if message[i].isupper():
                replacement_letter = replacement_letter.upper()
            message = message[:i] + replacement_letter + message[i + 1:]
    return message


print(apply_caesar_cipher(args.message, args.shift))
