formatter = "{} {} {} {}"
""" here we created a veriable in which 4 {} is add & in this curly bracket we are going to add all types of data types.
For Ex. see bellow"""
print(formatter.format(1, 2, 3, 4))

""" Here we are saying that print this formatter veriable, then we are adding number in that
Curly bracket, by using .format method. The sequence of add num or word is exactly same If we didn't provide sequence.
Nomber 1 will goto 1st position, Number 2 will go to 2nd Position, and so on."""

print(formatter.format("one", "two", "three", "four"))
""" Same goes here just differance is this is string & this explain that we can also insert string by using .format method.
Now bellow boolean character is taken."""
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
""" Now here He wanted to print veriable in veriable, I'm also gone try leaving one position keeping emty & see it runs or not"""
print(formatter.format(     # Here he littraly did what he wants. a person who didn't know 'C' of coding, he will be cofused
    "Try your", # Well farget, above he just didn't want to get code to long because if it get longer he will have to scroll
    "It got little borring now.", # horizontally thats why he used ""folder-sub folder"". Means main line is normal but its sub
    "Fine. Zed is asking me to write a poem", # file will have to give some space to show that its in the same ???(the exact word
    "What! me and poem! no way.I will be rally far off the mark" # didn't know) program or code line or group lets see will it run?
    ))
    # Now its time to experiment
    # print(formatter.format(1, "Second", 3)) This Exp. Failed.
    # print ( formatter.format(1, "Second", 3, "four")) This also Failed. So I think it can only be used in same data type.
# The error was UNEXPECTED UNDENT means space, which is I'm using from previous codeline. now lets check all the above code
#     print( formatter.format(1, 2, 3))
# print(formatter.format(1, "Second", 3)) The Error is "IndexError: tuple index out of range"
print ( formatter.format(1, "Second", 3, "four"))
""" It worked perfectly. So that means all position must be filled"""
