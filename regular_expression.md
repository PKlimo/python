# Regular expression
* [docs](https://docs.python.org/3/howto/regex.html)

## Special characters
* \d  Matches any decimal digit; this is equivalent to the class [0-9]
* \s  Matches any whitespace character
* \w  Matches any alphanumeric character
* \b  Word boundary
* capital letter means negation (\D non-digits, \S non-space, \W non-alphabetical, \B not word boundary)
* \A  Matches only at the start of the string, if multiline is disabled, it is equal to ^
* \Z  Matches only at the end of the string.

## Qualifiers
* .*  Zero or more (greedy version)
* .*? Zero or more (non-greedy version)
* .+  One or more (greedy)
* .+? One or more (non-greedy)
* .?  One or zero (greedy)
* .?? One or zero (non-greedy)
* .{m,n} at least m repetitions, and at most n

## Check if string matches reg exp
* function `p = re.compile(r'reg exp', flags)` creates compiled regular expression
* function `m = p.search('sring')` returns first match object (or None if reg exp. did not match the string)
* function `m = p.finditer('string')` return iterator of all matched object
* function `m.group(0)` returns string that matched regular expression
* function `m.group(1)` return first subgroup in reg exp part in ()
* function `m.span()` return beginning and end of matched string

### Compilator flags
* re.IGNORECASE     case insensitive
* re.LOCALE         Make \w, \W, \b, and \B, dependent on the current locale
* re.MULTILINE      ^ / $ matches at the beginning / end of the string and at the beginning / end of each line
* re.DOTALL         . matches any character at all, including a newline
* re.VERBOSE        whitespace within the RE string is ignored, except when the whitespace is in a character class

### Example
```python
    import re
    m = re.compile(r'\s*(.*?)\s*:\s*(.*?)\s*$').search(" key : value ")
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
```

## Split
* function m.split(string)  split where regexp matches
```python
    import re
    s = 'From: "Name Surname, Phd."<email@address.com>, Next Person<another@email.com>'
    for word in re.compile(r'\W').split(s):
        print(word)
```

## Substitute
* function m.sub(replacement, string)  replacing the leftmost non-overlapping occurrences of the RE in string by the replacement replacement
* replacement can be:
    * string
    * \2 - second grup in regexp
```python
import re
p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First} section{second}')
```
    * function (with one parameter match)
```python
import re
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
```
