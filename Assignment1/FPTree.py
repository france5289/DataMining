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
    def __FindPath(self, startnode, path, cnt ):
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
        if parent in path.keys():
            path[parent] = path[parent] + cnt 
        else:
            path.update({parent:cnt})
        self.__FindPath(startnode = parent, path = path, cnt = cnt)

    def __FindPattern(self, startnode, freqpattern, temp, cnt):
        '''
        Find all possible relative pattern form startnode \n
        Parameter: \n
            startnode(Node obj.) : where to start \n
            freqpattern(dict) : store frequent pattern item and count \n
            temp : store temporally generated freqpattern \n
        '''
        if startnode is None:
            return
        if startnode.getNodeLevel() == 1 : # root node
            if str(temp) not in freqpattern.keys() and len(temp) != 0:
                freqpattern.update({str(temp):cnt})
                return
            if str(temp) in freqpattern.keys():
                freqpattern[str(temp)] = freqpattern[str(temp)] + cnt
                return
            return
        self.__FindPattern(startnode.getParent(), freqpattern, temp, cnt)
        temp2 = temp.copy()
        temp2.update({startnode.getItem()})
        self.__FindPattern(startnode.getParent(), freqpattern, temp2, cnt)

    def TreeMining(self, item, min_sup_cnt):
        '''
        return frequent pattern with relative item \n
        e.g ['Bread->Egg', 4] \n
        Parameter : \n
            item(str) \n
            min_sup_cnt(int) \n
        Return : \n
            freqpattern(list) : contain frequent pattern and relative support count \n
        '''
        path = dict() # e.g { <Node obj.> : cnt }
        pattern = dict() # e.g {"{'Bread'}":4, ....}
        temp = set()
        for node in self.__headerTable[item]:
            self.__FindPath(startnode=node, path=path, cnt = node.getSupcnt())
        for node, count in path.items():
            temp= {node.getItem()}
            self.__FindPattern(startnode=node.getParent(), freqpattern=pattern, temp=temp, cnt=count)
        freqpattern = [ pair for pair in pattern.items() if pair[1] >= min_sup_cnt ]
        freqpattern = [[ pair[0].strip("{}"), pair[1]]  for pair in freqpattern]
        freqpattern = [ [ pair[0].replace("'", ""), pair[1]] for pair in freqpattern]
        freqpattern = [ [ pair[0] +'->' + str(item), pair[1]  ]  for pair in freqpattern]
        return freqpattern

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

    # print(Tree.__str__())
    #for i in Tree.GetHeaderTable().items():
    #    print(i)
    Tree.TreeMining('Egg', 2)