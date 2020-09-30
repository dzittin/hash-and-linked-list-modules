# hash-and-linked-list-modules
A hash table that uses linked lists to handle collisions. Two files: the hash table manager and the linked list code.

Having fun trying to get my coding skills back after a long hiatus. The has table seems to run quite fast providing that collisions do not
create execssively long lists. Emperically, I have observed that if the table size (implemented as a list) is equal to the expected number of hash
entries performance is good. I based "good performance" on observing that around 90% of the collision lists had 1 - 3 members and the count of lists of 4 or more was
proportionally small.

There is commented code at the bottom of hash.py that when uncommented will present a human digestable view of the hash table by
printing the collision lists (if the print hash table parameter is set to True) and will produce a graph of linked lists lengths.
