from collections import Counter
my_string = "aaaaabbbbcccc"
my_counter = Counter(my_string)
print(my_counter)  #It returns a dictionary with the count of each character in the string.
print(my_counter.items())  #It returns a list of tuples with the character and its count.
print(my_counter.keys())  #It returns a list of characters in the string.
print(my_counter.values())  #It returns a list of counts of each character in the string.
print(my_counter.most_common(2))  #It returns a list of the two most common characters and their counts.
print(my_counter.most_common(2)[0][0])  #It returns the most common character in the string.
print(list(my_counter.elements()))  #It returns an iterator over the elements in the string, repeating each character as many times as it appears in the string.