import networkit as nk
from networkit import *
import networkx as nx
import matplotlib.pyplot as plt
import time
from pyvis.network import Network
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
    # convert from NetworKit.Graph to networkx.Graph
    nxG = nk.nxadapter.nk2nx(G)
    print(f"Plotting graph")
    start = time.time()
    coreDec = nk.centrality.CoreDecomposition(G)
    coreDec.run()
    set(coreDec.scores())
    #communities = community.detectCommunities(G)
    # Plotting full graph if needed using networkx
    # nx.draw_networkx(nxG, node_size=[(k ** 2) * 20 for k in coreDec.scores()], with_labels=True)
    # plt.show()
    print("1")
    # plotting full interactive graph
    pyvis_net = Network(notebook=True, cdn_resources='remote')
    pyvis_net.from_nx(nxG)
    # Save the Pyvis network as an HTML file
    pyvis_net.show("full_graph.html")
    print("3")
    # the 10 most central nodes
    print("2")
    end = time.time()
    print(f"Done plotting. The graph took {end - start:.2f} seconds to draw.")

    pf = profiling.Profile.create(G,  preset="minimal")


