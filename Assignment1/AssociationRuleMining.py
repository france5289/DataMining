import KaggleReader
import IBMReader
from FPGrowth import FPGrowth
from apriori import Apriori
import argparse
import cProfile
import os


if __name__ == '__main__':
    try:
        cwd = os.getcwd()
        KAGGLE_DATA_PATH = cwd + '/GroceryStoreDataSet.csv'
        IBM1_DATA_PATH = cwd + '/output.data'
        IBM2_DATA_PATH = cwd + '/output_50k.data'
        IBM3_DATA_PATH = cwd + '/output_100k.data'
        IBM4_DATA_PATH = cwd + '/output_500.data'
        DB = dict()
        parser = argparse.ArgumentParser()
        parser.add_argument('DATA', help='which data (IBM or KAGGLE) do you want to mine? type "IBM" for IBM dataset "Kaggle" for Kaggle dataset')
        parser.add_argument('MIN_SUP', help='customize minimum support', type=float)
        parser.add_argument('MIN_CONF', help='customize minimum confidence', type=float)
        parser.add_argument('-a', '--association', help='generate association rule?', action='store_true')
        parser.add_argument('-p', '--profile', help='run profiling tools or not?', action='store_true')
        args = parser.parse_args()
        if args.DATA == 'IBM1':
            DB = IBMReader.DataReader(IBM1_DATA_PATH)
        elif args.DATA == 'IBM2':
            DB = IBMReader.DataReader(IBM2_DATA_PATH)
        elif args.DATA == 'IBM3':
            DB = IBMReader.DataReader(IBM3_DATA_PATH)
        elif args.DATA == 'IBM4':
            DB = IBMReader.DataReader(IBM4_DATA_PATH)
        elif args.DATA == 'Kaggle':
            DB = KaggleReader.DataReader(KAGGLE_DATA_PATH)
        else:
            raise ValueError('Invalid dataset!')
        min_sup = args.MIN_SUP
        min_conf = args.MIN_CONF
        APR = Apriori(DB, min_sup, min_conf)
        FPG = FPGrowth(DB, min_sup, min_conf)
        if args.profile:
            print('------------------Run Profiling ( Apriori Algo )---------------------------')
            input('Press any key to continue')
            cProfile.run('APR.Run_Apriori()')
            print('------------------Run Profiling ( FP Growth Algo )---------------------------')
            input('Press any key to continue')
            cProfile.run('FPG.Run_FPGrowth()')
        else: 
            APR.Run_Apriori()
            FPG.Run_FPGrowth()
        
        print('------------------Output Frequent Itemset ( Apriori Algo )---------------------------')
        input('Press any key to continue')
        for item in APR.Get_FreqItemsets():
            print(item)
        print('------------------Output Frequent Itemset ( FP Growth Algo )---------------------------')
        input('Press any key to continue')
        for item in FPG.Get_FreqItemsets():
            print(item)
        input('Press any key to continue')
        if args.association:
            print('------------------Output Association Rule ( Apriori Algo )---------------------------')
            for i,rule in enumerate(APR.RuleGenerator()):
                print("Rule Num {:<}: {} -> {} conf: {:<.3f} sup: {:<}".format(i+1 , rule[0], rule[1], rule[2], rule[3]))
            input('Press any key to continue')
            print('------------------Output Association Rule ( FPGrowth Algo )---------------------------')
            for i,rule in enumerate(FPG.RuleGenerator()):
                print("Rule Num {:<}: {} -> {} conf: {:<.3f} sup: {:<}".format(i+1 , rule[0], rule[1], rule[2], rule[3]))
            input('Press any key to continue')

    except ValueError as e:
        print(str(e))
    except TypeError as e2:
        print(str(e2))