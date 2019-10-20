from Node import Node
class FPTree():
    def __init__(self, node=None):
        '''
        constructor for Tree object
        it can receive a Node object which will be the root node of the tree \n
        Parameter:
            node(optional)(Node obj.)
            if node parameter value is None, then it will create a NULL node as root node \n
        Return: none
        '''
        self.__root = Node(level=1) if node is None else node
        self.__headerTable = dict() # this table record position of a Node obj.
        # e.g                    root 
        #                       /
        #               <Node.obj( item = 'Bread' ) at 0x10ab53b90> 
        # self.__headerTable :  { 'Bread': [ <Node.obj at 0x10ab53b90 ] }
    def __str__(self):
        return self.__root.__str__()
    #-----------Getter-----------
    def GetRoot(self):
        '''
        Return root node of FPTree \n
        Parameter : none \n
        Return : Node object \n
        '''
        return self.__root
    def GetHeaderTable(self):
        '''
        Return header Table of FPTree \n
        Parameter : none \n
        Return : dict with {key:value} = { Node.item(str) : list of Node object(list) }
        '''
        return self.__headerTable
    #-----------Getter-----------
    #-----------Setter-----------
    def __insertHederTable(self, node):
        '''
        Insert Node object into header table \n
        Parameter: node (Node obj.) \n
        Return : No return value \n
        '''
        key = node.getItem()
        if key in self.__headerTable.keys():
            self.__headerTable[key].append(node)
        else:
            self.__headerTable.update({key:[node]})
    #-----------Setter-----------
    def __FindPath(self, startnode, path):
        ''' 
        Find a path from startnode to root \n
        Parameter: \n
            startnode(Node obj.): where to start 
            path(dict) : a dictionary with key value pair { Node obj : count }
        Return: none, we will save our path into 'path' parameter
        '''
        # base case
        parent = startnode.getParent()
        if parent.getNodeLevel() == 1: # parent is root
            return
        path.update({parent:parent.getSupcnt()})
        self.__FindPath(startnode = parent, path = path)

    def __FindPattern(self, startnode, freqpattern, temp):
        '''
        Find all possible relative pattern form startnode \n
        Parameter: \n
            startnode(Node obj.) : where to start \n
            freqpattern(list of sets) : store frequent pattern sets \n
            temp : store temporally generated freqpattern \n
        '''
        
        if startnode.getNodeLevel() == 1 : # root node
            if temp not in freqpattern and len(temp) != 0:
                freqpattern.append(temp)
            return
        
        self.__FindPattern(startnode.getParent(), freqpattern, temp)
        temp2 = temp.copy()
        temp2.update({startnode.getItem()})
        self.__FindPattern(startnode.getParent(), freqpattern, temp2)

    def TreeMining(self, item):
        '''
        
        Parameter : \n
            item(str) \n
        Return : \n
            freqpattern()
        '''
        path = dict()
        freqpattern = list()
        temp = set()
        for node in self.__headerTable[item]:
            self.__FindPath(startnode=node, path=path)
        for node in path:
            self.__FindPattern(startnode=node, freqpattern=freqpattern, temp=temp)
        
        print(freqpattern)


    def ContructPatternPath(self, startnode, pattern):
        '''
        contruct pattern path from root node \n
        if startnode is None then it start from root node \n
        this function is recursive function with base case that pattern is empty \n
        Parameter: \n
            pattern(lits of string)
            startnode(Node obj.)
        '''
        # base case
        if len(pattern) == 0:
            return
        if startnode is None: # start from root
            startnode = self.__root
        insert_item = pattern.pop(0) # it is a string
        # check insert_itemset is startnode's child or not
        for child in startnode.getChilds():
            if child.getItem() == insert_item:
                child.addSupCount(1)
                return self.ContructPatternPath(startnode = child, pattern=pattern)
        # if insert_itemset is not startnode's child
        newnode = Node(item=insert_item, supcnt=1, parent=startnode, level=startnode.getNodeLevel() + 1)
        startnode.addChild(newnode)
        self.__insertHederTable(newnode)
        return self.ContructPatternPath(startnode=newnode, pattern=pattern)

    
    

if __name__ == '__main__':
    Tree = FPTree()
    transactions = [    ['Bread', 'Milk', 'Beer'], 
                        ['Bread', 'Coffee'],
                        ['Bread', 'Egg'],
                        ['Bread', 'Milk', 'Coffee'],
                        ['Milk', 'Egg'],
                        ['Bread', 'Milk', 'Egg', 'Beer'],
                        ['Bread', 'Milk', 'Egg'],
                        ['Bread', 'Egg'],
                        ['Milk', 'Egg'] ] 
    for tranc in transactions:
        Tree.ContructPatternPath(startnode = None,pattern = tranc)

    print(Tree.__str__())
    #for i in Tree.GetHeaderTable().items():
    #    print(i)
    Tree.TreeMining('Beer')