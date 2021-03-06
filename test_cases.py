#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        # 1から999
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        # 0以下
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))
                
        # 1000以上
        def test_sample3 (self):
                self.assertEqual (-1, calc(1010,5))

        # 小数
        def test_sample4 (self):
                self.assertEqual (-1, calc(22.2,300))

        # 数字以外かどうかの判定
        def test_sample5 (self):
                self.assertEqual (-1, calc('a','gg'))
        
        # 片方が文字列片方が数字
        def test_sample6 (self):
                self.assertEqual (-1, calc('+', 5))
