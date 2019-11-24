from player_data_generator import PlayerDataGenerator
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_graphviz

if __name__ == '__main__':
    train = PlayerDataGenerator.Batting_data_Generate(player_num=1000)
    train.drop(['OBP', 'SLG', 'OPS', 'BA', 'SB', 'SO', 'RBI'], axis = 1, inplace = True)
    train_X = train.drop(['Rank'], axis=1)
    features = train_X.columns
    train_y = train['Rank']
    X = train_X.to_numpy()
    y = train_y.to_numpy()
    print('Generate training data finished! Lets train a Decision Tree!')
    tree_clf = DecisionTreeClassifier(random_state=42, max_depth=4)
    print('Run cross validation!')
    f1_scores = cross_val_score(tree_clf, X, y, cv=10, scoring='f1_micro') 
    tree_f1_mean = f1_scores.mean()
    print(f'Decision Tree Classifier mean F1 score: {tree_f1_mean}')
    tree_clf.fit(X,y)
    tree_graph = export_graphviz(tree_clf, out_file='Batting', feature_names=features, class_names=['A', 'B', 'C'])