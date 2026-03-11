from math import dist
import numpy as np
import pandas as pd
from plotly import data
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def lnFit(CSVfile, columnName, outputFile):
    df = pd.read_csv(CSVfile)
    df['Log-Data'] = np.log(df[columnName])
    df = df.drop(columns = "Unnamed: 0")
    df.to_csv(outputFile)
    return df
    
def modelQuality(CSVfile, columnName): # Only tests exponential, gamma, log norm, weibull, and invgauss
    df = pd.read_csv(CSVfile)
    data = df[columnName]
    n = len(data)
    results=[]

    distributions = ['norm', 't', 'laplace', 'johnsonsu', 'genhyperbolic', 'hypsecant']
    for dist in distributions:
        try:
            distr = getattr(stats, dist)
            params = distr.fit(data, floc=0)  # Fit the distribution to the data and floc=0 to force location parameter to be zero
            log_likelihood = np.sum(distr.logpdf(data, *params))  # Calculate log-likelihood, *param takes list/tuple and unpack its contents into individual arguments for the function
            k = len(params)

            aic = 2*k - 2*log_likelihood
            bic = k*np.log(n) - 2*log_likelihood

            results.append({"Distribution": dist, 
                            "AIC": aic, 
                            "BIC": bic,
                            "Params": params})
            
        except Exception as e:
            print(f"Error fitting {dist}: {e}")

    results_df = pd.DataFrame(results).sort_values(by="AIC")
    return results_df

# def lrTotalClose(CSVfile, outputFile):
