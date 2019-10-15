def DataReader(filename):
    '''
    Helper function to read file : 'GroceryStoreDataSet.csv' from Kaggle
    It will return a dict of sets: { Transaction ID : set( Item ID ) }
    Parameter : 
            filename(str): full file name
    Return:
            python dictionary of sets
    '''
    transactions = dict()
    with open(filename, 'r') as f:
        for count, line in enumerate(f, 1):
            # count is Transaction ID and key in dict
            line = line.strip('"\n').split(',')
            transactions.update({count : set(line)})
    
    return transactions

if __name__ == '__main__':
    filename = input('Please enter full filename\n')
    DB = DataReader(filename)
    for item in DB.items():
        print(item)
