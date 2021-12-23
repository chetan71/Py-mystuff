from sys import argv

script, filename = argv

print ("now we will begain real coding \n lets see will it print on new line")

txt = open(filename)
R = txt.read()
print(R)
