from sys import argv
#from os.path import exists

script, from_file, to_file =argv


# we could do these two on one line, how?
in_file = open(from_file).read()


# print(f"The input file is {len(in_file)} bytes long")

#print (f"Does the output file exist? {exists(to_file)}")

out_file = open(to_file, 'w').write(in_file)


#out_file.close()
