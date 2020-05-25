import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import argparse

# usage python3 random_forest.py "--criterion=gini" "--max_depth=3"

def main(args):
    iris_data = pd.read_csv('./data/iris.csv',index_col=0)
    # print(iris_data)
    from sklearn.model_selection import train_test_split
    X = iris_data.values[:,0:4]
    Y = iris_data.values[:,4]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=12)

    # Randomforest is one of the highly accurate nonlinear algorithm, which works on the principle of Decision Tree Classification.
    model = RandomForestClassifier(max_depth=args.max_depth,criterion=args.criterion)
    model.fit(x_train,y_train)
    print('train_accuracy:',model.score(x_train,y_train))
    print('test_accuracy:',model.score(x_test,y_test))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="train random_forest",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--max_depth', type=int, default=10,
                        help='The maximum depth of the tree')
    parser.add_argument('--criterion', type=str, default='gini',
                        help='The function to measure the quality of a split')
    args = parser.parse_args()
    main(args)
