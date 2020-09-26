import unittest
import hash

class HashTest(unittest.TestCase):

    def setUp(self):
        self.keys1 = ["1key1", "1key2", "1key3", 1, -1]
        self.keys2 = ["2key1", "2key2", "2key3", 6, -8]
        self.ht = hash.my_hash()
        self.load_ht(self.keys1)
        self.load_ht(self.keys2)
        
    def load_ht(self, keys):
        for k in keys:
            self.ht.add(k, k + k)
            
    def get_value(self, key):
        return self.ht.find_key_value(key)
    
    def get_count(self):
        return self.ht.get_ht_count()
    
    def test_hash_count(self):
        cnt = self.ht.get_ht_count()
        self.assertEqual(cnt, len(self.keys1) + len(self.keys2))
        self.ht.add("foobar", 234)
        self.assertIsNone(self.ht.add("foobar", 123))
        self.assertEqual(cnt + 1, self.ht.get_ht_count())
        self.ht.delete_key("foobar")
        self.assertEqual(cnt, self.ht.get_ht_count())
        for k in self.keys1:
            self.ht.add(k + k, "")
        for k in self.keys2:
            self.ht.add(k + k, "")
        self.assertEqual(cnt * 2, self.ht.get_ht_count())
        

    def test_hash_get_values(self):
        self.assertEqual(self.get_value(self.keys1[2]), self.keys1[2] + self.keys1[2])
        for k in self.keys2:
            self.assertEqual(self.get_value(k), k + k)
        self.assertIsNone(self.ht.find_key_value("foobar"))
            
    def test_change_value(self):
        for k in self.keys1:
            self.ht.change_value(k, k + k + k)
        for k in self.keys1:
            self.assertEqual(self.get_value(k), k + k + k)
        self.ht.add("foo", 124)
        self.ht.increment_value("foo")
        self.assertEqual(self.get_value("foo"), 125)
        self.ht.increment_value("foo", 55)
        self.assertEqual(self.get_value("foo"), 180)
        self.ht.increment_value("foo", -100)
        self.assertEqual(self.get_value("foo"), 80)
        self.ht.change_value("foo", "bar")
        # Only int values can be incremented
        self.assertRaises(ValueError, self.ht.increment_value, "foo", 1)
        # Non existant keys return none
        self.assertIsNone(self.ht.increment_value("fubar key"))
        self.assertIsNone(self.ht.change_value("fubar key", "foo"))

    
    def test_delete_value(self):
        ht_key_cnt = len(self.keys1) + len(self.keys2)
        self.assertEqual(self.get_count(), ht_key_cnt)
        i = ht_key_cnt
        for k in self.keys1 + self.keys2:
            self.ht.delete_key(k)
            i -= 1
            self.assertEqual(self.get_count(), i)
        for k in self.keys1 + self.keys2:
            self.ht.delete_key(k)
            self.assertIsNone(self.ht.delete_key(k))
        self.ht.add("A key", 123)
        self.assertEqual(self.get_count(), 1)
        self.ht.delete_key("A key")
        self.assertEqual(self.get_count(), 0)
        
            
if __name__ == "__main__":
    unittest.main()