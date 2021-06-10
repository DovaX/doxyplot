import numpy as np
import matplotlib.pyplot as plt
import math
from operator import itemgetter


def prepare_xy_data_from_file(filename, columns=2):
    """Prepares two lists based on data in txt file"""
    with open(filename) as f:
        lines = f.readlines()
        # print(lines)
        x = [line.split()[0] for line in lines]
        try:
            y = [line.split()[1] for line in lines]
        except:
            y = [line.replace("\n", "") for line in lines]
            y = [line.split(" ")[1] for line in lines]
        if columns == 3:
            y2 = [line.split()[2] for line in lines]
    for i in range(len(x)):
        x[i] = float(x[i])

    for i in range(len(y)):
        try:
            y[i] = float(y[i])
        except:
            print(y[i])
    if columns == 3:
        for i in range(len(y2)):
            y2[i] = float(y2[i])
        return (x, y, y2)
    return (x, y)


def sort_depth_value(x, y):
    """Sorts values according to the depth, x ... value, y ... depth"""
    assert len(x) == len(y)
    list1 = [[x[i], y[i]] for i in range(len(x))]

    list1 = sorted(list1, key=itemgetter(0))
    x = [item[0] for item in list1]
    y = [item[1] for item in list1]

    return (x, y)


class Doxyplot:
    """Class for automated plotting of xy-scatter data"""
    def __init__(self):
        self.x_list = []
        self.y_list = []
        self.c_list = []
        self.label_list = []
        self.linewidth = []
        pass

    def load_data(self, filepath, sort=False):
        x, y = prepare_xy_data_from_file(filepath)
        if sort:
            x, y = sort_depth_value(x, y)
        return (x, y)

    def append_data(self, x, y, c, label, linewidth=2.0):
        self.x_list.append(x)
        self.y_list.append(y)
        self.c_list.append(c)
        self.label_list.append(label)
        self.linewidth.append(linewidth)

    def construct_plot(
        self,
        title,
        xlabel,
        ylabel,
        save=False,
        xymin=False,
        xymax=False,
        figsize=(7, 5),
    ):
        fig = plt.figure(figsize=figsize)
        ax1 = fig.add_subplot(111)
        ax1.set_title(title)
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)
        for i in range(len(self.x_list)):
            ax1.plot(
                self.x_list[i],
                self.y_list[i],
                c=self.c_list[i],
                label=self.label_list[i],
                linewidth=self.linewidth[i],
            )

        # ax1.plot(y,x, c='r', label='Mean T depth profile, Viscoplasticity - case 1', linewidth=1.0)
        leg = ax1.legend()
        if xymin:
            ax1.set_xlim(xmin=xymin[0])
            ax1.set_ylim(ymin=xymin[1])
        if xymax:
            ax1.set_xlim(xmax=xymax[0])
            ax1.set_ylim(ymax=xymax[1])
        if save:
            fig.savefig(save, format="png",
                        dpi=200, bbox_inches="tight")
        return (ax1, fig)


def logarithmic(x):
    """recalculates whole list of values to decadic logarithm - used in plots"""
    for i in range(len(x)):
        if x[i] <= 0:
            x[i] = 1e-10
        x[i] = math.log10(x[i])
    return x
