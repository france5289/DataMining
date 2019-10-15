def DataReader( filename ):
    '''
    Helper function to read IBM Quest Synthetic data.
    It receive a filename and return a dictionary 
    { Transaction ID : set( customer ID, Item ID ) }
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
            customerID = obj[0]
            item = obj[2]
            value = set()
            value.update([customerID, item])
            transactions.update(zip(TID, value))

    return transactions        

