# Moduless
import pandas as pd
from utils.config import *

# Body
def request_data(path):
    return pd.read_csv(path)
