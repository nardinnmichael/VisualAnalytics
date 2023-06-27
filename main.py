from PyQt5.QtWidgets import QApplication

import parser
import view_old
from plotting import *
from algos import *
import networkx as nx

# Press the green button in the gutter to run the script.
# TODO: install all requirements using pip install -r requirements.txt
if __name__ == '__main__':
    print(
        f"current number of threads is {nk.getCurrentNumberOfThreads()}, lets increase this to {(nk.getMaxNumberOfThreads() / 2) + 1}")
    nk.setNumberOfThreads((nk.getMaxNumberOfThreads() / 2) + 1)  # set the maximum number of available threads
    # df = parser.parse_tweets_as_df("train.json")  # this file is too large for git. I'll send it to you using bigmail - Florian
    df = parser.parse_tweets_as_df("test.json")


    # Parsing graph from the dataframe:
    G, G_x, att = parser.get_graph(df)
    G_undirected, att = parser.get_graph(df, directed=False)


    # Tryout-zone of algos: --------------------------------------------------------------
    plot_degree_centrality(G)
    plot_communities_info(G_undirected)
    #basic_network_plot(G)
    # this does not work because we have loops in our graph:
    plot_k_core_decomposition(G, att)

    # this creates a full profile of the network like shown here https://networkit.github.io/dev-docs/notebooks/User-Guide.html#NetworkX-Compatibility
    # the .show() function only works in a jupyter notebook, but the data is there, and we can use it
    # profile = nk.profiling.Profile.create(G)

    # ------------------------------------------------------------------------------------

    # Starting the GUI
    app = QApplication(sys.argv)
    window = view_old.MainWindow(G=G, G_x=G_x, G_undirected=G_undirected)
    window.show()
    app.exec_()





    print("End of file.")
