import numpy as np
from matplotlib import pyplot as plt

def barplot():
    data = np.array([['L=10', 0.006188],
                     ['L=20', 0.069171],
                        ['L=30', 0.288017],
                        ['L=40', 0.804825],
                        ['L=50', 1.745629],
                        ['L=60', 3.237971],
                        ['L=70', 5.912708],
                        ['L=80', 9.412025],
                        ['L=90', 13.608704],
                        ['L=100', 19.286371]])
    x = data[:,0]
    y = data[:,1].astype(np.float)
    plt.bar(x, y)
    plt.xlabel('L')
    plt.ylabel('Time (ms)')
    plt.title('Execution time of poissonEquation() in solver.cpp')
    plt.savefig('barplot.pdf')
    plt.show()

if __name__ == '__main__':
    barplot()
    