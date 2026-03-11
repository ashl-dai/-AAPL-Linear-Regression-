import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

def scatterPlot(CSVFile, plotName, yName, xName):
    df = pd.read_csv(CSVFile)
    fig = px.scatter(df, title = plotName, y = yName, x = xName)
    fig.show()

def lnPlot(CSVfile, columnName):
    df = pd.read_csv(CSVfile)
    fig = sm.qqplot(df[columnName], line='s') # s for standardized line
    plt.title('QQ Plot of Log-Transformed Data')
    plt.show()

import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

def plotLineFit(CSVFile, columnName):
    df = pd.read_csv(CSVFile)
    data = df[columnName]
    data = data[np.isfinite(data)]
    
    xRange = np.linspace(data.min(), data.max(), 500)

    pdfVal = ['norm', 't', 'laplace', 'johnsonsu', 'genhyperbolic', 'hypsecant']
    fig = px.histogram(
        data,
        nbins=100,
        histnorm='probability density',
        title=f'Distribution of Daily Returns: {columnName}',
        labels={'value': 'Daily Return (%)'},
        opacity=0.6
    )
    
    for dist in pdfVal:
        try:
            distr = getattr(stats, dist)
            params = distr.fit(data)  
            yVal = distr.pdf(xRange, *params)

            fig.add_scatter(x=xRange, y=yVal, mode='lines', name=f'{dist} PDF')
        except Exception as e:
            print(f"Error with {dist}: {e}")
    
    fig.show()