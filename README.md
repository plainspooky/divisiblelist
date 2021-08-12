divisiblelist
---

A customized **list** type (based on [collections.UserList](
https://docs.python.org/3/library/collections.html#collections.UserDict)
that can be easilly splited in sublist using  `/` (division) and `//`
(integer division) operators.

``` python
import divisiblelist as dl

my_list = dl.DivisibleList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for sublist in my_list / 2:
    print(sublist)
```

That results in `[0, 1, 2, 3, 4]` and `[5, 6, 7, 8, 9]`.

If divisor and dividend (as list lenght) aren't multiples the last sublist
will contains fewer elements.

``` python
for sublist in my_list / 3:
    print(sublist)
```

Will results  `[0, 1, 2]`, `[3, 4, 5]`, `[6, 7, 8]`, and `[9]`

# Instalation

Use:

``` console
pip install git+https://github.com/plainspooky/divisiblelist
```

To install the lastest version of this module.

# Usage

To create a **divisiblelist** object:

``` console
>>> import divisiblelist as dl
>>> my_list = dl.DivisibleList([0, 1, 2, 3])
>>> my_list
[0, 1, 2, 3]
```

It works like as an ordinary **list** so you can use `.append()`, `.count()`,
`.index()`, `.pop()` or any other built-in method from **list** type.

But there are some concerns about list division:

1. A list can be divided only by integer values, tries to use another
  type as divisor raises `TypeError` exception:

  ``` console
  >>> my_list / "2"
  TypeError: unsupported operand type(s) for /: 'DivisibleList' and 'str'
  ```

2. Divisor must be greater than zero:

  ``` console
  >>> my_list / -2
  ValueError: cant't divide a list by a negative number
  ```

3. A **list** can't be divided by zero:

  ``` console
  >>> my_list / 0
  ZeroDivisionError
  ```

# Features

## Integer division

If you want to force the same number of elements in a sublist, use `//`
instead of `/` to force an integer division.

``` console
>>> my_list // 3
ValueError: can't divide 4 items by 3
```

It raises a **ValueError** exception in case of the divisor isn't a
multiple of the dividend.

## Division by chunks

To produce sublists with specific number of elements put divisor between
braces.

``` console
>>> [sublist for sublist in my_list / {1}]
[[0],[1],[2],[3]]
```

It follows same rule for integer division when using `//`.

## Generator function

To avoid waste resources, all sub-lists are created as a [generator
function](https://wiki.python.org/moin/Generators) and will work
only by demand.

``` console
>>> my_list / 2
<generator object DivisibleList.__truediv__.<locals>.<genexpr> at 0x7fc0676e09
e0>
>>> first_half, second_half = my_list / 2
>>> print(first_half, second_half, sep="\n")
[0, 1]
[2, 3]
```
