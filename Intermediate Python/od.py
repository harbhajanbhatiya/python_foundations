from collections import OrderedDict, defaultdict
my_dict = {'a': 1, 'b': 2, 'c': 3} #It's like regular dictionaries, but it remembers the order in which the items were added.
#Now simple dictionaries also remember the order of items as of Python 3.7, but ordereddict has some additional features.
# the features of ordereddict are:
# 1. Reversing the order of items.
# 2. Moving an item to the end or beginning of the dictionary.
# 3. Comparing two ordereddict objects for equality, taking into account the order of items.
# 4. Creating a new ordereddict object from an existing one, preserving the order of items.
# 5. Creating a new ordereddict object from an iterable of key-value pairs, preserving the order of items.
my_ordered_dict = OrderedDict(my_dict)
print(my_ordered_dict)  #It returns an ordereddict with the items in the order they were added.
my_ordered_dict.move_to_end('b') #It moves the item with key 'b' to the end of the dictionary.
print(my_ordered_dict)  #It returns an ordereddict with the items in the order they were added, with 'b' moved to the end.


#The only difference between a regular dictionary and a defaultdict is that a defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory. If no default factory is provided, it defaults to None.
my_default_dict = defaultdict(int) #It creates a defaultdict with a default factory of int,
my_default_dict['a'] = 1
my_default_dict['b'] = 2
print(my_default_dict)  #It returns a defaultdict with the items in the order they were added.
print(my_default_dict['c'])  #It returns the default value of int, which is 0, since 'c' does not exist in the dictionary.

