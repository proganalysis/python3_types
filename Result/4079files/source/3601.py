import unittest
from main import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(
            self.sol.longestCommonPrefix(["flower","flow","flight"]),
            "fl"
        )

    def test_2(self):
        self.assertEqual(
            self.sol.longestCommonPrefix(["dog","racecar","car"]),
            ""
        )
