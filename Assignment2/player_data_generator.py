'''
This file provide a object which is reponsible to generate baseball player data
'''
import numpy as np
import pandas as pd
import os
import random
from tqdm import tqdm
class BattingDataGenerator:
    def __init__(self):        
        pass

    def Generate(self, player_num=500,seed=42):
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
        rows['AB'] = [ random.randint(100,700)  for _ in range(500) ]
        rows['H'] = [ random.randint(50,200) for _ in range(500) ]
        rows['2B'] = [ random.randint(0,50) for _ in range(500) ]
        rows['3B'] = [ random.randint(0,20) for _ in range(500) ]
        rows['HR'] = [ random.randint(0,60) for _ in range(500) ]
        rows['RBI'] = [ random.randint(0,150) for _ in range(500) ]
        rows['SB'] = [ random.randint(1,45) for _ in range(500) ]
        rows['BB'] = [ random.randint(1,150) for _ in range(500) ]
        rows['SO'] = [ random.randint(1,200) for _ in range(500) ]
        rows['HBP'] = [ random.randint(0,30) for _ in range(500) ]
        rows['SF'] = [ random.randint(0,15) for _ in range(500) ]
        dataset = pd.DataFrame(rows)
        dataset['BA'] = dataset['H'] / dataset['AB']
        dataset['OBP'] = ( dataset['H'] + dataset['BB'] + dataset['HBP'] ) / ( dataset['AB'] + dataset['BB'] + dataset['HBP'] + dataset['SF'] )
        dataset['SLG'] = ( dataset['H'] + 2 * dataset['2B'] + 3 * dataset['3B'] + 4 * dataset['HR'] ) / dataset['AB']
        dataset['OPS'] = dataset['OBP'] + dataset['SLG']
        dataset.drop(dataset[dataset['OPS'] >= 2].index, inplace=True) # drop outliers
        stats = dataset.describe()
        ops_max = stats['OPS']['max']
        ops_75 = stats['OPS']['75%']
        ops_S = ( ops_75 + ops_max ) / 2
        ops_50 = stats['OPS']['50%']
        ops_25 = stats['OPS']['25%']
        
        def Evaluate(ops):
            if ops >= ops_S and ops <= ops_max :
                return 'S'
            elif ops >= ops_75 and ops < ops_S :
                return 'A'
            elif ops >= ops_50 and ops < ops_75 :
                return 'B'
            elif ops >= ops_25 and ops < ops_50 :
                return 'C'
            else:
                return 'E'
        dataset['Rank'] = dataset['OPS'].apply(func=Evaluate)
            
        return dataset

if __name__ == '__main__':
    datagenerator = BattingDataGenerator()
    data = datagenerator.Generate()
    print(data.head())
