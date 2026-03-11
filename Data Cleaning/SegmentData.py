import pandas as pd
import numpy as np

def yearBreakup(CSVfile, outputFile):
    df = pd.read_csv(CSVfile)
    df['Year-Month'] = df['Date'].str.split(" ").str[0].str[0:7] # New Column of Year and Month
    df.to_csv(outputFile)


def monthlyAvg(CSVfile, outputMean):
    df = pd.read_csv(CSVfile)
    grouped_mean = df.groupby('Year-Month')['Close'].mean()
    average = pd.DataFrame(grouped_mean)
    average.to_csv(outputMean)