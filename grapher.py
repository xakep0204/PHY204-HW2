import sys
import subprocess
import numpy as np
from time import monotonic
from matplotlib import pyplot as plt


if __name__ == '__main__':
    argv = sys.argv[1:][0]
    cmd = f"./solver {argv}"
    # cmd = f"./solver {argv} > data.csv"
    start_time = monotonic()
    data_txt = subprocess.check_output(cmd, shell=True).decode("utf-8").strip().split("\n;")
    t = data_txt[1]
    data_txt = data_txt[0]
    data_csv = []
    for row in data_txt.split('\n'):
      data_csv.append([float(x) for x in row.split(',')])
    V = np.array(data_csv)
    # V = np.genfromtxt('data.csv', delimiter=",", usemask=True)

    plt.imshow(V, cmap='viridis')
    plt.colorbar()
    print(f"Python {(monotonic() - start_time)*1000:.3f} ms; C++ {t} ms")
    # plt.title(f"$V(x,y)$ for $N={argv}$")
    # plt.xlabel("$x$")
    # plt.ylabel("$y$")
    # # # save as pdf
    # # plt.savefig(f"V_{argv}.pdf")
    # # #display the plot
    # # plt.show()