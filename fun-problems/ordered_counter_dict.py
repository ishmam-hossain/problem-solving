from collections import OrderedDict, Counter


class MyDict(Counter, OrderedDict):
    """This is a Counter dict that remembers the order data was inserted"""


md = MyDict()
md[1] = 3
md[3] = 3
md[4] = 3
md[3] = 3
print(md)
