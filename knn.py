from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder()

def encode(y):
    encoder = LabelEncoder()
    yTransform = le.fit_transform(y)
    
    return (y, encoder)
    
def decode(y, encoder):
    return encoder.inverse_transform(y)

def fit_knn(X, y):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X, y)
    
    return model
    
def predict_knn(model, X_new):
    return model.predict(X_new)
    
def run_knn(X, y, X_new):
    y, encoder = encode(y)
    model = fit_knn(X, y)
    predictions = predict_knn(model, X_new)
    predictionsTransform = decode(predictions, encoder)
     
    return predictionsTransform