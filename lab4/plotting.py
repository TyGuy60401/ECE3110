import matplotlib.pyplot as plt
import pandas as pd
import os

OUT_DIR = "./imgs/meas/"
COLORS = ['xkcd:ocean', 'xkcd:crimson', 'xkcd:light forest green']

class Plot():
    def __init__(self, **kwargs):
        self.plot_data = {
            'title': "Title",
            'xlabel': "X Label",
            'ylabel': "Y Label",
            'filename': 'img.png',
            'graphs': None
        }
        for key in self.plot_data.keys():
            try:
                self.plot_data[key] = kwargs[key]
            except KeyError:
                continue
        
        self.f = plt.figure()

    def makeplot(self):
        i = 0
        for graph in self.plot_data['graphs']:
            plt.plot(graph['df'], '.', color=COLORS[i % len(COLORS)])
            plt.plot(graph['df'], linewidth=0.5, color=COLORS[i % len(COLORS)], label=graph['label'])
            i += 1
        plt.legend()
        plt.title(self.plot_data['title'])
        plt.xlabel(self.plot_data['xlabel'])
        plt.ylabel(self.plot_data['ylabel'])
        self.f.savefig(os.path.join(OUT_DIR, self.plot_data['filename']))
    
    


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

    p1_data = {
        'graphs': [
            {
            'label': "V$_{ds}=5$ V",
            'df': vds50
        },
        ],
        'title': "Sweeping V$_{gs}$",
        'xlabel': "V$_{gs}$ [V]",
        'ylabel': "I$_D$ [A]",
        'filename': 'sweepvds.png'
    }
    p2_data = {
        'graphs': [
            {
            'label': "V$_{gs}=2.5$ V",
            'df': vgs25
        },
            {
            'label': "V$_{gs}=3.0$ V",
            'df': vgs30
        },
            {
            'label': "V$_{gs}=3.5$ V",
            'df': vgs35
        },
        ],
        'title': "Sweeping V$_{gs}$",
        'xlabel': "V$_{gs}$ [V]",
        'ylabel': "I$_D$ [A]",
        'filename': 'sweepvgs.png'
    }
    p1 = Plot(**p1_data)
    p1.makeplot()
    p2 = Plot(**p2_data)
    p2.makeplot()


if __name__ == '__main__':
    main()