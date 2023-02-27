from sklearn.neighbors import KNeighborsClassifier

def fit_knn(X, y):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X, y)
    
    return model
    
def predict_knn(model, X_test):
    return model.predict(X_test)
    
def run_knn(X, y, X_test):
    model = fit_knn(X, y)
    predictions = predict_knn(model, X_test)
    
    return predictions