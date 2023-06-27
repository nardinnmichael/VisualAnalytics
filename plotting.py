
# This file is intended for the GUI and / or the visualizion functions of the graphs
import networkit as nk
from networkit import *
import matplotlib.pyplot as plt
import time
import numpy
import pandas as pd
import networkx as nx
from pyvis.network import Network
import textwrap
import math
import parser

# plots a matplotlib graph of the centrality degree of the network G and saves it as png
def plot_degree_centrality(G):
    dd = sorted(nk.centrality.DegreeCentrality(G).run().scores(), reverse=True)
    degrees, numberOfNodes = numpy.unique(dd, return_counts=True)
    fig, ax = plt.subplots()
    plt.xscale("log")
    plt.xlabel("degree")
    plt.yscale("log")
    plt.ylabel("number of nodes")
    plt.plot(degrees, numberOfNodes)
    plt.savefig('./images/centrality.png')
    #plt.show()
    return fig


# creates a .html file of the k-core decomposition of a graph, k_count is the core count
def plot_k_core_decomposition(G_x, attributes, k_count=2):
    os.makedirs('k_cores', exist_ok=True)

    print("Starting k-core")
    k = nx.k_core(G_x, k=k_count)

    nt = Network('600px', '1400px', notebook=True, cdn_resources="remote",
                 bgcolor= "white", font_color="black")
    nt.show_buttons(filter_=['physics'])
    nt.from_nx(k)

    # Assigning colors to each node based on values in label column of original data
    att = attributes["node_to_att"]
    sizes = [math.log10(x) if x > 0 else 0 for x in attributes["node_to_size"]]
    # sizes = [math.sqrt(x) for x in attributes["node_to_size"]]
    print(f"size go from {sizes[0]} to {sizes[-2]}")

    for node in nt.nodes:
        node['color'] = att[node['id']][0]
        node['shape'] = att[node['id']][1]
        node['size'] = 1 + 10 * sizes[node['id']]

    nt.show_buttons()
    nt.show(f"k_cores/{k_count}_core_graph.html")

    print("Showing the plot for {}".format(k))
    #plt.show()


# already used in the view_old.py in tab1. Works as intended.
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
    plt.savefig('./images/Communities.png')
    # plt.show()
    return fig


def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0)


def formatter(x, pos):
    return str(round(x / 1e6, 1)) + " M"


# finds the top n accounts in terms of follower count and creates a matplotlib bar chart
def get_Top_Accounts(n, type):
    influencers = parser.get_Top_N_Accounts(n, type)
    influencers.plot(kind='bar', edgecolor='black', rot=0)
    ax = influencers.plot.bar(x='profile.name', y='profile.followers_count', rot=0, legend=False,
                              color=['royalblue', 'darkorange','green', 'red','black'],xlabel='')
    ax.yaxis.set_major_formatter(formatter)

    wrap_labels(ax, 15)
    plt.savefig('./images/Influencers.png')
    plt.clf()
    #plt.show()

# plots two matplotlib pie chart of 1. the ratio of users and bots and 2. the percentage of human / bot statuses
def plot_User_Type_Ratio():
    # plot Percentage of Humans and Bots Users
    df = pd.read_pickle("df.pkl")
    labels = ['Bots', 'Humans']
    df.groupby(['label']).count().plot(kind='pie', y='ID', autopct='%1.0f%%',
                                    colors=['royalblue', 'darkorange'],
                                    title='Percentage of Humans and Bots Users', labels=labels,xlabel='', ylabel='',legend=False)
    plt.savefig('./images/countPerUserType.png')
    plt.clf()

    # plot Percentage of Humans and Bots Statuses
    df.groupby(['label']).sum(numeric_only=True).plot(kind='pie', y='profile.statuses_count', autopct='%1.0f%%',
                                    colors=['royalblue', 'darkorange'],
                                    title='Percentage of Humans and Bots Statuses',
                                    labels=labels,xlabel='', ylabel='',legend=False)
    plt.savefig('./images/statusesCount.png')
    plt.clf()
