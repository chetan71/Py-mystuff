from sys import argv

script, filename = argv
txt = open(ex15_sample_txt_file.py)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
