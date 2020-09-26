import linked_list as llist
from collections import Counter  #Needed for diagnosic in bottom part


class my_hash:
    def __init__(self, ht_size = 100):
        """Create a hash table object"""
        self.ht_size  = int(ht_size * 1.0)
        if self.ht_size < 10:
            self.ht_size = 10
        self.hash_table = [llist.linked_list() for i in range(0, self.ht_size)]
        self.count = 0  # Keys in table
        
    def hash_gen(self, key):
        """Generate a hash table index"""
        return hash(key) % self.ht_size
        
    def add(self, key, value):
        """Add unique key, return if key was in table"""
        h_index = self.hash_gen(key)
        if self.hash_table[h_index].head == None: # No list at this index
            self.hash_table[h_index] = llist.linked_list()
            self.hash_table[h_index].add_node(key, value)
            self.count += 1
        else:
            a_list = self.hash_table[h_index]
            if self.find_key_value(key) == None:
                a_list.add_node(key, value)
                self.count += 1
            else:
                return None
        return not None  # Key already in table..nothing done.
    
    def get_ht_count(self):
        """Return count of keys in table"""
        return self.count
    
    def get_node(self, key):
        """Access an individual key node"""
        """in order to change a value"""
        a_list = self.hash_table[self.hash_gen(key)]
        if a_list != None:
            return a_list.find_node(key)
            
    def change_value(self, key, value):
        node = self.get_node(key)
        if node != None:
            node.value = value
            return not None
        return None

    def increment_value(self, key, incrval=1):
        """If the node value is not type int throw value exception"""
        node = self.get_node(key)
        if node == None:
            return None
        if node != None:
            if type(node.value) == int:
                node.value += incrval
            else:
                s = "Key='{}', value '{}' cannot be incremented.".format(node.key, node.value)
                raise ValueError(s)
                
                
    def find_key_value(self, key):
        """Find the value associated with key"""
        return self.hash_table[self.hash_gen(key)].find_value(key)
    
    def delete_key(self, key):
        """Delete a found key"""
        """If key is deleted, return 'not None'"""
        a_list = self.hash_table[self.hash_gen(key)]
        if a_list.head == None or a_list.find_node(key) == None:
            return None
        a_list.delete_node(key)
        self.count -= 1
        return not None
    
    def grow_ht(self):
        """Grow the table if there are too many collisions"""
        """Tables whose size is at leat 80% of the key count"""
        """tend to peform well where at least 90% of the collisions"""
        """are in lists whose length is 3 or less"""
        pass 
    
# Uncomment from next line to bottom to visualize hash table linked list lengths.

#     def dump_table_contents(self, full_dump):
#         """Dump the contents of a hash table"""
#         """For debugging and analysis"""
#         counter = Counter()
#         for llnkedlst in self.hash_table:
#             lst = llnkedlst.print_list()
#             if lst != None:
#                 list_len = len(lst)
#                 counter[len(lst)] += 1
#                 if full_dump:
#                     print("{} {}".format(list_len, lst))
#         cnt_list = [i for i in counter.items()]
#         cnt_list.sort()
#         return cnt_list
    
# import random
# def really_ugly_word(char_list):
#     """Generate random string lengths to test hashing"""
#     s = ""
#     word_len = random.randrange(1, 14 + 1)
#     for w in range(1, word_len + 1):
#         c = random.choice(char_list)
#         if c.isprintable() == True and c.isspace() == False:
#             s += c
#     if len(s) < 1 or len(s) > 14:
#         print("Length ", len(s), s)
#     return s
 
# def main():
#     n = 1000
#     ht = my_hash(int(n))
    
#     chars = [chr(i) for i in range(32, 127)] #Printables
#     i = 0
#     while i < n:
#         w = really_ugly_word(chars)
#         if ht.find_key_value(w) == None: # No dupllicates
#             ht.add(w, i)
#             i += 1
    
#     dump_whole_table = False
#     freqs = ht.dump_table_contents(dump_whole_table)
#     entries = 0
#     lst = []
#     for i in freqs:
#         stars = "*" * (80 if i[1] > 80 else i[1])
#         stars = stars + ("..." if i[1] > 80 else "")
#         lst.append(("{:6d} {} ({})".format(i[0], stars, i[1]), i[1]))
#         entries += i[0] * i[1]
        
#     print("++++ {} entries\n".format(entries))
#     print("Collision list length(len) and frequencies of a given length")
#     print("{:>8s} {:>8s} {:^12s} {}".format("%", "cum%", "len", "frequency"))
#     print("-" * 50)
#     i = 1
#     cum = 0
#     for f in lst:
#         percent = i * f[1] / entries
#         cum += percent
#         lst = f[0].split()
#         print("{:8.1%} {:8.1%} {:^12s} {:s}".format(percent, cum, lst[0], lst[1] + lst[2]))
#         i += 1

    
# if __name__ == "__main__":
#     main()