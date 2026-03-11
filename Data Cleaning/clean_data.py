import yfinance as yf

aapl = yf.Ticker('AAPL') # Ticker for stock
df = aapl.history(period = '10y') # Dataset from 2016-03-11 to 2026-03-10

missing = df.isnull().sum() #checking for total null values
print(missing)

nan = df.isna().sum() #checking for total nan values
print(nan)

Q1 = df.quantile(0.25) # 25th percentile
Q3 = df.quantile(0.75) # 75th percentile
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR # Checking to see outlier
upper_bound = Q3 + 1.5 * IQR # Checking to see outlier

outliers = df[(df < lower_bound) | (df > upper_bound)]
print(outliers)

csvFile1 = '../Data/AAPL_Close_Price.csv'
df['Close'].to_csv(csvFile1, index = True)

csvFile2 = '../Data/AAPL_Stock_Info.csv'
df.to_csv(csvFile2, index = True)
