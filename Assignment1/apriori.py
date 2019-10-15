import IBMReader
import KaggleReader
class Apriori():
    def __init__(self, DB):
        '''
        constructor for Apriori object
        it should receive a ditctionary which store transaction database
        '''
        self.__DB = DB.copy() # shallow copy transaction database
        self.__Candidates =  list(set())

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
        remove those item which dose not fullfil min support count
        Parameter:
            ck(set) : candidate sets
        return : None
        '''


    def __join(self):
        '''

        '''

    def Get_Candidates(self):
        '''
        Getter of Candidates
        Parameter : None
        Return : a list of sets
        '''
        return self.__Candidates

    def Run_Apriori(self, min_sup):
        '''
        Public function to run apriori algo to generate candidates
        Parameter : 
            min_sup(int) : minimum support count
        Return :
            None
        '''
        Lk = list(set()) 
        Ck = list(set())
        L1 = set()
        for item in self.__DB.values():
            if item not in L1:
                L1 = L1.union(item)
        L1 = [ {i} for i in L1 ]
        