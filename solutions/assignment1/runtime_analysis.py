"""
Authors:
Alena Zorich (elzorich@uni-koblenz.de)
Igor Maksimovich Fedotov (ifedotov@uni-koblenz.de)
Mariya Chkalova (mchkalova@uni-koblenz.de)
Arsenii Smyrnov (smyrnov@uni-koblenz.de)
"""

import time
import os
import numpy as np
import matplotlib.pyplot as plt

from naive_search import *

def analyze(keyword):
    results = []
    for x in range (1, 11):
        filename = 'simplewiki-20160501-extracted-' + str(x) + '.xml'
        print('file: ',filename)
        startTime = time.time()
        matches = naive_search(filename, keyword)
        endTime = time.time()
        statinfo = os.stat(filename)
        processTime = endTime - startTime
        sizeMiB = statinfo.st_size / 1048576
        print('processTime: ', processTime)
        print('sizeMiB: ', sizeMiB)
        results.append((sizeMiB, processTime))
    return results

def visualize(results):
    """results = [(12.956766128540039, 2.4282357692718506), (22.98198890686035, 4.528490781784058), (31.99721050262451, 5.9590981006622314), (40.01898384094238, 7.73870325088501), (46.82229995727539, 9.955496549606323), (51.050435066223145, 11.15609335899353), (58.71097946166992, 13.102061986923218), (67.6065902709961, 15.149430513381958), (76.34563541412354, 16.6189067363739), (83.06983470916748, 21.519630670547485)]"""
    plt.plot(*zip(*results))
    plt.title('Elapsed time per filesize')
    plt.xlabel('Filesize, MiB')
    plt.ylabel('Time, sec')
    plt.show()


if __name__ == '__main__':
    keyword = input("keyword: ")

    results = analyze(keyword)
    visualize(results)