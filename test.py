from unittest import TestCase

import Solution

class TestSolution(TestCase):
    def test_calculatelbtt(self):
         self.assertEqual(Solution.calculatelbtt(125000), 0)
         self.assertEqual(Solution.calculatelbtt(150000), 500)
         self.assertEqual(Solution.calculatelbtt(500000), 15000)
         self.assertEqual(Solution.calculatelbtt(1000000), 43750)
         self.assertEqual(Solution.calculatelbtt(1600000), 105750)


    def test_calculatelbttRaiseException(self):
         self.assertRaises(Exception, Solution.calculatelbtt, -5000)

    def test_calculatelbttraiseTypeError(self):
         self.assertRaises(TypeError, Solution.calculatelbtt, "500")