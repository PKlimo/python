# Working with files

## Opening files
```python
with open('file.txt', encoding='utf-8', mode="rt") as f:
```

* modes:
  * b (binary), t(text) - with text mode specify encoding
  * r(read), w(write - truncate file if exists), a(append), w+(read and write), x(write - fail if file exists)

## Reading text file

```python
with open('file.txt', encoding='utf-8', mode="rt") as f:
    lines = f.read().splitlines()  # f.read() returns whole content as string, method splitlines() returns list (of lines)

    # few tips:
    # sort_lines = sorted(lines)  # sort lines
    # sort_loc_lines = sorted(lines, key=functools.cmp_to_key(locale.strcoll))  # import locale, import functools
    # uniq_lines = set(lines)  # list of uniq lines (dont preserve order)
    # count_lines = Counter(lines)  # from collections import Counter

    # or if you dont need whole content in one variable
    for line in f:
        print(line, end='')
```

## Reading binary file

```python
with open('file.txt', mode="rb") as f:
    content = f.read()  # byte string - imutable object of integer from interval 0 - 255
    b_content = bytearray(content)  # bytearray - mutable version of byte string
```

## Reading standard input as text files:

```python
import sys
f = sys.stdin
# rest is like working with files
lines = f.read().splitlines()
```
## Writing files

```python
with open('file.txt', encoding='utf-8', mode="wt") as f:
    f.write('line')
```

