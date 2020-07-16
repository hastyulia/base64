import re

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(bytes_string):
    bit_string = ''
    result = ''
    padding = ''
    while (len(bytes_string) % 3) != 0:
        padding += '='
        bytes_string += b'\x00'
    for byte in bytes_string:
        bin_char = bin(byte).lstrip('0b')
        bin_char = (8 - len(bin_char)) * '0' + bin_char
        bit_string += bin_char
    bin_b64_symbols = re.findall('(\d{6})', bit_string)
    if padding != '':
        bin_b64_symbols = bin_b64_symbols[:-len(padding)]
    for bin_b64_symbol in bin_b64_symbols:
        result += ALPHABET[int(bin_b64_symbol, 2)]
    result += padding
    return result.encode()


if __name__ == '__main__':
    string = input('Enter string: ')
    print(encode(string.encode()))
