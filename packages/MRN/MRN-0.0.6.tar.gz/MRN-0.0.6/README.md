# Memory Retention Normalization - MRN

This Library is used for normalizing data array with respect to long term memory retention

Timeseries Data's have influence of long term memory retention on their current data

This phenomenon happens in the field of finance sports and other live streaming timeseries datas

Developed by Philip Pankaj (c) 2021

##Example with Nasdaq 100 data

<p align="center">
  <img src="MRN_Nasdaq_Graph.png">
</p>

```python
#importing our MRN
from MRN import Normalization

#importing all required library
from yahoo_fin.stock_info import get_data
from datetime import date

#getting nifty data and converyting to numpy array
now=date.today().strftime("%d/%m/%Y")  
from_date="5/5/2006" # m/d/year
data= get_data("^IXIC", start_date=from_date, end_date=now, index_as_date = True, interval="1d")
data=data['close'].dropna()
data=data.to_numpy()

#initializing MRN and transforming data
mrn=Normalization(data,0.5)
n_data=mrn.transform()

#importing matplotlib and plotting
import matplotlib.pyplot as plt
plt.figure(figsize=(40, 40))

fig, ax1 = plt.subplots()
ax1.set_ylabel('Nasdaq-100')
ax1.plot(data[-1000:], color = 'tab:blue')

ax2=ax1.twinx()
ax2.set_ylabel('MRN-Normalized')
ax2.plot(n_data[-1000:],color='tab:green')
plt.show()

```
