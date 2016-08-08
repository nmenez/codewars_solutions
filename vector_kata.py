import unittest

from math import sqrt
class Vector:
    def __init__(self,elements):
        self.elements = elements

    def __str__(self):
        return str(self.elements).replace('[','(').replace(']',')').replace(' ','')
                
    def __checklength__(self, b):
        if len(b.elements) != len(self.elements):
            raise ValueError('vectors are no equal')
            
    def add(self, b):
        self.__checklength__(b)
        return Vector([ei + bi for ei, bi in zip(self.elements, b.elements)])
                
    def subtract(self, b):
        return self.add(Vector([-1*bi for bi in b.elements]))
                
    def dot(self, b):    
        self.__checklength__(b)
        return sum([ai*bi for ai, bi in zip(self.elements, b.elements)])
            
    def norm(self):
        return sqrt(sum(ai**2 for ai in self.elements))
            

    def equals(self,b):
        self.__checklength__(b)
        for ai, bi in zip(self.elements, b.elements):
            if ai != bi:
                return False
        return True
        
        
class TestVector(unittest.TestCase):
    def test_add(self):
        a = Vector([1,2,3])
        b = Vector([3,4,5])
        c = a.add(b)
        self.assertEqual(c.elements, [4,6,8])
          
    def test_add_exception(self):
        a = Vector([1,2,3])
        b = Vector([3,4,5,6])
        self.assertRaises(ValueError, a.add, b)

    def test_subtract(self):
        a = Vector([1,2,3])
        b = Vector([3,4,5])
        c = a.subtract(b)
        self.assertEqual(c.elements, [-2, -2, -2])

    def test_dot(self):
        a = Vector([1,2,3])
        b = Vector([3,4,5])
        self.assertEqual(a.dot(b), 3+8+15)

    def test_norm(self):
        a = Vector([1,2,3])
        self.assertEqual(a.norm(), sqrt(1+4+9))

    def test_equal(self):
        a = Vector([1,2,3])
        b = Vector([3,4,5])
        c = Vector([1,2,3])
        self.assertFalse(a.equals(b))
        self.assertTrue(a.equals(c))


    def test_str(self):
        a= Vector([1,2,3])
        stra = str(a)
        self.assertEqual(stra, '(1,2,3)')



if __name__ == "__main__":
    unittest.main()