import sys

import numpy as np

from IBMReader import DataReader


class NetworkGraph():
    def __init__(self):
        self.graph = None

    def insert_edge(self, v1, v2):
        """
        insert a directed edge form vertex 1 to vertex 2
        Raise ValueError when node not exist

        Args:
        -------------
            v1(int) : vertex number
            v2(int) : vertex number
        """
        if v1 < 1 or v1 > self.graph.shape[0]:
            raise ValueError('Invalid vertex!')
        if v2 < 1 or v2 > self.graph.shape[0]:
            raise ValueError('Invalid vertex!')
        if type(v1) is not int or type(v2) is not int:
            raise TypeError('Invalid vertex type')
        if self.graph[v1-1, v2-1] == 1:
            #print('Edge has already existed!')
            return
        self.graph[v1-1, v2-1] = 1

    def remove_edge(self, v1, v2):
        """
        Remove a directed edge from vertex 1 to vertex 2
        Raise ValueError when node not exist

        Args:
        ------------
            v1(int) : vertex number
            v2(int) : vertex number
        """
        if v1 < 1 or v1 > self.graph.shape[0]:
            raise ValueError('Invalid vertex!')
        if v2 < 1 or v2 > self.graph.shape[0]:
            raise ValueError('Invalid vertex!')
        if type(v1) is not int or type(v2) is not int:
            raise TypeError('Invalid vertex type')
        if self.graph[v1-1, v2-1] == 0:
            #print('Edge has not existed!')
            return
        self.graph[v1-1, v2-1] = 0
    
    def load_from_file(self,fileaname):
        """
        Load a graph from dataset, and set self.graph as a numpy adjacency matrix 

        Args:
        -------------
            filename(string)
        Example:
        -------------
        >>> graph = Graph.load_from_file('graph_1.txt')

        >>> print(graph)
        [[0, 0, 0],[1, 0, 0],[0, 1, 0]]
        """
        nodes = set()
        edges = []
        with open(fileaname, 'r') as f:
            lines = f.readlines()
        
        for link in lines:
            edge = link.strip('\n').split(',')
            for node in edge:
                nodes.add(node) 
            edges.append(tuple(edge)) # edges will be list of tuple
        # Create Adj. Matrix
        self.graph = np.zeros(shape=(len(nodes), len(nodes)))
        for edge in edges:
            n1, n2 = edge
            self.graph[int(n1)-1][int(n2)-1] = 1
    
    def load_from_IBM(self, filename):
        transactions = DataReader(filename)
        # ======= Count Nodes ===========
        nodes = set()
        for v in transactions.values():
            for node in v:
                nodes.add(int(node))
        self.graph = np.zeros(shape=(max(nodes), max(nodes)))
        # ======= Insert Edges ==========
        for v in transactions.values():
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    self.insert_edge( v1 = int( v[i] ), v2 = int( v[j] ))

    def PageRank(self, d: float = 0.15, criteria: float = 0.01):
        """
        Implement PageRank with Power Method

        Args:
        --------
            d(float) : damping factor, default=0.15
            criteria(float) : under what circumstances do iteration stop, '0.1' means norm of x_new and x_old leq 0.1
        Return:
        --------
            x(np.array) : 1-d vector, PageRank Value of every node
        """
        A = self.graph.T
        nodenum = A.shape[0]
        norm_vec = np.linalg.norm(A, ord=1, axis=0)
        A = np.nan_to_num(A / norm_vec)
        S = np.full((nodenum, nodenum), 1/nodenum )
        M = ( 1 - d ) * A + d * S
        x = np.random.rand( nodenum )
        x = x / np.linalg.norm(x, ord=1)
        # Start power iteration
        count = 0
        while True:
            count += 1
            prev = np.copy(x)
            x = M @ x
            if np.linalg.norm(x - prev) <= criteria:
                print(f'Damping Factor:{d}')
                print(f'Criteria of PageRank:{criteria}')
                print(f'Iterations of PageRank:{count}')
                return x


    def HITS(self, criteria: float = 0.01):
        """
        Implement HITS with Power Method

        Args:
        --------
            criteria(float) : criteria(float) : under what circumstances do iteration stop, '0.1' means norm of x_new and x_old leq 0.1
        Return:
        --------
            a(np.array) : 1-dim vector of authority
            h(np.array) : 1-dim vector of hub
        """
        A = self.graph
        A_T = A.T
        nodenum = A.shape[0]
        Au = A_T @ A
        Hu = A @ A_T
        a = np.ones(nodenum)
        h = np.ones(nodenum)
        #==============================================
        # Find authority
        print(f'Criteria of HITS: {criteria}')
        count = 0
        while True:
            count += 1
            prev = np.copy(a)
            a = Au @ a
            a = a / np.linalg.norm(a, ord=1)
            if np.linalg.norm( a - prev ) <= criteria:
                print(f'Iterations of Authority finding:{count}')
                break
        # Find Hub
        count = 0
        while True:
            count += 1
            prev = np.copy(h)
            h = Hu @ h
            h = h / np.linalg.norm(h, ord=1)
            if np.linalg.norm( h - prev ) <= criteria:
                print(f'Iterations of Hub finding:{count}')
                break
        return a, h


    def SimRank(self, c: float = 0.5, criteria: float = 0.01):
        """
        Implement SimRank with Matrix Representation

        Args:
        --------
            c(float) : decay factor
            criteria(float) : loop condition
        """
        if c >= 1 or c <= 0:
            raise ValueError('Error! Invalid Decay Factor of SimRank!')
        Q = self.graph.T
        nodenum = Q.shape[0]
        Q = np.nan_to_num( Q / np.linalg.norm(Q, ord=1, axis=0) )
        Q_T = Q.T
        S = np.identity( nodenum )
        I = np.identity( nodenum )
        # SimRank Matrix Representation
        count = 0
        while True:
            count += 1
            prev = np.copy(S)
            S = c * Q @ S @ Q_T
            S = S + I - np.diag( np.diag( S ) )
            if np.linalg.norm( S - prev ) <= criteria:
                print(f'Decay Factor:{c}')
                print(f'Criteria of SimRank:{criteria}')
                print(f'Iterations of SimRank:{count}')
                return S




if __name__ == "__main__":
    test_dir = 'Assignment3/project3dataset/hw3dataset/graph_1.txt'
    mygraph = NetworkGraph()
    mygraph.load_from_file(test_dir)
    print(f'PageRank\n:{mygraph.PageRank()}')
    authority, hub = mygraph.HITS()
    print(f'Authority:\n{authority}')
    print(f'Hub:\n{hub}')
    print('SimRank:\n')
    S = mygraph.SimRank( c = 0.6, criteria = 0.001 )
    np.set_printoptions(threshold=sys.maxsize)
    print(S)
