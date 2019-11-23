# -*- coding: utf-8 -*-
'''
This is a data generator for classification practice. This dataset is based on a restaurant waiting setting.
The table below shows the details of the attributes of the generated dataset.
| Alternatives | isBusy  | isHungry | Price | Patrons | estWait | Reserve | Weather | DayOfWeek | Cuisine | Label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/0 | 1/0 | 1~5 | 1~3 | 1/0 | 0~60  | 1/0 | "Sunny", "Rainy", "Cloudy" | "Sun"~"Sat" | "Japanese" "Korean" et al. | 1/0 |
The dataset is then finally exported to a `.csv` file.
'''
# Import Required Modules
import numpy as np
import pandas as pd
import os
import random

class DataGenerator:
    def __init__(self):
        '''
        Constructor for DataGenerator class
        Parameters:
            attributes(list of str) = column names(attributes) 
        '''
        self.attributes = ["Alternatives", "isBusy", "isHungry", "Price", "Patrons", "estWait", "Reserved", "Weather", "DayOfWeek", "Cuisine", "Label"]

    def generator(self, cnt=None, seed=None):
        '''
        Input: 
            cnt(int) = number of data(rows)
            seed(int) = initialize random seed
        Output:
            df(DataFrame) = data frame
        '''
        df = pd.DataFrame(columns=self.attributes)
        if cnt is None:
            cnt = 500
        elif type(cnt) is not int or cnt <= 0:
            raise ValueError("Count input must be an integer > 0.")
        if seed is None:
            seed = None
        elif type(seed) is not int or seed < 0:
            raise ValueError("Seed must be an integer")

        random.seed(seed)

        for i in range(cnt):
            d = {}
            # Generate attributes & value
            d["isBusy"] = random.randint(0,1)
            d["isHungry"] = random.randint(0,5)
            d["Price"] = random.choice(['$','$$','$$$'])
            d["Patrons"] = random.randint(1,10)
            if d["Price"] is '$$$':
                res_weight = [1] * 75 + [0] * 25
            else:
                res_weight = [1] * 10 + [0] * 90
            d["Reserved"] = random.choice(res_weight)
            if d["Reserved"] is 1:
                d["estWait"] = random.randint(5,10)
            elif d["Patrons"] >= 5:
                d["estWait"] = random.randint(25, 60)
            elif d["Patrons"] < 5:
                d["estWait"] = random.randint(5, 30)
            d["Companion"] = random.randint(0, 1)
            d["Transport"] = random.choice(["Walk", "Cycle", "Bus", "Motor", "Car"])
            if d["Transport"] is "Motorcycle" or d["Transport"] is ["Car"]:
                alt_weight = [0] * 15 + [1] * 85
                d["Alternatives"] = random.choice(alt_weight)
            else:
                d["Alternatives"] = random.randint(0,1)
            d["Weather"] = random.choice(["Rainy", "Sunny", "Cloudy"])
            d["DayOfWeek"] = random.choice(["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"])
            d["Cuisine"] = random.choice(["Japanese", "Korean", "Italian", "French", "Spanish"])
            
            # Generate rules for label
            if d["Reserved"] is 1: d["Label"] = 1
            else:
                if d["estWait"] <= 15: d["Label"] = 1
                elif d["estWait"] >= 50: d["Label"] = 0
                else:
                    if d["Transport"] is "Bus": d["Label"] = 1
                    else:
                        if d["Weather"] is 'Rainy': d["Label"] = 1
                        else: 
                            if d["Price"] is '$' or d["Price"] is '$$$': d["Label"] = 1
                            else:
                                if d["Alternatives"] is 1 and d["isBusy"] is 1: d["Label"] = 0
                                elif d["Patrons"] > 8: d["Label"] = 0
                                else: d["Label"] = 1
            
            # d["Label"] = random.randint(0,1)
            df = df.append(d, ignore_index=True)
        return df
    
    def save_data(self, df, path=None):
        '''
        Input: 
            df(Data Frame) = data frame object containing generated data
            path(str) = path to save file
        '''
        if path is None:
            path = "data/data.csv"
        elif type(path) is not str:
            raise OSError("Path should be `str` type.")
        elif len(path.split('/')) >= 3:
            path = path.split('/')[-2] + path.split('/')[-1]
        
        if not os.path.exists(path):
            os.makedirs(path.split('/')[-2])

        df.to_csv(path, index=None, header=True)

if __name__ == '__main__':
    try:
        gen = DataGenerator()
        df = gen.generator(cnt=10, seed=1)
        print(df.head())
    except ValueError as e:
        print(str(e)) 
