def DataReader( filename ):
    '''
    Helper function to read IBM Quest Synthetic data.
    It receive a filename and return a dictionary 
    { Transaction ID : list( Item ID ) }
    Parameter : 
        filename (str) : data filename (ex: 'input.data', 'input.csv')
    Return value:
        a dictionary 
    '''
    transactions = dict()
    with open(filename, 'r') as f:
        for line in f:
            obj = line.split()
            TID = obj[1]
            ItemID = obj[2]
            if TID in transactions: # check key TID exist or not
                transactions[TID].append(ItemID)
            else: # key value pair dosen't exist then update dictionary 
                transactions.update({TID : [ItemID] })    
    return transactions        

if __name__ == '__main__':
    #filename = input('Please enter entire filename:\n')
    DB = DataReader('/home/kychen/Desktop/DataMining/Assignment1/output.data')
    for item in DB.items():
        print(item)