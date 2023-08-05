requires python 3.6 or above.\
tested in 3.8, 3.9 and 3.10

```
pip install -U incr
```

usage:

```py
from incr import incr

@incr
def x():
    i = 0
    print(++i)  # 1
    print(i)    # 1

    ++i
    print(i)    # 2
```

post-increment (`i++`) is not supported because it's not a valid python syntax
