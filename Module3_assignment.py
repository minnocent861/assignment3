#7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things=["mozzarella", "cinderella", "salmonella"]
#7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
things[1] = things[1].capitalize
print("After capitalizing the person element",things)
#7.6 Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper
print("After making the cheesy element all uppercase",things)
#7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
things[-1] = things[-1].upper
print("After deleting the disease element",things)