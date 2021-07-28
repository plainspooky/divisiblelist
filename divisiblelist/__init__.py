# divisiblelist
# https://github.com/plainspooky/divisiblelist
#
# A customized 'collections.UserList' that adds list spliting using
# the "/" (division) operator.
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
"""
A customized 'collections.UserList' that adds list spliting using
the "/" (division) operator.

``` python
import divisiblelist as dl

my_list = dl.DivisibleList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for sublist in my_list / 2:
    print(sublist)

# output:
# [0, 1, 2, 3, 4]
# [5, 6, 7, 8, 9]
```

## Instalation

To install the lastest version of this module, use:

``` console
pip install git+https://github.com/plainspooky/divisiblelist
```

## Usage

To create a new "list":

``` console
>>> import divisiblelist as dl
>>> my_list = dl.DivisibleList([0, 1, 2, 3])
>>> my_list
[0, 1, 2, 3]
```

Some notes:

- This lists can only be divided by an integer value, tries to use another
  type as divisor raises `TypeError` exception:

  ``` console
  >>> my_list / "2"
  TypeError: unsupported operand type(s) for /: 'DivisibleList' and 'str'
  ```

- Divisor must be greater than zero:

  ``` console
  >>> my_list / -2
  ValueError: cant't divide a list by a negative number
  ```

- You can't divide a list by zero:

  ``` console
  >>> my_list / 0
  ZeroDivisionError
  ```

- And, off course, it's a integer division, so there is no rest:

  ``` console
  >>> my_list // 3
  ValueError: can't divide 4 items by 3
  ```

You can invert the division to set the number of elemets...

- To avoit to dwaste resources, all sub-lists are created as `Generators`.

``` console
>>> my_list / 2
<generator object DivisibleList.__truediv__.<locals>.<genexpr> at 0x7fc0676e09
e0>
>>> first_half, second_half = my_list / 2
>>> print(first_half, second_half, sep="\\n")
[0, 1]
[2, 3]
```
"""
from collections import UserList
from typing import Any, Generator


class DivisibleList(UserList):
    """Customizes `collections.UserList` to add list split support by using
    the `/` operator by implementing the [__truediv__](
    https://docs.python.org/3.9/reference/datamodel.html#object.__truediv__)
    method.
    """

    divide_by_chunks = False

    def __init__(self, data=None, *args, **kwargs) -> None:

        super().__init__(data, *args, **kwargs)

    @property
    def dividend(self) -> int:
        return len(self.data)

    def __validate_divisor(self, value: Any) -> int:

        if isinstance(value, set) and len(value) == 1:
            self.divide_by_chunks = True
            (value,) = value
        else:
            self.divide_by_chunks = False

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
            divisor if self.divide_by_chunks else elements
        )

        return (
            self.data[part : part + total_of_elements]  # noqa E203
            for part in range(0, self.dividend, step)
        )

    def __truediv__(self, value: int) -> Generator:

        divisor = self.__validate_divisor(value)

        if self.dividend % divisor:
            raise ValueError(
                f"can't divide {self.dividend} items by {divisor}"
            )

        return self.__do_division(divisor)
