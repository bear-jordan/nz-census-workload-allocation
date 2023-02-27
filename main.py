# Modules
import pandas as pd

# Custom modules
from knn import *
from api import *
from cleaner import *

def main():
    data = request()
    X, y, X_test = clean(data)
    # classifications = run_knn(X, y, X_test)
    

if __name__ == "__main__":
    main()
    