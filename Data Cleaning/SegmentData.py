import pandas as pd
import numpy as np

def yearBreakup(CSVfile, outputFile):
    df = pd.read_csv(CSVfile)
    df['Year-Month'] = df['Date'].str.split(" ").str[0].str[0:7] # New Column of Year and Month
    df = df.drop(columns='Date')
    df.to_csv(outputFile, index = False)


def monthlyAvg(CSVfile, column, outputMean, columnName):
    df = pd.read_csv(CSVfile)
    grouped_mean = df.groupby('Year-Month')[column].mean()
    average = pd.DataFrame(grouped_mean)
    average = average.rename(columns={column: columnName})
    average.to_csv(outputMean)