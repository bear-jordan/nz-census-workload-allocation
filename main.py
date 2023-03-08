# Modules
import pandas as pd

# Custom Modules
from utils.parser import *
from utils.knn import *
from utils.api import *
from utils.cleaner import *

# Body
def main():
    wcatPath, databasePath = run_parser()
    data = request_data(databasePath)
    newData = request_data(wcatPath)
    X, y, X_new = run_cleaner(data, newData)
    classifications = run_knn(X, y, X_new)
    results = get_resulting_workloads(classifications, data, newData)
    results.to_csv(RESULT_FILEPATH, index=False)
    
if __name__ == "__main__":
    main()
    print("Allocation complete. Check the results folder.")
    