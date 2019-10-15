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
