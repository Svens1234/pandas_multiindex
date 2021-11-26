import numpy as np
import pandas as pd
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]

tuples = list(zip(*arrays))
print(tuples)

index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
print(index)


s = pd.Series(np.random.randn(8), index=index)

print(s)

iterables = [["bar", "baz", "foo", "qux"], ["one", "two"]]

print(pd.MultiIndex.from_product(iterables, names=["first", "second"]))

