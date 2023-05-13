# the GUI using pyqt
import main

import sys
import matplotlib.pyplot as plt
import networkx as nx
import networkit as nk
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel, QCheckBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from pyvis.network import Network
from PyQt5.QtGui import QFont
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel, QCheckBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from pyvis.network import Network
import sys
import os
import plotting


class MainWindow(QMainWindow):
    def __init__(self, *args, G, G_x, G_undirected, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Twitter Data Analysis")
        # Our custom font that we will use for all titles
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # tryout of pyvis, this should be in a function if it works
        # this just creates a random graph
        # Create a graph with NetworkX
        nx_G = nx.erdos_renyi_graph(30, 0.2)
        # Convert the NetworkX graph to a Pyvis network
        pyvis_net = Network(notebook=True)
        pyvis_net.from_nx(nx_G)
        # Save the Pyvis network as an HTML file
        pyvis_net.show("graph.html")

        # Create the tab widget
        self.tabs = QTabWidget()

        # Create the tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        # Add the tabs to the tab widget
        self.tabs.addTab(self.tab1, "Communities")
        self.tabs.addTab(self.tab2, "K-Core")
        self.tabs.addTab(self.tab3, "Influencers")
        self.tabs.addTab(self.tab4, "Retweet")
        self.tabs.addTab(self.tab5, "Centrality")

        # TODO: we need to have the graph of communities and how they are connected here
        # For the first tab, we create a QWebEngineView, load the graph, and add it to the tab
        self.view1 = QWebEngineView()
        # self.setGeometry(0, 0, 800, 600) # you can use this to position and size the graph
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.view1.load(local_url)

        # TODO: we need to calculate the k-core decomposition here (maybe also apply it to tab1?)
        # For the second tab, we create a QWebEngineView, load the graph, and add it to the tab
        self.view2 = QWebEngineView()
        # self.setGeometry(0, 0, 800, 600) # you can use this to position and size the graph
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.view2.load(local_url)


        # For each tab, we can set layout and add widgets
        self.tab1.layout = QVBoxLayout()
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.layout.addWidget(QLabel("Content for first tab"))
        self.tab1.layout.addWidget(QCheckBox("Display Bots"))
        self.tab1.layout.addWidget(QCheckBox("Display Humans"))
        self.tab1.layout.addWidget(self.view1)
        # Plotting the communities using matplotlib
        fig = plotting.plot_communities_info(G_undirected)
        canvas = FigureCanvas(fig)
        self.tab1.layout.addWidget(canvas)

        self.tab2.layout = QVBoxLayout()
        self.tab2.setLayout(self.tab2.layout)
        self.tab2.layout.addWidget(QLabel("Content for second tab"))
        self.tab2.layout.addWidget(QCheckBox("Display Bots"))
        self.tab2.layout.addWidget(QCheckBox("Display Humans"))
        self.tab2.layout.addWidget(self.view2)

        self.tab3.layout = QVBoxLayout()
        self.tab3.setLayout(self.tab3.layout)
        self.tab3.layout.addWidget(QLabel("Content for third tab"))
        self.tab3.layout.addWidget(QCheckBox("Display Bots"))
        self.tab3.layout.addWidget(QCheckBox("Display Humans"))

        self.tab4.layout = QVBoxLayout()
        self.tab4.setLayout(self.tab4.layout)
        title_label = QLabel("Retweets")
        title_label.setFont(font)
        self.tab4.layout.addWidget(title_label)

        self.tab5.layout = QVBoxLayout()
        self.tab5.setLayout(self.tab5.layout)
        title_label = QLabel("Degree of Centrality")
        title_label.setFont(font)
        self.tab5.layout.addWidget(title_label)
        fig = plotting.plot_degree_centrality(G)
        canvas = FigureCanvas(fig)
        self.tab5.layout.addWidget(canvas)

        # Set the tab widget as the central widget of the window
        self.setCentralWidget(self.tabs)

    def update_graph(self, index):
        if index == 0:
            self.view.reload()
        print(f"Tab Nr {index} was opened. We could update it here")  # this message is not displayed in the console :/
