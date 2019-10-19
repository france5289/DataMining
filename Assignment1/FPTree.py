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
        self.__root = Node() if type(node) is None else node
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
            pattern(lits of sets)
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
        if startnode.getItem() == insert_itemset:
            startnode.addItem(insert_itemset)
            pattern.remove(insert_item)
            return self.ContructPatternPath(startnode, pattern)
        else:
            for child in startnode.getChilds():
                if child.getItem() == insert_itemset:
                    child.addItem(insert_itemset)
                    pattern.remove(insert_item)
                    return self.ContructPatternPath(child, pattern)
            # if the following codes are executed
            # it implies maybe this node don't have any child or its childs' item don't fit insert_itemset
            # we have to create a new node
            newnode = Node(item = insert_itemset, supcnt=1, parent=startnode)
            startnode.addChild(newnode)
            pattern.remove(insert_item)
            return self.ContructPatternPath(newnode, pattern)
    #-----------Setter-----------
    

if __name__ == '__main__':
    # FPTree.InsertPattern(parentnode=a.getroot(), {1,2,3})
    pass