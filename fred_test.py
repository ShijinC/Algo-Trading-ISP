from fredapi import Fred

fred = Fred(api_key="3493a13577022550f820851351c97211")

data = fred.get_series_latest_release('WM1NS')
print(data.tail())