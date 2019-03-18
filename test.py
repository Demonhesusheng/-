import unittest
from practice import operate


class CalcTestCase(unittest.TestCase):
    """
    测试practice.py
    """

    def test_operate(self):
        """是否能够正确处理表达式"""
        result = operate(12, 14, '+')
        self.assertEqual(result, 26)


unittest.main()