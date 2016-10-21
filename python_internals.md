# Python internals
## Urls:
* [jakevdp basic object overview](https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)
## Basic functions:
* return address of object in memory (in cpython implemantation) - function id(object)

```python
ptr = id(13)     # address of object / integer 13 (integer is object)
print(hex(ptr))  # print in hexadecimal format
```
* read address from memory - methond ctypes._CData().from_address(address) - return array of pointers  pointing into adress

```python
from ctypes import c_int
ptr = (c_int * 4).from_address(id(13))  # ptr is array of 4 poiters (of lenght int) poiting to address of object int 13

print("long ob_refcnt:", ptr[0])
print("PyTypeObject *ob_type", hex(ptr[1]))
print("size_t ob_size", ptr[2])
print("long ob_digit[1]", ptr[3])
```

* byte code and constants of function (e.g. function main()): main.__code__.co_consts and main.__code__.co_code

## Examples:
* Rewriting object in memory - e.g. value (ob_digit) of int object
```python
#!/usr/bin/env python3

def fun(i):
    from ctypes import c_int
    ptr = (c_int * 4).from_address(id(42))

    print("Dumping from memory {} 4 longs (4 bytes)".format(hex(id(i))))
    print("long ob_refcnt:", ptr[0])
    print("PyTypeObject *ob_type", hex(ptr[1]))
    print("size_t ob_size", ptr[2])
    print("long ob_digit[1]", ptr[3])
    ptr[3] = 1337


def main():
    i = 42
    fun(i)
    print("Value of i:", i)
    if 42 == 1337:
        print('strange')

if __name__ == "__main__":
    main()
```

* Rewriting constants and byte-code of function
```python
import ctypes
import sys
import dis


def fun():
    # change constant from 20 to 13
    m_con = main.__code__.co_consts
    ptr = (ctypes.c_int * sys.getsizeof(m_con)).from_address(id(m_con))
    ptr[4] = id(13)
    # change 19 from LOAD_FAST to LOAD_CONST
    m_bc = main.__code__.co_code
    off = sys.getsizeof("") // 2
    src = (ctypes.c_byte * len(m_bc)).from_address(id(m_bc) + off)
    src[19] = src[0]
    src[20] = src[1]


def main():
    a = 20
    fun()
    print("Value of a:", a)
    print("Value of a:", a)

if __name__ == "__main__":
    dis.dis(main)
    main()
    dis.dis(main)
```

* change LOAD_CONST value before instruction RETURN_VALUE to change return value of function
```python
from ctypes import c_byte
from sys import getsizeof
import dis


def fun():
    temp = 1337
    c = fun.__code__.co_code
    off = getsizeof("") - 1
    ptr = (c_byte * len(c)).from_address(id(c) + off)
    ptr[-18]=1
    return 42


dis.dis(fun)
print(fun())
dis.dis(fun)
```
