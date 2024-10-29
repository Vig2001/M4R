"""Conitnuation of Research Project"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge, ElasticNet

baseline_scores = pd.read_csv("baseline_scores.csv")
baseline_scores.head(10)
