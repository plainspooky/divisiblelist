divisiblelist
---

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
  >>> print(first_half, second_half, sep="\n")
  [0, 1]
  [2, 3]
  ```
