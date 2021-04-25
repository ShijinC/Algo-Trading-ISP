import csv

sp500 = {}
with open('s&p 500.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sp500[row["Symbol"]] = []
        sp500[row["Symbol"]].append(row['Name'])
        sp500[row["Symbol"]].append(row['Sector'])
print(sp500)