import argparse
import os
import sys

import numpy as np

from Graph import NetworkGraph

CWD = os.getcwd()
#================ Set DATA_PATH ==============
DATA_PATH = ''
if 'Assignment3' not in CWD:
    DATA_PATH = os.path.join(CWD, 'Assignment3', 'project3dataset')
else:
    DATA_PATH = os.path.join(CWD, 'project3dataset')

if __name__ == "__main__":
    pass
