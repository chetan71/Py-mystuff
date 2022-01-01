from sys import argv# here we are using argv for asking user for arguments

script, input_file = argv# we assign commond line arguments to veriable


def print_all(f):#here we are defining funtṇ "print_all"
    print(f.read())#here we are saying read given file then print it

def rewind(f):
    f.seek(0)
'''here the most IMP thing seek, here we sending refrance point back to 0'''

def print_a_line(line_count, f):
    print(line_count, f.readline())#here we are using readline function
    # to read only line on which the refrancepoint is


current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind. kind of like a tape.")

rewind(current_file)

print("lET'S PRINT THREE LINES:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)
