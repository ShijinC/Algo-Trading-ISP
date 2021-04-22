from td_read import *
from td_get import *
from theory import *

rfr = 0.28
div = 0.0

aapl = load_option_chain("aapl")

option1 = aapl.calls[1]
options = aapl.calls
data = define_graphing_metrics(options)
make_graphs(data)
