import abc

import numpy as np



class NetworkGraph():
    def __init__(self):
        self.graph = None

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
            self.graph[n1-1][n2-1] = 1
        return self
    
    def PageRank(self, d: float = 0.15):
        """
        Implement PageRank with Power Method

        Args:
        --------
            d(float) : dampling factor, default=0.15
        """
        A = self.graph.T
        norm_vec = np.linalg.norm(A, ord=1, axis=0)
        A = A / norm_vec
        S = np.ones(shape=(A.shape[0], A.shape[0]))
        S = S / S.shape[0]
        M = ( 1 - d ) * A + d * S
        x_old = np.random.rand( A.shape[0] )
        x_old = x_old / np.linalg.norm(x_old, ord=1)
        x_new = np.zeros( A.shape[0] )
        # Start power iteration
        while np.linalg.norm(x_new - x_old) > 0.01:
            temp = np.copy(x_new)
            x_new = M @ x_old 
            x_old = temp
            
        return x_new


    def HITS(self):
        raise NotImplementedError

    def SimRank(self):
        raise NotImplementedError

