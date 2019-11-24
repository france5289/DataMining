'''
This file provide a object which is reponsible to generate baseball player data
'''
import numpy as np
import pandas as pd
import os
import random
from tqdm import tqdm
class PlayerDataGenerator:
    def __init__(self):        
        pass
    @staticmethod
    def Batting_data_Generate(player_num=500,seed=42):
        '''
        given number of players to generate players' data

        Args:
            player_num(int) : how many players' data you want to generate, default:500
            seed(int) : random seed, default:42
        Return:
            dataset(pd.Dataframe)
        '''
        # dataset = pd.DataFrame(columns=self.attrs)
        random.seed(seed)
        rows = {}
        tqdm.pandas()
        rows['AB'] = [ random.randint(100,700)  for _ in range(player_num) ]
        rows['H'] = [ random.randint(50,200) for _ in range(player_num) ]
        rows['2B'] = [ random.randint(0,50) for _ in range(player_num) ]
        rows['3B'] = [ random.randint(0,20) for _ in range(player_num) ]
        rows['HR'] = [ random.randint(0,60) for _ in range(player_num) ]
        rows['RBI'] = [ random.randint(0,150) for _ in range(player_num) ]
        rows['SB'] = [ random.randint(1,45) for _ in range(player_num) ]
        rows['BB'] = [ random.randint(1,150) for _ in range(player_num) ]
        rows['SO'] = [ random.randint(1,200) for _ in range(player_num) ]
        rows['HBP'] = [ random.randint(0,30) for _ in range(player_num) ]
        rows['SF'] = [ random.randint(0,15) for _ in range(player_num) ]
        dataset = pd.DataFrame(rows)
        dataset['BA'] = dataset['H'] / dataset['AB']
        dataset['OBP'] = ( dataset['H'] + dataset['BB'] + dataset['HBP'] ) / ( dataset['AB'] + dataset['BB'] + dataset['HBP'] + dataset['SF'] )
        dataset['SLG'] = ( dataset['H'] + 2 * dataset['2B'] + 3 * dataset['3B'] + 4 * dataset['HR'] ) / dataset['AB']
        dataset['OPS'] = dataset['OBP'] + dataset['SLG']
        dataset.drop(dataset[dataset['OPS'] >= 2].index, inplace=True) # drop outliers
        stats = dataset.describe()
        ops_75 = stats['OPS']['75%']
        ops_50 = stats['OPS']['50%']
        
        def Evaluate(ops):
            if ops >= ops_75 :
                return 'A'
            elif ops >= ops_50 and ops < ops_75:
                return 'B'
            else:
                return 'C'
        
        dataset['Rank'] = dataset['OPS'].progress_apply(func=Evaluate)    
        return dataset

if __name__ == '__main__':
    datagenerator = PlayerDataGenerator()
    data = datagenerator.Batting_data_Generate()
    print(data.head())
