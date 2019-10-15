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
        self.__min_sup_count = 0

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
        return a new candidate sets and clear old ones
        Parameter:
            ck(list of sets) : candidate sets
        return : candidates which elements fulfill min support count
        '''
        newck = [ item for item in ck if not self.__count_support(item) < self.__min_sup_count]
        ck.clear()
        return newck
                


    def __gencandidate(self, lk_1, k):
        '''
        reveive k-1 itemsets and return k itemsets candidate
        Parameter :
            lk_1(list of sets) : k-1 itemsets
            k(int) : 
        Return :
            ck ( list of sets ) : k itemsets
        '''
        ck = list(set())
        i = 0
        j = i+1
        # join
        while i < len(lk_1):
            while j < len(lk_1):
                temp = lk_1[i].union(lk_1[j])
                if ( temp not in ck ) and ( len(lk_1[i].intersection(lk_1[j])) != k-2 ) :
                    ck.append(temp)
                j=j+1
            i=i+1
        # prune


        
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
        self.__min_sup_count = int(min_sup * len(self.__DB))
        Lk_1 = list(set()) # frequent k-1 itemsets
        Lk = list(set()) # frequent k itemsets
        Ck = list(set()) # k-itemset candidates
        L1 = set()
        for item in self.__DB.values():
            if item not in L1:
                L1 = L1.union(item)
        L1 = [ {i} for i in L1 ]
        Lk_1 = self.__remove_item(L1)
        k = 2
        while len(Lk_1) != 0:
            # generate Ck
            pass
