# sloc
A tiny Python script that finds the total lines of code in a directory tree.

## Usage
```
python sloc.py cpp h
```
will find all files ending with `.cpp` and `.h` in the **current directory tree**, count how many lines they each have, and tell you the total.

```
python sloc.py -d /some/arbitrary/path py rb
```
will find all files ending with `.py` and `.rb` in the **/some/arbitrary/path directory tree**, count how many lines they each have, and tell you the total.
