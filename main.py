# Modules
import pandas as pd

# Custom modules
from knn import *
from api import *
from cleaner import *

RESULT_FILEPATH = "./results/new_workloads"

def main():
    data = test_request_data()
    newData = test_request_new_data()
    X, y, X_new, workloads = run_cleaner(data, newData)
    classifications = run_knn(X, y, X_new)
    results = get_resulting_workloads(classifications)
    
    results.to_csv(RESULT_FILEPATH)
    

if __name__ == "__main__":
    main()
    