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
            self.graph[int(n1)-1][int(n2)-1] = 1
    
    def PageRank(self, d: float = 0.15, criteria: float = 0.1):
        """
        Implement PageRank with Power Method

        Args:
        --------
            d(float) : dampling factor, default=0.15
            criteria(float) : under what circumstances do iteration stop, '0.1' means norm of x_new and x_old < 0.1
        """
        A = self.graph.T
        norm_vec = np.linalg.norm(A, ord=1, axis=0)
        A = np.nan_to_num(A / norm_vec)
        S = np.ones(shape=(A.shape[0], A.shape[0]))
        S = S / S.shape[0]
        M = ( 1 - d ) * A + d * S
        x_old = np.random.rand( A.shape[0] )
        x_old = x_old / np.linalg.norm(x_old, ord=1)
        x_new = np.zeros( A.shape[0] )
        # Start power iteration
        count = 0
        while np.linalg.norm(x_new - x_old) > criteria:
            count += 1
            temp = np.copy(x_new)
            x_new = M @ x_old
            x_old = temp
        
        print(f'Criteria:{criteria}')
        print(f'Num of iteration:{count}')
        return x_new


    def HITS(self):
        raise NotImplementedError

    def SimRank(self):
        raise NotImplementedError

if __name__ == "__main__":
    test_dir = 'Assignment3/project3dataset/hw3dataset/graph_1.txt'
    mygraph = NetworkGraph()
    mygraph.load_from_file(test_dir)
    print(mygraph.PageRank())
