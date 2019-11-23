from player_data_generator import PlayerDataGenerator
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    train = PlayerDataGenerator.Batting_data_Generate(player_num=1000)
    train.drop(['OBP', 'SLG', 'OPS'], axis = 1, inplace = 'True')
    train = train.to_numpy()
