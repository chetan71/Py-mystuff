ten_things = "Apples Oranges Crews Telephone Light Sugar"

stuff = ten_things.split(' ')
print(len(stuff))
print(stuff)

print("Wait there are not 10 things in that list. let's fix that.")

more_stuff = ["Day", "Night", "Song", "Fresbee", "Corn", "Banana", "Gril", "Boy"]
print(more_stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
else:
    print("now there are 10 items")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar
