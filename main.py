import multiprocessing
from multiprocessing import Pool

import random
import time
import os

from def_common import *

def func(x):
    if (x['cmd_type']=='shell'):
        delay = random.randint(1, 9)/10
        time.sleep(delay)
        
        cmd = ' '.join(x['cmd_opt'])
        # print(cmd)
        os.system(f'{cmd} , delay = {delay}')
    elif (x[0]=='script'):
        pass
    elif (x[0]=='python'):
        pass
    else:
        print('Error :: command type not found !')

if __name__== '__main__':
    files_to_include = ['sim.py']
    for file in files_to_include:
        with open(file) as f:
            code = f.read()
            exec(code)

    # print(list_run)
    # for i in list_run:
    #     print(i['cmd_opt'][1:])

    # 1. for loop
    for item in list_run:
        func(item)

    # 2. seq from loop
    seq = [func(item) for item in list_run]

    # 3. multi process
    print("Number of CPU :", multiprocessing.cpu_count())
    with Pool(4) as p:
        seq = p.map(func, [item for item in list_run])