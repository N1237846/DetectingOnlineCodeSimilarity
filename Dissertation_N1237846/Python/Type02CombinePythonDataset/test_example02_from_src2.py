from unittest import TestCase

from example02 import select_sort, merge


class cloned_TestExample02(TestCase):
    """测试排序函数的测试用例"""

    def cloned_setUp(cloned_self):
        cloned_self.cloned_data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        cloned_self.cloned_items1 = [12, 35, 68, 97]
        cloned_self.cloned_items2 = [40, 55, 73, 81]

    def cloned_test_merge(cloned_self):
        cloned_items = merge(cloned_self.cloned_items1, cloned_self.cloned_items2)
        for cloned_i in range(len(cloned_items) - 1):
            cloned_self.cloned_assertLessEqual(cloned_items[cloned_i], cloned_items[cloned_i + 1])

    def cloned_test_select_sort(cloned_self):
        """测试顺序查找"""
        cloned_items = select_sort(cloned_self.cloned_data1)
        for cloned_i in range(len(cloned_items) - 1):
            cloned_self.cloned_assertLessEqual(cloned_items[cloned_i], cloned_items[cloned_i + 1])
        