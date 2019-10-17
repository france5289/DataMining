class Node():
    def __init__(self, item=set(),supcnt=0,parent=None, child=list()):
        '''
        constructor for Node object
        it can receive item(set), supcnt(support count)(int), parent(Node obj) and child(List of Node obj)
        if item is parent is None then it implies this node is root node
        if every attribute in Node is empty it implies this node is NULL node
        '''
        if type(item) is not set:
            raise ValueError('Node __init()__ item paramter just receive set type')
        if type(supcnt) is not int:
            raise ValueError('Node __init()__ supcnt paramter just receive integer type')
        if type(child) is not list:
            raise ValueError('Node __init()__ child paramter just receive list type')
        self.__item = item
        self.__supcnt = supcnt
        self.__parent = parent
        self.__child = child

    #------------Getter---------------
    def getItem(self):
        '''
        return memeber variable of Node obj : '__item'
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
    def setItem(self, item):
        '''
        Insert an Item(set) to Node
        if Node already have Item value, it will be replaced
        Parameter : item(set)
        Return : none
        '''
        if type(item) is not set:
            raise ValueError('setItem() just receive set type as parameter')
        self.__item = item
    def addChild(self, child):
        '''
        Add a child to Node
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
    except ValueError as e:
        print(str(e))
