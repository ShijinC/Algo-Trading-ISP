from sas7bdat import SAS7BDAT
import pandas

import pandas as pd
df = pd.read_sas("C:/Users/10111/OneDrive/Desktop/opprcd2017.sas7bdat", chunksize = 100000)
dfs = []
i = 0
for chunk in df:
    i  += 1
    print(i)
    dfs.append(chunk)
    chunk.to_csv("C:/Users/10111/Documents/GitHub/Algo-Trading-ISP/data/option2017-"+str(i)+".csv")
df_final = pd.concat(dfs)

df.head()