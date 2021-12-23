"""Assignment No. 4-5
4. Get rid of the lines 10-15 where you use input and run the script again.
5. Use only input and try the script that way. Why is one way of getting the
filename better than another?"""
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

txt1 = open(input("FILENAME>"))# I didn't put double quests so I got error
print(f"this is the file name {filename}")

print(txt1.read())
