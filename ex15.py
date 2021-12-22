from sys import argv
#here sys is package & argv is feature from that package
#So we are just saying get the "argv" feature from that "sys" package.

script, filename = argv
#get argv commond line arguments (when running the file) and assigning it to two veriable

txt = open(filename)
# here we are opening veriable filename and assigning it to txt veriables

print(f"here's your file {filename}:")
#here we are using "f" type formating to insert veriable filename and then printing it
print(txt.read())
#here we are using another new fucntion "read". here we are saying read txt veriable and then print it

print("Type the filename again:")
file_again = input(">")
#here we are simply printing string to understan the user what he have to give input
#then we asking for input and assinging it to file_again veriables

txt_again = open(file_again)
#Same as above

print(txt_again.read())
