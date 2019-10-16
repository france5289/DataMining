import IBMReader
import KaggleReader
import itertools
class Apriori():
    def __init__(self, DB):
        '''
        constructor for Apriori object
        it should receive a ditctionary which store transaction database
        '''
        self.__DB = DB.copy() # shallow copy transaction database
        self.__FreqItemsets =  list()
        self.__min_sup_count = 0

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
        receive k-1 itemsets and return k itemsets candidate
        Parameter :
            lk_1(list of sets) : k-1 itemsets
            k(int) : 
        Return :
            ck ( list of sets ) : k itemsets
        '''
        #-------------------------------- inner function ----------------------
        def find_k1_subset(item, k):
            '''
            Helper function to find k-1 subset of items 
            Parameter :
                item(set)
                k(int)
            Return :
                k_1_subset(list of sets) : k-1 subset of item
            '''
            return  [ set(i) for i in itertools.combinations(item, k-1)]
        
        def pruned(lk_1, item, k):
            '''
            Check item should be pruned or not
            Parameter:
                lk_1(list of sets) : k-1 itemsets
                item(set) : item in K-candidate
                k(int)
            Return:
                Boolean: True means this item should be pruned
            '''
            k1_subset = find_k1_subset(item, k)
            for i in k1_subset:
                if i not in lk_1:
                    return True
            return False
        #-------------------------------- inner function ----------------------

        ck = list(set())
        i = 0
        j = i+1
        # join
        while i < len(lk_1):
            while j < len(lk_1):
                temp = lk_1[i].union(lk_1[j])
                if ( temp not in ck ) and ( len(lk_1[i].intersection(lk_1[j])) == k-2 ) :
                    ck.append(temp)
                j=j+1
            i=i+1
            j=i+1
        # prune
        ck = [ item for item in ck if not pruned(lk_1, item, k) ]
        return ck
        


    def Run_Apriori(self, min_sup):
        '''
        Public function to run apriori algo to generate candidates
        Parameter : 
            min_sup(int) : minimum support count
        Return :
            None
        '''
        self.__min_sup_count = int(min_sup * len(self.__DB))
        Lk_1 = list(set()) # frequent k-1 itemset
        Lk = list(set()) # frequent k itemset
        Ck = list(set()) # k-itemset candidates
        L1 = set()
        for item in self.__DB.values():
            if item not in L1:
                L1 = L1.union(item)
        L1 = [ {i} for i in L1 ]
        Lk_1 = self.__remove_item(L1)
        k = 2
        self.__update_FreqItemsets(Lk_1)
        while len(Lk_1) != 0:
            # generate Ck
            Ck = self.__gencandidate(Lk_1, k)
            # check support count fullfillment
            Lk = self.__remove_item(Ck)
            self.__update_FreqItemsets(Lk)
            Lk_1 = Lk
            k = k + 1
    def RuleGenerator(self):
        '''
        Generator function to generate association rule
        '''
if __name__ == '__main__':
    DB = {10:{'A','C','D'}, 20:{'B','C','E'}, 30:{'A','B','C','E'}, 40:{'B','E'}}
    a = Apriori(DB)
    a.Run_Apriori(0.5)
    print(a.Get_FreqItemsets())
