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
  >>> my_list / 3
  ValueError: can't divide 4 items by 3
  ```

- To doesn't waste resources, all sub-lists are created as `Generators`.

  ``` console
  >>> my_list / 2
  <generator object DivisibleList.__truediv__.<locals>.<genexpr> at 0x7fc0676e
  09e0>
  >>> first_half, second_half = my_list / 2
  >>> print(first_half, second_half, sep="\\n")
  [0, 1]
  [2, 3]
  ```
"""
from collections import UserList
from typing import Generator


class DivisibleList(UserList):
    """Customizes `collections.UserList` to add list split support by using
    the `/` operator by implementing the [__truediv__](
    https://docs.python.org/3.9/reference/datamodel.html#object.__truediv__)
    method.
    """

    def __truediv__(self, divisor: int) -> Generator:

        if not isinstance(divisor, int) or isinstance(divisor, bool):
            raise TypeError(
                "unsupported operand type(s) for /: '{}' and '{}'".format(
                    self.__class__.__name__, divisor.__class__.__name__
                )
            )

        elif divisor < 0:
            raise ValueError("cant't divide a list by a negative number")

        elif divisor == 0:
            raise ZeroDivisionError

        dividend = len(self.data)

        if dividend % divisor:
            raise ValueError(f"can't divide {dividend} items by {divisor}")

        elements = dividend // divisor

        return (
            self.data[part : part + elements]  # noqa: E203
            for part in range(0, dividend, elements)
        )
