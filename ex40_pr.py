mystuff_dict = {'apple': "I AM APPLE"}
print(mystuff_dict['apple'])

import applefn
applefn.apple()

print(applefn.vfn)

print(mystuff_dict['apple']) # get apple from dict
applefn.apple() # get apple from the module
applefn.vfn

class mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousnd years between"

    def apple_c(self):
        print("I AM CLASSY APPLES!")

thing = mystuff()
print(thing.tangerine)
thing.apple_c()

print("I now have three wy to get things from things:")

print("dict style")
print(mystuff_dict['apple'])

print("module style")
applefn.apple()

print("Class style")
thing = mystuff()
thing.apple_c()
print(thing.tangerine)
