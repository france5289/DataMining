from player_data_generator import PlayerDataGenerator
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_graphviz
from sklearn.linear_model import LogisticRegressionCV
import pydotplus
from sklearn.externals.six import StringIO 
if __name__ == '__main__':
    train = PlayerDataGenerator.Batting_data_Generate(player_num=1000)
    train.drop(['OBP', 'SLG', 'OPS', 'BA', 'SB', 'SO', 'RBI'], axis = 1, inplace = True)
    X = train.drop(['Rank'], axis=1)
    features = X.columns
    y = train['Rank']
    X = X.to_numpy()
    y = y.to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    print('Generate training data finished! Lets train a Decision Tree!')
    tree_clf = DecisionTreeClassifier(random_state=42, max_depth=4)
    tree_clf.fit(X_train,y_train)
    print('Run cross validation!')
    f1_scores = cross_val_score(tree_clf, X_train, y_train, cv=10, scoring='f1_micro') 
    tree_f1_mean = f1_scores.mean()
    print(f'Decision Tree Classifier mean F1 score: {tree_f1_mean}')
    treeDataPath = './tree.pdf'
    dot_data = StringIO()
    export_graphviz(tree_clf, out_file=dot_data, filled=True, feature_names=features, class_names=['A', 'B', 'C'], special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_pdf(treeDataPath)
    print('Now use Softmax Regression!')
    Softmax_clf = LogisticRegressionCV(cv=10, multi_class='multinomial', random_state=42, Cs=5, scoring='f1_micro').fit(X_train,y_train)
    print(f'Softmax regression F1 score: {Softmax_clf.score(X_test,y_test)}')