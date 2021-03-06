import argparse
import cProfile
import os
import sys

import numpy as np

from Graph import NetworkGraph

CWD = os.getcwd()
#================ Set DATA_PATH ==============
DATA_PATH = ''
if 'Assignment3' not in CWD:
    DATA_PATH = os.path.join(CWD, 'Assignment3', 'project3dataset', 'hw3dataset')
else:
    DATA_PATH = os.path.join(CWD, 'project3dataset', 'hw3dataset')

if __name__ == "__main__":
    # ========== Data Path init ====================
    G1_path = os.path.join(DATA_PATH, 'graph_1.txt')
    G2_path = os.path.join(DATA_PATH, 'graph_2.txt')
    G3_path = os.path.join(DATA_PATH, 'graph_3.txt')
    G4_path = os.path.join(DATA_PATH, 'graph_4.txt')
    G5_path = os.path.join(DATA_PATH, 'graph_5.txt')
    G6_path = os.path.join(DATA_PATH, 'graph_6.txt')
    G7_path = os.path.join(DATA_PATH, 'output.data')
    # ========== Argument Parser Setting ===========
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--profile', help='run profiling mode', action='store_true')
    args = parser.parse_args()
    # ========== Interactive UI ====================
    mygraph = NetworkGraph()
    np.set_printoptions(threshold=sys.maxsize)
    while True:
        gnum = input("Enter graph number(1~7) to choose graph, insert '-1' to exit program :\n")
        if gnum == '1':
            mygraph.load_from_file(G1_path)
        elif gnum == '2':
            mygraph.load_from_file(G2_path)
        elif gnum == '3':
            mygraph.load_from_file(G3_path)
        elif gnum == '4':
            mygraph.load_from_file(G4_path)
        elif gnum == '5':
            mygraph.load_from_file(G5_path)
        elif gnum == '6':
            mygraph.load_from_file(G6_path)
        elif gnum == '7':
            mygraph.load_from_IBM(G7_path)
        elif gnum == '-1':
            print('Bye Bye')
            break
        else:
            raise ValueError('Unknown graph!')
        # ============== Run PageRank HITS SimRank =================
        PRvector = mygraph.PageRank()
        print('=======================================')
        print(f'PageRank:\n{PRvector}')

        AUTH, HUB = mygraph.HITS()
        print('=======================================')
        print(f'Authority:\n{AUTH}')
        print(f'Hub:\n{HUB}')

        SRmatrix = mygraph.SimRank()
        print('=======================================')
        print(f'SimRank:\n{SRmatrix}')
        # ============= Run Profiling if neccessary ================
        if args.profile:
            print('=======================================')
            print('Now Run Profiling on PageRank')
            input('Press any key to start')
            cProfile.run('mygraph.PageRank()')
            print('=======================================')
            print('Now Run Profiling on HITS')
            input('Press any key to start')
            cProfile.run('mygraph.HITS()')
            print('=======================================')
            print('Now Run Profiling on SimRank')
            input('Press any key to start')
            cProfile.run('mygraph.SimRank()')
        # ============== Increase PageRank, Authority and Hub ======
        if gnum == '1':
            print('=======================================')
            print('Add extra edge to node 1 in Grpah 1')
            print('Add new edges form node 6, 5, ...,2 to node 1 ')
            print('Add new edges form node 1 to node 6, 5, ...,2')
            for i in range(2,7):
                mygraph.insert_edge( v1 = i, v2 = 1)
                mygraph.insert_edge( v1 = 1, v2 = i )
            print('Now get new PageRank HITS')
            PRvector = mygraph.PageRank()
            print(f'PageRank:\n{PRvector}')
            AUTH, HUB = mygraph.HITS()
            print(f'Authority:\n{AUTH}')
            print(f'Hub:\n{HUB}')
        elif gnum == '2':
            print('=======================================')
            print('Add extra edge to node 1 in Grpah 1')
            print('Add a bi-direct edge from node 1 to node 3')
            mygraph.insert_edge( v1 = 1, v2 = 3 )
            mygraph.insert_edge( v1 = 3, v2 = 1 )
            print('Now get new PageRank HITS')
            PRvector = mygraph.PageRank()
            print(f'PageRank:\n{PRvector}')
            AUTH, HUB = mygraph.HITS()
            print(f'Authority:\n{AUTH}')
            print(f'Hub:\n{HUB}')
        elif gnum == '3':
            print('=======================================')
            print('Add extra edge to node 1 in Grpah 1')
            print('Add a bi-direct edge from node 1 to node 4')
            mygraph.insert_edge( v1 = 1, v2 = 4 )
            mygraph.insert_edge( v1 = 4, v2 = 1 )
            print('Now get new PageRank HITS')
            PRvector = mygraph.PageRank()
            print(f'PageRank:\n{PRvector}')
            AUTH, HUB = mygraph.HITS()
            print(f'Authority:\n{AUTH}')
            print(f'Hub:\n{HUB}')
        print('=======================================')