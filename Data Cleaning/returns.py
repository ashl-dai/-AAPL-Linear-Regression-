import pandas as pd

def simpleReturns(CSVfile, columnName, outputFile, newName):
    df = pd.read_csv(CSVfile)
    df[newName] = df[columnName].pct_change() * 100
    df.to_csv(outputFile)

def AvgMonthlyReturns(CSVfile, columnName, outputFile, newName):
    df = pd.read_csv(CSVfile)
    df[newName] = df[columnName].pct_change() * 100
    df.to_csv(outputFile)