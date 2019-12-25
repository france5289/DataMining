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
    
    def PageRank(self, d: float = 0.15, criteria: float = 0.01):
        """
        Implement PageRank with Power Method

        Args:
        --------
            d(float) : dampling factor, default=0.15
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
                print(f'Criteria:{criteria}')
                print(f'Num of iteration:{count}')
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

        # Find authority
        count = 0
        while True:
            count += 1
            prev = np.copy(a)
            a = Au @ a
            a = a / np.linalg.norm(a, ord=1)
            if np.linalg.norm( a - prev ) <= criteria:
                print(f'Iterations of authority finding:{count}')
                break
        # Find Hub
        count = 0
        while True:
            count += 1
            prev = np.copy(h)
            h = Hu @ h
            h = h / np.linalg.norm(h, ord=1)
            if np.linalg.norm( h - prev ) <= criteria:
                print(f'Iterations of hub finding:{count}')
                break
        return a, h


    def SimRank(self):
        raise NotImplementedError

if __name__ == "__main__":
    test_dir = 'Assignment3/project3dataset/hw3dataset/graph_6.txt'
    mygraph = NetworkGraph()
    mygraph.load_from_file(test_dir)
    print(f'PageRank:{mygraph.PageRank()}')
    authority, hub = mygraph.HITS(criteria=0.1)
    print(f'Authority:{authority}')
    print(f'Hub:{hub}')
