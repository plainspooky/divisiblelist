# divisiblelist
# https://github.com/plainspooky/divisiblelist
#
# A customized 'collections.UserList' that adds list splitting using
# "/" (division) and "//" (integer division) operators.
#
# Copyright (C) 2021  Giovanni Nunes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Contains `DivisibleList` class."""
from collections import UserList
from typing import Any, Generator


class DivisibleList(UserList):
    """Uses 'collections.UserList` to implement list splitting using "/"
    and "//" operators by implementing '__truediv__' and '__floordiv__'
    methods. You can split a list in sublists using "/" and "//" operators:

    >>> DivisibleList([1, 2, 3, 4, 5]) / 2
    [1, 2, 3], [4, 5]

    >>> DivisibleList([1, 2, 3, 4, 5, 6]) // 3
    [1, 2], [3, 4], [5, 6]

    Integer division only splits lists if divisor is multiple of list's
    length:

    >>> DivisibleList([1, 2, 3, 4, 5, 6]) // 5
    can't divide 6 items by 5

    You can also divide a 'list' in sublists of same number of length putting
    divisor between braces (as a 'set'):

    >>> DivisibleList([1, 2, 3, 4, 5, 6, 7]) / {2}
    [1, 2], [3, 4], [5, 6], [7,]
    """

    __divide_by_chunks = False

    def __init__(self, data=None, *args, **kwargs) -> None:

        super().__init__(data, *args, **kwargs)

    @property
    def dividend(self) -> int:
        return len(self.data)

    def __validate_divisor(self, value: Any) -> int:

        if isinstance(value, set) and len(value) == 1:
            self.__divide_by_chunks = True
            (value,) = value
        else:
            self.__divide_by_chunks = False

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(
                "unsupported operand type(s) for /: '{}' and '{}'".format(
                    self.__class__.__name__, value.__class__.__name__
                )
            )

        elif value < 0:
            raise ValueError("cant't divide a list by a negative number")

        elif value == 0:
            raise ZeroDivisionError

        return value

    def __do_division(self, divisor: int) -> Generator:

        elements = self.dividend // divisor

        total_of_elements = step = (
            divisor if self.__divide_by_chunks else elements
        )

        return (
            self.data[part : part + total_of_elements]  # noqa E203
            for part in range(0, self.dividend, step)
        )

    def __truediv__(self, value: int) -> Generator:

        divisor = self.__validate_divisor(value)

        return self.__do_division(divisor)

    def __floordiv__(self, value: int) -> Generator:

        divisor = self.__validate_divisor(value)

        if self.dividend % divisor:
            raise ValueError(
                f"can't divide {self.dividend} items by {divisor}"
            )

        return self.__do_division(divisor)
