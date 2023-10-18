import matplotlib.pyplot as plt
import pandas as pd
import os

OUT_DIR = "./imgs/meas/"

def main():
    v1 = [1, 1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5]
    v2 = [0,0.5,1,1.5,2,2.5,3,3.5]

    i1   = [0,0,0,0.002,0.042,0.771,56.5,62.1,68.3,74.9,80.8]
    i2_1 = [0,5.6,9.94,15,20.2,25.8,31.4,37.3]
    i2_2 = [0.2,31,20,24.3,29.8,35.1,41.5,48]
    i2_3 = [0.29,105,100,42.6,44.5,48.6,54.3,60.2]
    
    vds50 = pd.DataFrame(i1, v1)
    vgs25 = pd.DataFrame(i2_1, v2)
    vgs30 = pd.DataFrame(i2_2, v2)
    vgs35 = pd.DataFrame(i2_3, v2)

    plot1(vds50)
    plot2(vgs25, vgs30, vgs35)

def plot1(df):
    f = plt.figure()
    plt.plot(df, '.')
    plt.title("Sweeping V$_{ds}$")
    f.savefig(os.path.join(OUT_DIR, "sweepvds.png"))

def plot2(*dfs):
    f = plt.figure()
    colors = ['xkcd:ocean', 'xkcd:crimson', 'xkcd:light forest green']
    i = 0
    for df in dfs:
        plt.plot(df, '.', color=colors[i % len(colors)])
        plt.plot(df, linewidth=0.2, color=colors[i % len(colors)])
        i += 1
    plt.xlabel("This is a new x label")

    f.savefig(os.path.join(OUT_DIR, "sweepvgs.png"))



if __name__ == '__main__':
    main()