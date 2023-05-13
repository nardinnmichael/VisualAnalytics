import networkit as nk
from networkit import *
import matplotlib.pyplot as plt
import time
import numpy

def calc_ranked_centrality(G):
    start = time.time()
    bc = nk.centrality.Betweenness(G)
    bc.run()
    print(f"The 10 nodes with the highest centrality are {bc.ranking()[:10]}")
    end = time.time()
    print(f"Done calculating centrality. This calculation took {end - start:.2f} seconds.")
    return bc.ranking()

# TODO: fix this
# see  plot_k_core_decomposition(G, kcore) in plotting.py
# does not finish, maybe stuck in a loop
def calc_k_core_decomposition(G, cores):
    # coreDec = nk.centrality.CoreDecomposition(K)
    # coreDec.run()
    nk.coreDec = nk.centrality.CoreDecomposition(G)
    nk.coreDec.run()
    C = nk.graph.Subgraph().fromNodes(G, cores)
    pass

# TODO: figure out how to plot the network. Maybe using pyvis. Without k-core decomposition the graph will likely be too large
def basic_network_plot(G):
    print(f"Plotting graph")
    start = time.time()
    # coreDec = nk.centrality.CoreDecomposition(K)
    # coreDec.run()
    # set(coreDec.scores())
    # communities = community.detectCommunities(G)
    print("1")
    # nk.viztasks.drawGraph(K, node_size=[(k ** 2) * 20 for k in coreDec.scores()])
    # plt.show()
    # print("3")
    # the 10 most central nodes
    print("2")

    # nk.community.detectCommunities(G)


    end = time.time()
    print(f"Done plotting. The graph took {end - start:.2f} seconds to draw.")

    # pf = profiling.Profile.create(G,  preset="minimal")


