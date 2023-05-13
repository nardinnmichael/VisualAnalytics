# This file is intended for the GUI and / or the visualizion functions of the graphs
import networkit as nk
from networkit import *
import matplotlib.pyplot as plt
import time
import numpy

# already used in the view.py in tab5. Works as intended.
def plot_degree_centrality(G):
    dd = sorted(nk.centrality.DegreeCentrality(G).run().scores(), reverse=True)
    degrees, numberOfNodes = numpy.unique(dd, return_counts=True)
    fig, ax = plt.subplots()
    plt.xscale("log")
    plt.xlabel("degree")
    plt.yscale("log")
    plt.ylabel("number of nodes")
    plt.plot(degrees, numberOfNodes)
    # plt.show()
    return fig

# TODO: fix this. Implement in algos.py and call here or put everything here
# this does not finish at my machine. Maybe the loops that are in the graph are a problem, not sure
def plot_k_core_decomposition(G, kcore):
    print("Starting k-core")
    coreDec = nk.centrality.CoreDecomposition(G)
    print("Running coreDec")
    coreDec.run()
    print("Setting scores")
    set(coreDec.scores())
    print(f"Plotting graph for {coreDec.scores()}")
    nk.viztasks.drawGraph(G, node_size=[(k ** 2) * 20 for k in coreDec.scores()])
    print("Showing the plot")
    plt.show()


# already used in the view.py in tab1. Works as intended.
# plots a plot with two subplots
def plot_communities_info(G):
    communities = nk.community.detectCommunities(G, algo=nk.community.PLM(G, True))
    sizes = communities.subsetSizes()
    sizes.sort(reverse=True)
    fig, ax = plt.subplots()
    ax1 = plt.subplot(2, 1, 1)
    ax1.set_ylabel("size")
    ax1.set_title("Community Sizes in Total Numbers")
    ax1.plot(sizes)

    ax2 = plt.subplot(2, 1, 2)
    ax2.set_title("Community Sizes on a Log-Scale")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_ylabel("size")
    ax2.plot(sizes)
    plt.subplots_adjust(hspace=0.5)
    # plt.show()
    return fig

