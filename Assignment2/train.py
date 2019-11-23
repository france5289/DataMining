from player_data_generator import PlayerDataGenerator
import numpy as np
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    batting_data = PlayerDataGenerator.Batting_data_Generate()
    