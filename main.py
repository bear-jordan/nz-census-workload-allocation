# Modules
import pandas as pd

# Custom Modules
from knn import *
from api import *
from cleaner import *

# Global Variables
RESULT_FILEPATH = "./results/prod-new-workloads.csv"

# Body
def main():
    data = prod_request_data()
    newData = prod_request_new_data()
    X, y, X_new, _ = run_cleaner(data, newData)
    classifications = run_knn(X, y, X_new)
    results = get_resulting_workloads(classifications, data, newData)
    results.to_csv(RESULT_FILEPATH, index=False)
    
if __name__ == "__main__":
    main()
    