class Node():
    def __init__(self, item=None,supcnt=0,parent=None, child=None):
        '''
        constructor for Node object
        it can receive item(set), supcnt(support count)(int), parent(Node obj) and child(List of Node obj)
        if item is parent is None then it implies this node is root node
        if every attribute in Node is empty it implies this node is NULL node
        '''
        if type(supcnt) is not int:
            raise ValueError('Node __init()__ supcnt paramter just receive integer type')
        if item is None:
            item = set()
        if child is None:
            child = list()
        self.__item = item
        self.__supcnt = supcnt
        self.__parent = parent
        self.__child = child

    #------------Getter---------------
    def getItem(self):
        '''
        return memeber variable of Node obj : '__item' \n
        Return : self.__item(set)
        '''
        return self.__item
    def getChilds(self):
        '''
        return childs of Node
        '''
        return self.__child
    def getParent(self):
        '''
        return parent of Node
        '''
        return self.__parent
    def getSupcnt(self):
        '''
        return supcnt of Node
        '''
        return self.__supcnt
    def getSelf(self):
        '''
        return Node itself
        '''
        return self
    #------------Setter---------------
    def setSibling(self):
        raise NotImplementedError
    def addItem(self, item):
        '''
        Insert an Item(set) to Node and add supcnt by one \n
        if item already exist then just add supcnt by one \n
        Parameter : item(set) \n
        Return : none \n
        '''
        if type(item) is not set:
            raise ValueError('addItem() just receive set type as parameter')
        if self.__item == item:
            self.__supcnt = self.__supcnt + 1
        else:
            self.__item = item
            self.__supcnt = self.__supcnt + 1
    def addChild(self, child):
        '''
        Add a child to Node \n
        Parameter : child(Node obj.)
        Return : none
        '''
        if type(child) is not Node:
            raise ValueError('addChild() just receive Node object as parameter')
        self.__child.append(child)
    def addParent(self, parent):
        '''
        Add a parent to Node
        Parameter : parent(Node obj)
        Return : none
        '''
        if type(parent) is not Node:
            raise ValueError('addParent() just receive Node object as parameter')
        self.__parent = parent
    
    def addSupCount(self, value):
        '''
        Add supcnt by value \n
        Parameter: \n
            value(int)
        '''
        self.__supcnt = self.__supcnt + value
if __name__ == '__main__':
    try:
        # test functionality
        node = Node({1}, 5)
        print(node.getItem())
        print(node.getSupcnt())
        parent_node = Node({2}, 3)
        parent_node.addChild(node)
        print(parent_node.getItem())
        print(parent_node.getSupcnt())
        print(node)
        print(parent_node.getChilds()[0])
        node.addParent(parent_node)
        print(node.getParent())
        print(parent_node)
        print(node.getSelf())
    except ValueError as e:
        print(str(e))
