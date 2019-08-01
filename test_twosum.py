import unittest
from test import Solution

class test_module(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(Solution().twoSum([-1,-2,-3,-4], -7), [2,3])

if __name__ == "__main__":    unittest.TextTestRunner(verbosity=3).run(unittest.TestLoader().loadTestsFromTestCase(test_module))
