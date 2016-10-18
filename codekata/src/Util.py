import unittest
import string


def az_sequence():
    # generate infinite sequence of a1 ... z1, a2 ... z2 ...
    chars = string.ascii_lowercase
    num = 0
    while True:
        num += 1
        for char in chars:
            yield char + str(num)


class UtilTest(unittest.TestCase):

    def test_sequence(self):
        seq = az_sequence()
        self.assertEqual('a1', seq.next())
        [seq.next() for i in range(25)]
        self.assertEqual('a2', seq.next())
        [seq.next() for i in range(24)]
        self.assertEqual('z2', seq.next())

if __name__ == '__main__':
    import sys
    unittest.main()