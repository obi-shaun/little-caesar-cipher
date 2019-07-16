import argparse
import string

alphabet = [letter for letter in string.ascii_lowercase]

parser = argparse.ArgumentParser(description="apply caesar cipher")
parser.add_argument("--message", type=str, help="message to encode or decode", required=True)
parser.add_argument("--shift", type=int, help="value of shift", required=True)
args = parser.parse_args()


# TODO: account for capitalization
def apply_caesar_cipher(message, shift=1):
    for i in range(len(message)):
        if message[i].isalpha():
            position_in_alphabet = alphabet.index(message[i].lower())
            position_in_alphabet = calculate_shift(position_in_alphabet, shift)
            message = message[:i] + alphabet[position_in_alphabet] + message[i + 1:]
    return message


# TODO: reduce duplicate code
def calculate_shift(position_in_alphabet, shift):
    if not shift <= 0:
        for i in range(shift):
            if position_in_alphabet == len(alphabet) - 1:
                position_in_alphabet = -1
            position_in_alphabet += 1
        return position_in_alphabet
    else:
        for i in range(0, shift, -1):
            if position_in_alphabet == -len(alphabet) + 1:
                position_in_alphabet = 1
            position_in_alphabet -= 1
        return position_in_alphabet


print(apply_caesar_cipher(args.message, args.shift))
