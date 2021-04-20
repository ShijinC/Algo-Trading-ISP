import tda
import json
from td_get import *
from theory import *
import pandas
import numpy
import matplotlib.pyplot as plt

def load_option_chain(name):
    with open("./data/"+name+'.json') as outfile:
        data = json.load(outfile)
        data = option_chain(data)
        print("Option Chain Loaded")
        return data
    

def define_graphing_metrics(options):
    graphing_data = {}
    graphing_data["strike"] = [i.strike for i in options]
    graphing_data["extrinsic"] = [i.extrinsic for i in options]
    graphing_data["intrinsic"] = [i.intrinsic for i in options]
    graphing_data["last"] = [i.last for i in options]
    graphing_data["totalvolume"] = sum([i.totalvol for i in options])
    graphing_data["relative_volume"] = [i.totalvol / totalvolume for i in options]
    graphing_data["totalopeninterest"] = sum([i.openinterst for i in options])
    graphing_data["relative_interest"] = [i.openinterst / totalopeninterest for i in aapl.calls]
    graphing_data["interest"] = [i.openinterst for i in options]
    graphing_data["spread"] = [i.ask - i.bid for i in options]
    graphing_data["spread_ratio"] = [(i.ask - i.bid) / i.last for i in options]
    graphing_data["size_spread"] = [i.asksize - i.bidsize for i in options]
    graphing_data["underlying_price"] = options[0].stockprice
    graphing_data["IV"] = [i.TV for i in options]
    
    return graphing_data

def make_graphs(data):
    gridspec = {
        'hspace':0.27,
        'wspace':0.27,
        'left':0.08,
        'right':0.96,
        'top':0.95,
        'bottom':0.05
    }

    fig, axs = plt.subplots(
        2,2,
        dpi=150,
        figsize=(6,6),
        gridspec_kw=gridspec
    )

    """ axs[0][0].plot(x_strike,y_last,color="C1")
    axs[0][0].scatter(x_strike,y_last,color="C1")
    axs[0][0].grid()
    axs[0][0].set_title("Price vs Strike") """

    axs[0][0].plot(x_strike,x_relative_interest,color="C1")
    axs[0][0].plot(x_strike,x_interest,color="C1")
    axs[0][0].scatter(x_strike,x_relative_interest,color="C1",marker='.')
    axs[0][0].grid()
    axs[0][0].set_title("(Relative) Interst vs Strike")
    axs[0][0].axvline(underlying_price)

    """ axs[0][1].plot(x_strike,x_extrinsic,color="C0")
    axs[0][1].scatter(x_strike,x_extrinsic,color="C0")
    axs[0][1].grid()
    axs[0][1].set_title("Extrinsic Value vs Strike") """

    axs[0][1].plot(x_strike,x_size_spread,color="C0")
    axs[0][1].scatter(x_strike,x_size_spread,color="C0",marker='.')
    axs[0][1].grid()
    axs[0][1].axvline(underlying_price)
    axs[0][1].set_title("Size Spread vs Strike")

    """ axs[1][0].plot(x_strike,x_intrinsic,color="C2")
    axs[1][0].scatter(x_strike,x_intrinsic,color="C2")
    axs[1][0].grid()
    axs[1][0].set_title("Intrinsic Value vs Strike") """

    axs[1][0].bar(x_strike,x_spread_ratio,color="C4")
    axs[1][0].plot(x_strike,x_spread,color="C2")
    axs[1][0].scatter(x_strike,x_spread,color="C3",marker='.')
    axs[1][0].grid()
    axs[1][0].set_title("Spread Ratio vs Strike")
    axs[1][0].axvline(underlying_price)

    axs[1][1].plot(x_strike,x_relative_volume,color="C3")
    axs[1][1].scatter(x_strike,x_relative_volume,color="C3",marker='.')
    axs[1][1].grid()
    axs[1][1].set_title("Relative Volume vs Strike")
    axs[1][1].axvline(underlying_price)

    plt.show()
