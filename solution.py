import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest

chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: 
    alpha = 0.05
    pvalue = ztest(x, value=500, alternative='smaller')[1]
    return pvalue < alpha 
