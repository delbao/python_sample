import multiprocessing
import requests
from time import time
import random
import os

queries = ['some', 'sample', 'data']
url = 'http://www.google.com/search'

def apply_load(iterations):
    try:
        print "start {}".format(multiprocessing.current_process().name)
        s = time()
        success = 0
        error = 0
        for i in range(iterations):
            try:
                r = requests.get(url, params={'as_q': random.choice(queries)})
                r.raise_for_status()
                success += 1
            except:
                error += 1
      
        rate = (iterations / (time() - s))
    
        print 'Iterations %s/s' % rate
        return rate
    # only after python 3.4 supports multiprocessing.pool.RemoteTraceback
    except Exception:
        print("Exception in worker:")
	traceback.print_exc()
        raise

jobs = multiprocessing.cpu_count()
pool = multiprocessing.Pool(jobs)

if __name__ == '__main__':

    size = 50 / jobs
    inputs = [size for i in range(jobs)]

    rates = pool.map(apply_load, inputs)
    total = reduce(lambda a, b: a+b, rates)

    runningProcesses = os.popen('ps | grep multiprocess').readlines()
    nproc = len(runningProcesses)
    print 'Total: %s/s, there were %i Python processes running!' % (total, nproc)
