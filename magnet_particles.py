def doubles(maxk, maxn):
    return sum([sum([1. / (k * (1 + n)**(2 * k)) for n in range(1, maxn + 1)]) for k in range(1, maxk + 1)])

import unittest


class testMagnet(unittest.TestCase):
    def test1(self):
        self.assertEqual(doubles(1, 3), 0.4236111111111111)
        self.assertEqual(doubles(1, 10), 0.5580321939764581)
        self.assertEqual(doubles(10, 100), 0.6832948559787737)
        self.assertA
#if __name__ == "__main__":
#    unittest.main()



def testsum(q,N):
    return sum((q**n)/n for n in range(1,N+1))

n=999
for i in range(1000):
    print(i, testsum(1./(1+n)**2, i))