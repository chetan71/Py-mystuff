import sys

script, encoding, error = sys.argv


def main(raw_bytes_file, encoding, errors):
    line = raw_bytes_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(raw_bytes_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    strings = next_lang.decode(encoding, errors=errors)
    cooked_string = strings.encode(encoding, errors=errors)
    print(strings, "<===>", cooked_string)


lang = open("raw.txt", encoding="utf-8")


main(lang, encoding, error) # here we put arrguments in "main" funtion which is lang, encoding & error
# but encoding & error are the arrguments which we will provide it when we run this script which means these two
# arrguments given form line 3 which is argv.sys line
# It's like we are puting veriable value as veriable.....?
