import unittest
from data_structures.stack import Stack


class StackTestCase(unittest.TestCase):
    structure: Stack = Stack[int](10)

    def test_initialize(self):
        self.structure.push(67)
        self.structure.push(56)
        self.structure.push(12)
        self.structure.push(2)
        self.structure.push(99)
        self.assertEqual(len(self.structure), 5)

    def test_generic_type(self):
        self.assertEqual(self.structure.__generic_type__, int)


if __name__ == '__main__':
    unittest.main()
