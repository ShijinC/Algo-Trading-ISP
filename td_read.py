import tda
import json
from td_get import *
import pandas
import numpy

with open('data.json') as outfile:
    data = json.load(outfile)

aapl = option_chain(data)



print("\n\n\n\n\n")

print(aapl.calls[0])
print("\n")
print(aapl.calls[0].type)
print("\n")
print(aapl.calls[0].last)
print("\n")
print(aapl.calls[0].bid)
print("\n")