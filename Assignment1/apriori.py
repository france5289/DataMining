import IBMReader
import KaggleReader
import itertools
import os
class Apriori():
    def __init__(self, DB, min_sup, min_conf):
        '''
        constructor for Apriori object
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
            k1_subset = self.__find_subset(item, k-1)
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
        


    def Run_Apriori(self):
        '''
        Public function to run apriori algo to generate candidates
        Return :
            None
        '''
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
            # check support count fulfillment
            Lk = self.__remove_item(Ck)
            self.__update_FreqItemsets(Lk)
            Lk_1 = Lk
            k = k + 1

    def RuleGenerator(self):
        '''
        Generator function to generate association rule
        It will yield an association rule every time called
        ex: consider rule : {a,d} -> {c,e,f,g} with confidence = 0.4 and support = 2000
            it will yied a list of sets : [{a,d}, {c,e,f,g}, 0.4 , 2000]
        '''
        if len(self.__FreqItemsets) == 0:
            raise ValueError('Frequent Itemsets list is empty ! Can not generate any rule !')
        for item in self.__FreqItemsets: # item is a set
            # generate all subsets of item
            if len(item) == 1:
                continue 
            for n in range(1,len(item) ):
                n_subset = self.__find_subset(item, n)
                for subset in n_subset:
                    conf = self.__count_support(item) / self.__count_support(subset)
                    if conf >= self.__min_conf:
                        yield [ subset, item.symmetric_difference(subset), float(conf), self.__count_support(item) ]

if __name__ == '__main__':
    try:
        # use simple testing data to test correctness
        #DB = {10:{'A','C','D'}, 20:{'B','C','E'}, 30:{'A','B','C','E'}, 40:{'B','E'}}
        DB = KaggleReader.DataReader( os.getcwd() + '/GroceryStoreDataSet.csv')
        a = Apriori(DB, min_sup=0.2, min_conf=0.4)
        a.Run_Apriori()
        Freq = a.Get_FreqItemsets()
        for i in Freq:
            print(i)
        for i, rule in enumerate(a.RuleGenerator()):
            print("Rule Num {:<}: {} -> {} conf: {:<.3f} sup: {:<}".format(i+1 , rule[0], rule[1], rule[2], rule[3]))
    except ValueError as e:
        print(str(e))