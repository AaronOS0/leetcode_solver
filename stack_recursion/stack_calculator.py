#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import reduce
from math import ceil
import operator
import re

"""
Questions:
150. Evaluate Reverse Polish Notation
227. Basic Calculator II
"""


class Solution:
    """
    150. Evaluate Reverse Polish Notation
    https://leetcode.com/problems/evaluate-reverse-polish-notation/
    >>> tokens = ["2","1","+","3","*"]
    >>> 9
    ((2 + 1) * 3) = 9
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        binary_operator = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y),
        }

        for element in tokens:
            try:
                num = int(element)
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop()
                num = binary_operator[element](num2, num1)
            finally:
                stack.append(num)
        return stack[0]

    """
    227. Basic Calculator II
    https://leetcode.com/problems/basic-calculator-ii/
    >>> s = "3+2*2"
    >>> 7
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def calculate(self, s: str) -> int:
        # split by +-*/, and reserve them
        s = re.split(r'([\+\-\*\/])', s)
        stack = []
        pre_sign = '+'

        for element in s:
            # drop the space
            element = element.strip()
            if element.isdigit():
                num = int(element)
                if pre_sign == "+":
                    stack.append(num)
                elif pre_sign == "-":
                    stack.append(-num)
                elif pre_sign == "*":
                    stack.append(stack.pop() * num)
                elif pre_sign == "/":
                    stack.append(int(stack.pop() / num))
                else:
                    pass
            else:
                pre_sign = element

        return sum(stack)
