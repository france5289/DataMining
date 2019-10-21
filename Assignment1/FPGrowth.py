from FPTree import FPTree
import itertools
import IBMReader
import KaggleReader
import copy
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
        self.__OrderedDB = list()
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
    def GetFPTree(self):
        '''
        Return FPTree object
        '''
        return self.__FPTree
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
    
    
    def __ConstructFPTree(self):
        '''
        When we get OrderedDB use this method to construct FPTree \n
        If OrderedDB is empty raise ValueError \n
        Parameter : none \n
        Return : none \n
        '''
        if len(self.__OrderedDB) == 0:
            raise ValueError('Oedered DB is empty! Can not construct FP Tree')
        for tranc in self.__OrderedDB: # tranc is something like ['bread', 'coffee'...]
            if len(tranc) != 0:
                self.__FPTree.ContructPatternPath(startnode=None, pattern=tranc)
    
    def Run_FPGrowth(self):
        '''
        Public function to run FPGrowth algo to generate frequent itemsets \n
        Parameter: none \n
        Return: none
        '''
        # find frequent-1 itemset and consturct look up table(dict(string : int))
        L1 = set()
        for item in self.__DB.values():
            if item not in L1:
                L1 = L1.union(item)
        L1 = [{i} for i in L1]
        C1 = self.__remove_item(L1)
        table = dict()
        for item in C1: # type(item) is set
            element = item.pop()
            count = self.__count_support({element})
            table.update({element:count})
        # sort look up table
        sorted_table = sorted(table.items(), key=lambda kv: kv[1], reverse=True)
        # sorted_table is a list of tuple e.g [('f', 4), ('c', 3)...]
        # use sorted_table to create new transaction database with ordered transactions
        # new transaction database will be a list
        temp = list()
        for trancs in self.__DB.values():
            # trancs should be {'b', 'f', 'h', 'j', 'o'}
            for item in sorted_table:
                if item[0] in trancs:
                    temp.append(item[0])
            # end inner for loop it should generate something like ['f','b'...]
            self.__OrderedDB.append(temp.copy()) # OrderedDB is something like [['bread','coffee'],['tea','coffee']]
            temp.clear()
        # now we have constructed Ordered Data Base correctly
        # now we need to construct FP-Tree
        self.__ConstructFPTree()
        F1 = sorted(table.items(), key=lambda kv: kv[1])
        # F1 is frequent 1-itemset , which is something like [('a',2),...,('f',4)]
        F1 = [ [ item[0], item[1] ] for item in F1 ] # F1 = [ ['a', 2],....,['f',4] ]
        for item in F1:
            self.__update_FreqItemsets(item)
        # find other frequent patterns
        for item in F1:
            freqpattern = self.__FPTree.TreeMining(item[0], self.__min_sup_count)
            for pattern in freqpattern:
                self.__update_FreqItemsets(pattern)


if __name__ == '__main__':
    try:
        KAGGLE_DATA_PATH='Assignment1/GroceryStoreDataSet.csv'
        DB = KaggleReader.DataReader(KAGGLE_DATA_PATH)
        FP_G = FPGrowth(DB, min_sup=0.2, min_conf=0.66)
        FP_G.Run_FPGrowth()
        #print(FP_G.GetFPTree().GetRoot().__str__())
        for i in FP_G.Get_FreqItemsets():
            print(i)
    except ValueError as e:
        print(str(e))
    except NotImplementedError as e2:
        print(str(e2))