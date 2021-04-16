import tda
import json
from td_get import *
import pandas
import numpy
import matplotlib.pyplot as plt

with open('data.json') as outfile:
    data = json.load(outfile)

aapl = option_chain(data)



print("\n\n\n\n\n")

x_strike = [i.strike for i in aapl.calls]
x_extrinsic = [i.extrinsic for i in aapl.calls]
x_intrinsic = [i.intrinsic for i in aapl.calls]
y_last = [i.last for i in aapl.calls]


gridspec = {
    'hspace':0.27,
    'wspace':0.27,
    'left':0.04,
    'right':0.96,
    'top':0.95,
    'bottom':0.05
}

fig, axs = plt.subplots(
    2,2,
    dpi=200,
    figsize=(6,6),
    gridspec_kw=gridspec
)

numberCalls = len(aapl.calls)

axs[0][0].plot(x_strike,y_last,color="C1")
axs[0][0].scatter(x_strike,y_last,color="C1")
axs[0][0].grid()
axs[0][0].set_title("Options: Price vs Strike")

axs[0][1].plot(x_strike,x_extrinsic,color="C0")
axs[0][1].scatter(x_strike,x_extrinsic,color="C0")
axs[0][1].grid()
axs[0][1].set_title("Options: Extrinsic Value vs Strike")

axs[1][0].plot(x_strike,x_intrinsic,color="C2")
axs[1][0].scatter(x_strike,x_intrinsic,color="C2")
axs[1][0].grid()
axs[1][0].set_title("Options: Intrinsic Value vs Strike")

#plt.savefig('test.png',dpi=1000)

plt.show()
