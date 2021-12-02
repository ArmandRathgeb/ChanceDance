from distutils.core import setup
import py2exe
from glob import glob
import os

import time, pygame 
from random import choice
import sys, pygame, time
from moves import Moves
from settings import Settings

data_files = []
for files in os.listdir('Images/'):
    f1 = 'Images/'+ files
    if os.path.isfile(f1):
        f2 = 'images', [f1]
        data_files.append(f2)

print(data_files)
#setup(data_files = [glob(r'Images\*.*')],windows=['main.py'])
setup(
    options = {'py2exe': 
        {
            'bundle_files': 1, 
            'compressed': True, 
            'unbuffered':True, 
       #     'optimize': 2
            }
        },
    data_files = data_files,
    windows=['main.py'],
    zipfile = None
    )