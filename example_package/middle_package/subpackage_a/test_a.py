# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2021 Michiel Verboven
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Test module test_a"""


class TestA(object):
    """TestA class.

    Args:
            x (str) : test parameter x
            y (bool) : test parameter y
            z (int) : test parameter z

    """

    def __init__(self, x: str, y: bool, z: int):
        self._x = x
        self._y = y
        self._z = z

    def test_method_a1(self) -> None:
        """test_method_a1

        Returns:
            None
        """
        pass

    def test_method_a2(self, a: int = 0, test: bool = False) -> str:
        """test_method_a2

        Args:
            a (int) : test parameter a
            test (bool) : test parameter test

        Returns:
            str : test return parameter
        """
        res = str(a)
        if test:
            res = "x"
        return res
