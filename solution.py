import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import mannwhitneyu

chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(x,y) -> bool:
    alpha = 0.05
    pvalue = stats.ttest_ind(x,y)[1]
    return pvalue < alpha
