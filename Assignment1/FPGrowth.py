from FPTree import FPTree
import itertools
import IBMReader
import KaggleReader
class FPGrowth():
    def __init__(self, DB, min_sup, min_conf):
        '''
        contructor for FPGrowth object
        it should receive a ditctionary which store transaction database
        and receive min_sup(float) and min_conf(float)
        '''
        if type(min_conf) is not float or type(min_sup) is not float:
            raise ValueError('min_conf and min_sup must be float!')
        if min_conf > 1 or min_sup > 1:
            raise ValueError('min_conf anc min_sup should less than 1')
        self.__DB = DB.copy() # shallow copy transaction database
        self.__FreqItemsets =  list()
        self.__min_sup_count = int(min_sup * len(self.__DB))
        self.__min_conf = min_conf
        self.__FPTree = FPTree() # compressed database, we will access this tree frequently
    #--------- Setter -------------
    def __update_FreqItemsets(self, Lk):
        '''
        append Lk into freqent itemsets
        Parameter:
            Lk(list of sets) : frequent k itemsets
        Return: None
        '''
        for item in Lk:
            self.__FreqItemsets.append(item)
    #--------- Setter -------------
    #---------- Getter -----------
    def Get_FreqItemsets(self):
        '''
        Getter of Candidates
        Parameter : None
        Return : a list of sets
        '''
        return self.__FreqItemsets
    #---------- Getter -----------
    def __count_support(self, item):
        '''
        receive a item  and count support count of each item
        Parameter : 
            item(set) : an item 
        Return:
            supcnt(int) : support count of input item
        '''
        supcnt = 0
        for items in self.__DB.values():
            if item.issubset(items):
                supcnt = supcnt + 1
        return supcnt
    
    def __remove_item(self, ck):
        '''
        remove those item which dose not fulfill min support count
        return a new candidate sets and clear old ones
        Parameter:
            ck(list of sets) : candidate sets
        return : candidates which elements fulfill min support count
        '''
        newck = [ item for item in ck if not self.__count_support(item) < self.__min_sup_count]
        ck.clear()
        return newck
    
    def __find_subset(self, item, k):
        '''
        Helper function to find subset of item with cardinality k
        ex: k = 2 -> find subsets with cardinality 2
        Parameter :
            item(set)
            k(int)
        Return :
            (list of sets) : subsets of item with cardinality k
        '''
        return  [ set(i) for i in itertools.combinations(item, k) ]

    def Run_FPGrowth(self):
        '''
        Public function to run FPGrowth algo to generate frequent itemsets
        Parameter: none
        Return: none
        '''
        # scan DB to find frequent 1-item set and build a dictionary which key is string type implies item and value is count of that item
        # This dictionary store ordered transaction entity
        # e.g {'f':4, 'c':4, 'a':3}
        raise NotImplementedError('Run_FPGrowth is not implemented')
            

if __name__ == '__main__':
    try:
        KAGGLE_DATA_PATH='Assignment1/GroceryStoreDataSet.csv'
        DB = KaggleReader.DataReader(KAGGLE_DATA_PATH)
        FP_G = FPGrowth(DB, min_sup=0.5, min_conf=0.66)
    except ValueError as e:
        print(str(e))