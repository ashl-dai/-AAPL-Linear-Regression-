import plotly.express as px
import pandas as pd

def scatterPlot(CSVFile, plotName, yName, xName):
    df = pd.read_csv(CSVFile)
    fig = px.scatter(df, title = plotName, y = yName, x = xName)
    fig.show()
