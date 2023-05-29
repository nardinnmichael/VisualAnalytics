from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt5.QtWidgets import QLabel

class Ui_MainWindow_TwitterInsights(object):
    def setupUi(self, MainWindow_TwitterInsights):
        MainWindow_TwitterInsights.setObjectName("MainWindow_TwitterInsights")
        MainWindow_TwitterInsights.resize(1521, 831)
        MainWindow_TwitterInsights.setAcceptDrops(False)
        MainWindow_TwitterInsights.setWindowOpacity(1.0)
        MainWindow_TwitterInsights.setAutoFillBackground(False)
        MainWindow_TwitterInsights.setStyleSheet("background-color: #FFFFFF;")

        self.centralwidget = QtWidgets.QWidget(MainWindow_TwitterInsights)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.Qtab_Insights = QtWidgets.QTabWidget(self.centralwidget)
        self.Qtab_Insights.setGeometry(QtCore.QRect(0, 30, 1401, 721))
        self.Qtab_Insights.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Qtab_Insights.setAutoFillBackground(False)
        sshFile = "./style/style.css"
        with open(sshFile, "r") as fh:
         self.Qtab_Insights.setStyleSheet(fh.read())
        self.Qtab_Insights.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Qtab_Insights.setMovable(True)
        self.Qtab_Insights.setTabBarAutoHide(True)
        self.Qtab_Insights.setObjectName("Qtab_Insights")
        self.communities = QtWidgets.QWidget()
        self.communities.setObjectName("communities")
        self.CommunitiesShowBotsCheckBox = QtWidgets.QCheckBox(self.communities)
        self.CommunitiesShowBotsCheckBox.setGeometry(QtCore.QRect(70, 20, 111, 41))
        self.CommunitiesShowBotsCheckBox.setStyleSheet("")
        self.CommunitiesShowBotsCheckBox.setChecked(True)
        self.CommunitiesShowBotsCheckBox.setObjectName("CommunitiesShowBotsCheckBox")
        self.CommunitiesShowBotsCheckBox.stateChanged.connect(self.handleCommunitiesCheckboxes)


        self.CommunitiesShowHumansCheckBox = QtWidgets.QCheckBox(self.communities)
        self.CommunitiesShowHumansCheckBox.setGeometry(QtCore.QRect(70, 60, 171, 20))
        self.CommunitiesShowHumansCheckBox.setChecked(True)
        self.CommunitiesShowHumansCheckBox.setObjectName("CommunitiesShowHumansCheckBox")
        self.CommunitiesShowHumansCheckBox.stateChanged.connect(self.handleCommunitiesCheckboxes)
        self.graphicsView_communities = QtWidgets.QWidget(self.communities)
        self.graphicsView_communities.setObjectName("centralwidget")
        self.graphicsView_communities.webEngineView = QtWebEngineWidgets.QWebEngineView(self.graphicsView_communities)
        self.graphicsView_communities.webEngineView.load(QtCore.QUrl().fromLocalFile('./html/communities.html'))
        self.graphicsView_communities.setGeometry(QtCore.QRect(60, 110, 1331, 551))
        self.graphicsView_communities.webEngineView.setFixedWidth(1400)
        self.graphicsView_communities.webEngineView.setFixedHeight(2000)
        #self.graphicsView_communities.webEngineView.setZoomFactor(5)
        self.graphicsView_communities.setLayoutDirection(QtCore.Qt.RightToLeft)
        #self.graphicsView_communities = QtWidgets.QWidget()
        self.Qtab_Insights.addTab(self.communities, "")
        self.decomposition = QtWidgets.QWidget()
        self.decomposition.setObjectName("decomposition")
        self.DecompositionShowBotsCheckBox = QtWidgets.QCheckBox(self.decomposition)
        self.DecompositionShowBotsCheckBox.setGeometry(QtCore.QRect(70, 20, 111, 41))
        self.DecompositionShowBotsCheckBox.setChecked(True)
        self.DecompositionShowBotsCheckBox.setObjectName("DecompositionShowBotsCheckBox")
        self.DecompositionShowBotsCheckBox.stateChanged.connect(self.handleDecompositionCheckboxes)
        self.DecompositionShowHumansCheckBox = QtWidgets.QCheckBox(self.decomposition)
        self.DecompositionShowHumansCheckBox.setGeometry(QtCore.QRect(70, 60, 171, 20))
        self.DecompositionShowHumansCheckBox.setChecked(True)
        self.DecompositionShowHumansCheckBox.setObjectName("DecompositionShowHumansCheckBox")
        self.DecompositionShowHumansCheckBox.stateChanged.connect(self.handleDecompositionCheckboxes)

        self.graphicsView_decomposition = QtWidgets.QWidget(self.decomposition)
        self.graphicsView_decomposition.webEngineView = QtWebEngineWidgets.QWebEngineView(self.graphicsView_decomposition)
        self.graphicsView_decomposition.webEngineView.load(QtCore.QUrl().fromLocalFile('./html/decomposition.html'))
        self.graphicsView_decomposition.setGeometry(QtCore.QRect(60, 110, 1331, 551))
        self.graphicsView_decomposition.webEngineView.setFixedWidth(1400)
        self.graphicsView_decomposition.webEngineView.setFixedHeight(2000)
        self.graphicsView_decomposition.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.KValueSlider = QtWidgets.QSlider(self.decomposition)
        self.KValueSlider.setGeometry(QtCore.QRect(1030, 30, 160, 22))
        self.KValueSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.KValueSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.KValueSlider.setAutoFillBackground(False)
        self.KValueSlider.setMaximum(100)
        self.KValueSlider.setSingleStep(10)
        self.KValueSlider.setProperty("value", 50)
        self.KValueSlider.setSliderPosition(50)
        self.KValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.KValueSlider.setObjectName("KValueSlider")
        self.KValueSlider.valueChanged.connect(self.manageSliderChange)

        self.kvalue = QtWidgets.QLabel(self.decomposition)
        self.kvalue.setGeometry(QtCore.QRect(950, 30, 61, 21))
        self.kvalue.setObjectName("kvalue")
        self.KValueLabel = QtWidgets.QLabel(self.decomposition)
        self.KValueLabel.setGeometry(QtCore.QRect(1210, 30, 55, 16))
        self.KValueLabel.setText("50")
        self.KValueLabel.setObjectName("KValueLabel")
        self.Qtab_Insights.addTab(self.decomposition, "")
        self.influencers = QtWidgets.QWidget()
        self.influencers.setObjectName("influencers")
        self.InfluencersShowBotsCheckBox = QtWidgets.QCheckBox(self.influencers)
        self.InfluencersShowBotsCheckBox.setGeometry(QtCore.QRect(70, 20, 111, 41))
        self.InfluencersShowBotsCheckBox.setChecked(True)
        self.InfluencersShowBotsCheckBox.setObjectName("InfluencersShowBotsCheckBox")
        self.InfluencersShowBotsCheckBox.stateChanged.connect(self.handleInfluencersCheckboxes)
        self.InfluencersShowHumansCheckBox = QtWidgets.QCheckBox(self.influencers)
        self.InfluencersShowHumansCheckBox.setGeometry(QtCore.QRect(70, 60, 171, 20))
        self.InfluencersShowHumansCheckBox.setChecked(True)
        self.InfluencersShowHumansCheckBox.setObjectName("InfluencersShowHumansCheckBox")
        self.InfluencersShowHumansCheckBox.stateChanged.connect(self.handleInfluencersCheckboxes)
        self.NumberOfAccountSlider = QtWidgets.QSlider(self.influencers)
        self.NumberOfAccountSlider.setGeometry(QtCore.QRect(1030, 30, 160, 22))
        self.NumberOfAccountSlider.setMinimum(1)
        self.NumberOfAccountSlider.setMaximum(10)
        self.NumberOfAccountSlider.setProperty("value", 5)
        self.NumberOfAccountSlider.setSliderPosition(5)
        self.NumberOfAccountSlider.setOrientation(QtCore.Qt.Horizontal)
        self.NumberOfAccountSlider.setObjectName("NumberOfAccountSlider")
        self.NumberOfAccountSlider.valueChanged.connect(self.manageSliderChange)

        self.NumberOfAccounts = QtWidgets.QLabel(self.influencers)
        self.NumberOfAccounts.setGeometry(QtCore.QRect(880, 30, 131, 21))
        self.NumberOfAccounts.setObjectName("NumberOfAccounts")

        self.NumberOfAccountLabel = QtWidgets.QLabel(self.influencers)
        self.NumberOfAccountLabel.setGeometry(QtCore.QRect(1210, 30, 55, 16))
        self.NumberOfAccountLabel.setText("5")
        self.NumberOfAccountLabel.setObjectName("NumberOfAccountLabel")

        self.graphicsView_influencers = QtWidgets.QWidget(self.influencers)
        self.graphicsView_influencers.webEngineView = QtWebEngineWidgets.QWebEngineView(self.graphicsView_influencers)
        self.graphicsView_influencers.webEngineView.load(QtCore.QUrl().fromLocalFile('./html/influencers.html'))
        self.graphicsView_influencers.setGeometry(QtCore.QRect(60, 110, 1331, 551))
        self.graphicsView_influencers.webEngineView.setFixedWidth(1400)
        self.graphicsView_influencers.webEngineView.setFixedHeight(2000)
        self.graphicsView_influencers.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.Qtab_Insights.addTab(self.influencers, "")
        self.retweets = QtWidgets.QWidget()
        self.retweets.setObjectName("retweets")

        self.graphicsView_retweets = QtWidgets.QWidget(self.retweets)
        self.graphicsView_retweets.webEngineView = QtWebEngineWidgets.QWebEngineView(self.graphicsView_retweets)
        self.graphicsView_retweets.webEngineView.load(QtCore.QUrl().fromLocalFile('./html/retweets.html'))
        self.graphicsView_retweets.setGeometry(QtCore.QRect(60, 110, 1331, 551))
        self.graphicsView_retweets.webEngineView.setFixedWidth(1400)
        self.graphicsView_retweets.webEngineView.setFixedHeight(2000)
        self.graphicsView_retweets.setLayoutDirection(QtCore.Qt.RightToLeft)


        self.Qtab_Insights.addTab(self.retweets, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 231, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../twitter insights.png"))
        self.label.setObjectName("label")
        MainWindow_TwitterInsights.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_TwitterInsights)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1521, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_TwitterInsights.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_TwitterInsights)
        self.statusbar.setObjectName("statusbar")
        MainWindow_TwitterInsights.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_TwitterInsights)
        self.Qtab_Insights.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_TwitterInsights)

    def retranslateUi(self, MainWindow_TwitterInsights):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_TwitterInsights.setWindowTitle(_translate("MainWindow_TwitterInsights", "Twitter Insights"))
        self.CommunitiesShowBotsCheckBox.setText(_translate("MainWindow_TwitterInsights", "Show Bots"))
        self.CommunitiesShowHumansCheckBox.setText(_translate("MainWindow_TwitterInsights", "Show Humans"))
        self.Qtab_Insights.setTabText(self.Qtab_Insights.indexOf(self.communities), _translate("MainWindow_TwitterInsights", "   Communities      "))
        self.DecompositionShowBotsCheckBox.setText(_translate("MainWindow_TwitterInsights", "Show Bots"))
        self.DecompositionShowHumansCheckBox.setText(_translate("MainWindow_TwitterInsights", "Show Humans"))
        self.kvalue.setText(_translate("MainWindow_TwitterInsights", "K-Value"))
        self.Qtab_Insights.setTabText(self.Qtab_Insights.indexOf(self.decomposition), _translate("MainWindow_TwitterInsights", "   Decomposition    "))
        self.InfluencersShowBotsCheckBox.setText(_translate("MainWindow_TwitterInsights", "Show Bots"))
        self.InfluencersShowHumansCheckBox.setText(_translate("MainWindow_TwitterInsights", "Show Humans"))
        self.NumberOfAccounts.setText(_translate("MainWindow_TwitterInsights", "Number of Accounts"))
        # self.Bots.setText(_translate("MainWindow_TwitterInsights", "Bots: "))
        # self.Humans.setText(_translate("MainWindow_TwitterInsights", "Humans: "))
        self.Qtab_Insights.setTabText(self.Qtab_Insights.indexOf(self.influencers), _translate("MainWindow_TwitterInsights", "     Influencers       "))
        self.Qtab_Insights.setTabText(self.Qtab_Insights.indexOf(self.retweets), _translate("MainWindow_TwitterInsights", "       Retweets          "))

    # setting KValueLabel and NumberOfAccountLabel Based on the corresponding slider value
    def manageSliderChange(self,value):
        if(self.centralwidget.sender().objectName() == "KValueSlider"):
            self.KValueLabel.setText(str(value))
            self.graphicsView_decomposition.webEngineView.reload()
        if(self.centralwidget.sender().objectName() == "NumberOfAccountSlider"):
            self.NumberOfAccountLabel.setText(str(value))
            self.graphicsView_influencers.webEngineView.reload()


    # Handle Communities Checkboxes
    def handleCommunitiesCheckboxes(self,state):
        if state == QtCore.Qt.Unchecked:
          if(self.centralwidget.sender().objectName() =="CommunitiesShowBotsCheckBox"):
            self.CommunitiesShowHumansCheckBox.setChecked(True)
          if(self.centralwidget.sender().objectName() =="CommunitiesShowHumansCheckBox"):
            self.CommunitiesShowBotsCheckBox.setChecked(True)
        #updatecommuntiesdiagram(self.CommunitiesShowBotsCheckBox.state(),self.CommunitiesShowHumansCheckBox.state())
        self.graphicsView_communities.webEngineView.reload()
    # Handle Decomposition Checkboxes
    def handleDecompositionCheckboxes(self,state):
        #updateDecompositiondiagram(self.DecompositionShowBotsCheckBox.state(),self.DecompositionShowHumansCheckBox.state(),self.KValueSlider.value())
        if state == QtCore.Qt.Unchecked:
          if(self.centralwidget.sender().objectName() =="DecompositionShowBotsCheckBox"):
            self.DecompositionShowHumansCheckBox.setChecked(True)
          if(self.centralwidget.sender().objectName() =="DecompositionShowHumansCheckBox"):
            self.DecompositionShowBotsCheckBox.setChecked(True)
        self.graphicsView_decomposition.webEngineView.reload()
    # Handle Influencers Checkboxes
    def handleInfluencersCheckboxes(self,state):
        #updateInfluencersdiagram(self.InfluencersShowBotsCheckBox.state(),self.InfluencersShowHumansCheckBox.state(),self.NumberOfAccountSlider.value())
        if state == QtCore.Qt.Unchecked:
          if(self.centralwidget.sender().objectName() =="InfluencersShowBotsCheckBox"):
            self.InfluencersShowHumansCheckBox.setChecked(True)
          if(self.centralwidget.sender().objectName() =="InfluencersShowHumansCheckBox"):
            self.InfluencersShowBotsCheckBox.setChecked(True)
        self.graphicsView_influencers.webEngineView.reload()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_TwitterInsights = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_TwitterInsights()
    ui.setupUi(MainWindow_TwitterInsights)
    MainWindow_TwitterInsights.show()
    sys.exit(app.exec_())
