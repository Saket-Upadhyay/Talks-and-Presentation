from sklearn import  linear_model, metrics 
from sklearn.model_selection import train_test_split 
import pandas as pd
import numpy as np 
from sklearn.metrics import confusion_matrix 
import pickle
def main():
    file = pd.read_csv("<PUT YOUR DATASET HERE>")
    coulmnNames = file.iloc[1:1, 1:].columns
    FeatureNames = list(coulmnNames[1:-1])
    LabelName = coulmnNames[-1]
    X = file[FeatureNames]
    X = np.asarray(X)
    Y = file[LabelName]
    Y = np.asarray(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1) 
   
    
    reg = linear_model.LogisticRegression(solver='lbfgs') 
    reg.fit(X_train, y_train) 
    predictions = reg.predict(X_test) 
    print(reg.predict_proba(X_test))
    print("Logistic Regression model accuracy(in %):",  
    metrics.accuracy_score(y_test, predictions)*100) 
    for i in range(0,5):
            print ("Actual outcome :: {} and Predicted outcome :: {}".format(list(y_test)[i], predictions[i]))
 
    print (" Confusion matrix ", confusion_matrix(y_test, predictions))

    pickle.dump(reg,open("LOGREGRESSION.model",'wb'))
    
if __name__ == "__main__":
    main()
