#here I'm we are giving arguments to a fucntion
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")# here I'm inserting arguments in it
    print(f"You hace {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get ablanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)# here I'm giving arguments value


print("OR, we canuse variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)