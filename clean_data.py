import yfinance as yf
import plotly.express as px

aapl = yf.Ticker('AAPL')
df = aapl.history(period = '10y')

missing = df.isnull().sum()
print(missing)

nan = df.isna().sum()
print(nan)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df < lower_bound) | (df > upper_bound)]
print(outliers)

fig = px.scatter(df, y = "Close", title = 'Closing Price of AAPL Over the Past 10 Years')
fig.show()

csvFile1 = 'AAPL_Close_Price.csv'
df['Close'].to_csv(csvFile1, index = False)

csvFile2 = 'AAPL_Stock_Info.csv'
df.to_csv(csvFile2, index = False)