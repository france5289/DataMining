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
        self.__root = Node() if node is None else node
        
    #-----------Getter-----------
    def GetRoot(self):
        '''
        Return root node of FPTree \n
        Parameter : none \n
        Return : Node object \n
        '''
        return self.__root
    #-----------Getter-----------
    
    #-----------Setter-----------
    def ContructPatternPath(self, startnode, pattern):
        '''
        contruct pattern path from root node \n
        if startnode is None then it start from root node \n
        this function is recursive function with base case when pattern is empty \n
        Parameter: \n
            pattern(lits of string)
            startnode(Node obj.)
        '''
        # base case
        if len(pattern) == 0:
            print('Pattern path constructed')
            return
        if startnode is None: # start from root
            startnode = self.__root
        insert_item = pattern[0] # it is a string
        insert_itemset = {insert_item} # it is a set
        # check insert_itemset is startnode's child or not
        for child in startnode.getChilds():
            if child.getItem() == insert_itemset:
                child.addSupCount(1)
                pattern.remove(insert_item)
                return self.ContructPatternPath(startnode = child, pattern=pattern)
        # if insert_itemset is not startnode's child
        newnode = Node(item=insert_itemset, supcnt=1, parent=startnode)
        startnode.addChild(newnode)
        pattern.remove(insert_item)
        return self.ContructPatternPath(startnode=newnode, pattern=pattern)

    #-----------Setter-----------
    
    def PreorderTraversal(self, startnode = None):
        '''
        traverse tree preorderly
        '''
        if startnode is None:
            startnode = self.__root
        print('Node: ',startnode.getItem())
        print('Supcnt: ',startnode.getSupcnt())
        for child in startnode.getChilds():
            self.PreorderTraversal(startnode=child)


if __name__ == '__main__':
    Tree = FPTree()
    print(Tree.GetRoot())
    transactions = [    ['Bread', 'Milk', 'Beer'], 
                        ['Bread', 'Coffee'],
                        ['Bread', 'Egg'] ] 
    for tranc in transactions:
        Tree.ContructPatternPath(startnode = None,pattern = tranc)
    Tree.PreorderTraversal()