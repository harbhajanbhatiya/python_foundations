from collections import deque #It is a double ended queue, which means that you can add and remove elements from both ends of the queue. It is implemented as a doubly linked list, which means that it has a head and a tail, and each element has a reference to the previous and next element in the list. It is more efficient than a list for adding and removing elements from the ends of the queue, but it is less efficient for accessing elements in the middle of the queue.

my_deque = deque([1, 2, 3, 4, 5])
my_deque.append(6) #It adds an element to the right end of the deque.
print(my_deque)  #It returns a deque with the elements in the order they were added.
my_deque.appendleft(0) #It adds an element to the left end of the deque.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.pop() #It removes an element from the right end of the deque.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.popleft() #It removes an element from the left end of the deque.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.extend([7, 8, 9]) #It adds multiple elements to the right end of the deque.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.extendleft([-2, -1]) #It adds multiple elements to the left end of the deque.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.rotate(2) #It rotates the deque to the right by 2 elements.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.rotate(-2) #It rotates the deque to the left by 2 elements.
print(my_deque)  #It returns a deque with the elements in the order they were
my_deque.clear() #It removes all elements from the deque.
print(my_deque)  #It returns an empty deque.
