'''
Note: UI made with the help of QT Designer.
The program is long because of the button style sheets, but it is fairly easy to understand.
The comments highlights how the program flows.
'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from equation import balanceChemicalEquation
from elements import Elements
from elementWindowUI import Ui_elementWindow
from howToUseUI import Ui_howToUse
import sys

class chemWiz(QMainWindow):
    def __init__(self):                                                                 # Initiates object and
        super().__init__()                                                              # calls parent constructor
        self.setupUi()                                                                  # Starts program

    def setupUi(self):
        self.setObjectName("ChemWiz")
        self.setEnabled(True)
        self.resize(820, 500)
        self.setMinimumSize(QtCore.QSize(820, 500))
        self.setMaximumSize(QtCore.QSize(820, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.setFont(font)
        icon = QtGui.QIcon()                                                            # Loads icon
        icon.addPixmap(QtGui.QPixmap(":/icons/atom.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        # Set Keyboard Shortcuts Here
        self.shorcut_closeWindow = QShortcut(QKeySequence("Ctrl+Q"),self)
        self.shorcut_closeWindow.activated.connect(self.close)
        self.shorcut_closeWindow = QShortcut(QKeySequence("Ctrl+E"),self)
        self.shorcut_closeWindow.activated.connect(self.clearInput)

        # HOME
        self.home = QtWidgets.QWidget(self.centralwidget)
        self.home.setEnabled(True)
        self.home.setGeometry(QtCore.QRect(80, 0, 740, 500))
        self.home.setMinimumSize(QtCore.QSize(0, 0))
        self.home.setMaximumSize(QtCore.QSize(740, 500))
        self.home.setObjectName("home")
        self.label_chemWiz_sub = QtWidgets.QLabel(self.home)
        self.label_chemWiz_sub.setGeometry(QtCore.QRect(240, 230, 261, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chemWiz_sub.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_chemWiz_sub.setFont(font)
        self.label_chemWiz_sub.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chemWiz_sub.setObjectName("label_chemWiz_sub")
        self.atomBG = QtWidgets.QLabel(self.home)
        self.atomBG.setGeometry(QtCore.QRect(470, 250, 300, 300))
        self.atomBG.setMinimumSize(QtCore.QSize(300, 300))
        self.atomBG.setText("")
        self.atomBG.setPixmap(QtGui.QPixmap(":/backGround/atom.svg"))
        self.atomBG.setScaledContents(True)
        self.atomBG.setWordWrap(False)
        self.atomBG.setObjectName("atomBG")
        self.label_chemWiz = QtWidgets.QLabel(self.home)
        self.label_chemWiz.setGeometry(QtCore.QRect(100, 110, 541, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 78, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 78, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chemWiz.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(74)
        font.setStrikeOut(False)
        self.label_chemWiz.setFont(font)
        self.label_chemWiz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_chemWiz.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chemWiz.setObjectName("label_chemWiz")
        self.label_howToUse = QtWidgets.QPushButton(self.home)
        self.label_howToUse.setGeometry(QtCore.QRect(300, 320, 141, 23))
        self.label_howToUse.clicked.connect(self.openHowToUseWindow)                      # Signal to open How To Use Window
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_howToUse.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_howToUse.setFont(font)
        self.label_howToUse.setFlat(True)
        self.label_howToUse.setObjectName("label_howToUse")
        self.label_developed = QtWidgets.QLabel(self.home)
        self.label_developed.setGeometry(QtCore.QRect(30, 450, 231, 21))
        self.label_developed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_developed.setObjectName("label_developed")

        # SIDEBAR
        self.sideBar_2 = QtWidgets.QWidget(self.centralwidget)
        self.sideBar_2.setGeometry(QtCore.QRect(0, 0, 75, 500))
        self.sideBar_2.setMinimumSize(QtCore.QSize(75, 500))
        self.sideBar_2.setMaximumSize(QtCore.QSize(75, 500))
        self.sideBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sideBar_2.setObjectName("sideBar_2")
        self.sideBar = QtWidgets.QVBoxLayout(self.sideBar_2)
        self.sideBar.setContentsMargins(0, 0, 0, 250)
        self.sideBar.setSpacing(0)
        self.sideBar.setObjectName("sideBar")
        self.sideBarButton1 = QtWidgets.QToolButton(self.sideBar_2)
        self.sideBarButton1.setMinimumSize(QtCore.QSize(75, 75))
        self.sideBarButton1.setMaximumSize(QtCore.QSize(75, 75))
        self.sideBarButton1.setStyleSheet("QToolButton {\n"
"    border-image: url(:/sideBar/sideBarButton1_idle.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/sideBar/sideBarButton1_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/sideBar/sideBarButton1_selected.png);\n"
"    }")
        self.sideBarButton1.setText("")
        self.sideBarButton1.setIconSize(QtCore.QSize(100, 100))
        self.sideBarButton1.setObjectName("sideBarButton1")
        self.sideBarButton1.clicked.connect(self.showHome)                      # Signal to open Home Menu
        self.sideBar.addWidget(self.sideBarButton1)
        self.sideBarButton2 = QtWidgets.QToolButton(self.sideBar_2)
        self.sideBarButton2.setMinimumSize(QtCore.QSize(75, 75))
        self.sideBarButton2.setMaximumSize(QtCore.QSize(75, 75))
        self.sideBarButton2.setStyleSheet("QToolButton {\n"
"    border-image: url(:/sideBar/sideBarButton2_idle.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/sideBar/sideBarButton2_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/sideBar/sideBarButton2_selected.png);\n"
"    }")
        self.sideBarButton2.setText("")
        self.sideBarButton2.setIconSize(QtCore.QSize(100, 100))
        self.sideBarButton2.setAutoRaise(False)
        self.sideBarButton2.setObjectName("sideBarButton2")
        self.sideBarButton2.clicked.connect(self.showPeriodicTable)           # Signal to open Periodic Table
        self.sideBar.addWidget(self.sideBarButton2)
        self.sideBarButton3 = QtWidgets.QToolButton(self.sideBar_2)
        self.sideBarButton3.setMinimumSize(QtCore.QSize(75, 75))
        self.sideBarButton3.setMaximumSize(QtCore.QSize(75, 75))
        self.sideBarButton3.setStyleSheet("QToolButton {\n"
"    border-image: url(:/sideBar/sideBarButton4_idle.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/sideBar/sideBarButton4_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/sideBar/sideBarButton4_selected.png);\n"
"    }")
        self.sideBarButton3.setText("")
        self.sideBarButton3.setIconSize(QtCore.QSize(100, 100))
        self.sideBarButton3.setAutoRaise(False)
        self.sideBarButton3.setObjectName("sideBarButton3")
        self.sideBarButton3.clicked.connect(self.showEquationBalancer)        # Signal to open Chemical Equation Balancer
        self.sideBar.addWidget(self.sideBarButton3)
        self.sideBarButton4 = QtWidgets.QPushButton(self.sideBar_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        self.sideBarButton4.setFont(font)
        self.sideBarButton4.setFlat(True)
        self.sideBarButton4.setObjectName("sideBarButton4")
        self.sideBarButton4.clicked.connect(self.showCredits)                 # Signal to open Credits
        self.sideBar.addWidget(self.sideBarButton4)
        self.sideBar_BG = QtWidgets.QLabel(self.centralwidget)
        self.sideBar_BG.setGeometry(QtCore.QRect(0, 0, 75, 500))
        self.sideBar_BG.setMinimumSize(QtCore.QSize(75, 500))
        self.sideBar_BG.setMaximumSize(QtCore.QSize(75, 500))
        self.sideBar_BG.setText("")
        self.sideBar_BG.setPixmap(QtGui.QPixmap(":/sideBar/sideBarBG.png"))
        self.sideBar_BG.setScaledContents(True)
        self.sideBar_BG.setObjectName("sideBar_BG")

        # PERIODIC TABLE
        self.periodicTable = QtWidgets.QWidget(self.centralwidget)
        self.periodicTable.setGeometry(QtCore.QRect(80, 0, 740, 500))
        self.periodicTable.setMaximumSize(QtCore.QSize(740, 500))
        self.periodicTable.setObjectName("periodicTable")
        self.elementButton_1 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_1.setGeometry(QtCore.QRect(10, 60, 40, 40))
        self.elementButton_1.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_1.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_1.setFont(font)
        self.elementButton_1.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    \n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_1.setAutoRaise(True)
        self.elementButton_1.setObjectName("elementButton_1")
        self.elementButton_2 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_2.setGeometry(QtCore.QRect(690, 60, 40, 40))
        self.elementButton_2.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_2.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(13)
        self.elementButton_2.setFont(font)
        self.elementButton_2.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_2.setAutoRaise(True)
        self.elementButton_2.setObjectName("elementButton_2")
        self.elementButton_3 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_3.setGeometry(QtCore.QRect(10, 100, 40, 40))
        self.elementButton_3.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_3.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_3.setFont(font)
        self.elementButton_3.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_3.setAutoRaise(True)
        self.elementButton_3.setObjectName("elementButton_3")
        self.elementButton_4 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_4.setGeometry(QtCore.QRect(50, 100, 40, 40))
        self.elementButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_4.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_4.setFont(font)
        self.elementButton_4.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_4.setAutoRaise(True)
        self.elementButton_4.setObjectName("elementButton_4")
        self.elementButton_5 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_5.setGeometry(QtCore.QRect(490, 100, 40, 40))
        self.elementButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_5.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_5.setFont(font)
        self.elementButton_5.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_5.setAutoRaise(True)
        self.elementButton_5.setObjectName("elementButton_5")
        self.elementButton_6 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_6.setGeometry(QtCore.QRect(530, 100, 40, 40))
        self.elementButton_6.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_6.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_6.setFont(font)
        self.elementButton_6.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_6.setAutoRaise(True)
        self.elementButton_6.setObjectName("elementButton_6")
        self.elementButton_7 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_7.setGeometry(QtCore.QRect(570, 100, 40, 40))
        self.elementButton_7.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_7.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_7.setFont(font)
        self.elementButton_7.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_7.setAutoRaise(True)
        self.elementButton_7.setObjectName("elementButton_7")
        self.elementButton_8 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_8.setGeometry(QtCore.QRect(610, 100, 40, 40))
        self.elementButton_8.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_8.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_8.setFont(font)
        self.elementButton_8.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_8.setAutoRaise(True)
        self.elementButton_8.setObjectName("elementButton_8")
        self.elementButton_9 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_9.setGeometry(QtCore.QRect(650, 100, 40, 40))
        self.elementButton_9.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_9.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_9.setFont(font)
        self.elementButton_9.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_9.setAutoRaise(True)
        self.elementButton_9.setObjectName("elementButton_9")
        self.elementButton_10 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_10.setGeometry(QtCore.QRect(690, 100, 40, 40))
        self.elementButton_10.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_10.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_10.setFont(font)
        self.elementButton_10.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_10.setAutoRaise(True)
        self.elementButton_10.setObjectName("elementButton_10")
        self.elementButton_11 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_11.setGeometry(QtCore.QRect(10, 140, 40, 40))
        self.elementButton_11.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_11.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_11.setFont(font)
        self.elementButton_11.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_11.setAutoRaise(True)
        self.elementButton_11.setObjectName("elementButton_11")
        self.elementButton_12 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_12.setGeometry(QtCore.QRect(50, 140, 40, 40))
        self.elementButton_12.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_12.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_12.setFont(font)
        self.elementButton_12.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_12.setAutoRaise(True)
        self.elementButton_12.setObjectName("elementButton_12")
        self.elementButton_13 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_13.setGeometry(QtCore.QRect(490, 140, 40, 40))
        self.elementButton_13.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_13.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_13.setFont(font)
        self.elementButton_13.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_13.setAutoRaise(True)
        self.elementButton_13.setObjectName("elementButton_13")
        self.elementButton_14 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_14.setGeometry(QtCore.QRect(530, 140, 40, 40))
        self.elementButton_14.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_14.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_14.setFont(font)
        self.elementButton_14.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_14.setAutoRaise(True)
        self.elementButton_14.setObjectName("elementButton_14")
        self.elementButton_15 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_15.setGeometry(QtCore.QRect(570, 140, 40, 40))
        self.elementButton_15.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_15.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_15.setFont(font)
        self.elementButton_15.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_15.setAutoRaise(True)
        self.elementButton_15.setObjectName("elementButton_15")
        self.elementButton_16 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_16.setGeometry(QtCore.QRect(610, 140, 40, 40))
        self.elementButton_16.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_16.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_16.setFont(font)
        self.elementButton_16.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_16.setAutoRaise(True)
        self.elementButton_16.setObjectName("elementButton_16")
        self.elementButton_17 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_17.setGeometry(QtCore.QRect(650, 140, 40, 40))
        self.elementButton_17.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_17.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_17.setFont(font)
        self.elementButton_17.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_17.setAutoRaise(True)
        self.elementButton_17.setObjectName("elementButton_17")
        self.elementButton_18 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_18.setGeometry(QtCore.QRect(690, 140, 40, 40))
        self.elementButton_18.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_18.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_18.setFont(font)
        self.elementButton_18.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_18.setAutoRaise(True)
        self.elementButton_18.setObjectName("elementButton_18")
        self.elementButton_19 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_19.setGeometry(QtCore.QRect(10, 180, 40, 40))
        self.elementButton_19.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_19.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_19.setFont(font)
        self.elementButton_19.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_19.setAutoRaise(True)
        self.elementButton_19.setObjectName("elementButton_19")
        self.elementButton_20 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_20.setGeometry(QtCore.QRect(50, 180, 40, 40))
        self.elementButton_20.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_20.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_20.setFont(font)
        self.elementButton_20.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_20.setAutoRaise(True)
        self.elementButton_20.setObjectName("elementButton_20")
        self.elementButton_21 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_21.setGeometry(QtCore.QRect(90, 180, 40, 40))
        self.elementButton_21.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_21.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_21.setFont(font)
        self.elementButton_21.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_21.setAutoRaise(True)
        self.elementButton_21.setObjectName("elementButton_21")
        self.elementButton_22 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_22.setGeometry(QtCore.QRect(130, 180, 40, 40))
        self.elementButton_22.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_22.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_22.setFont(font)
        self.elementButton_22.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_22.setAutoRaise(True)
        self.elementButton_22.setObjectName("elementButton_22")
        self.elementButton_23 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_23.setGeometry(QtCore.QRect(170, 180, 40, 40))
        self.elementButton_23.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_23.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_23.setFont(font)
        self.elementButton_23.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_23.setAutoRaise(True)
        self.elementButton_23.setObjectName("elementButton_23")
        self.elementButton_24 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_24.setGeometry(QtCore.QRect(210, 180, 40, 40))
        self.elementButton_24.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_24.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_24.setFont(font)
        self.elementButton_24.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_24.setAutoRaise(True)
        self.elementButton_24.setObjectName("elementButton_24")
        self.elementButton_25 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_25.setGeometry(QtCore.QRect(250, 180, 40, 40))
        self.elementButton_25.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_25.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_25.setFont(font)
        self.elementButton_25.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_25.setAutoRaise(True)
        self.elementButton_25.setObjectName("elementButton_25")
        self.elementButton_26 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_26.setGeometry(QtCore.QRect(290, 180, 40, 40))
        self.elementButton_26.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_26.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_26.setFont(font)
        self.elementButton_26.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_26.setAutoRaise(True)
        self.elementButton_26.setObjectName("elementButton_26")
        self.elementButton_27 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_27.setGeometry(QtCore.QRect(330, 180, 40, 40))
        self.elementButton_27.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_27.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_27.setFont(font)
        self.elementButton_27.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_27.setAutoRaise(True)
        self.elementButton_27.setObjectName("elementButton_27")
        self.elementButton_28 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_28.setGeometry(QtCore.QRect(370, 180, 40, 40))
        self.elementButton_28.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_28.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_28.setFont(font)
        self.elementButton_28.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_28.setAutoRaise(True)
        self.elementButton_28.setObjectName("elementButton_28")
        self.elementButton_29 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_29.setGeometry(QtCore.QRect(410, 180, 40, 40))
        self.elementButton_29.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_29.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_29.setFont(font)
        self.elementButton_29.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_29.setAutoRaise(True)
        self.elementButton_29.setObjectName("elementButton_29")
        self.elementButton_30 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_30.setGeometry(QtCore.QRect(450, 180, 40, 40))
        self.elementButton_30.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_30.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_30.setFont(font)
        self.elementButton_30.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_30.setAutoRaise(True)
        self.elementButton_30.setObjectName("elementButton_30")
        self.elementButton_31 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_31.setGeometry(QtCore.QRect(490, 180, 40, 40))
        self.elementButton_31.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_31.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_31.setFont(font)
        self.elementButton_31.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_31.setAutoRaise(True)
        self.elementButton_31.setObjectName("elementButton_31")
        self.elementButton_32 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_32.setGeometry(QtCore.QRect(530, 180, 40, 40))
        self.elementButton_32.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_32.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_32.setFont(font)
        self.elementButton_32.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_32.setAutoRaise(True)
        self.elementButton_32.setObjectName("elementButton_32")
        self.elementButton_33 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_33.setGeometry(QtCore.QRect(570, 180, 40, 40))
        self.elementButton_33.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_33.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_33.setFont(font)
        self.elementButton_33.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_33.setAutoRaise(True)
        self.elementButton_33.setObjectName("elementButton_33")
        self.elementButton_34 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_34.setGeometry(QtCore.QRect(610, 180, 40, 40))
        self.elementButton_34.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_34.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_34.setFont(font)
        self.elementButton_34.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_otherNonMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_34.setAutoRaise(True)
        self.elementButton_34.setObjectName("elementButton_34")
        self.elementButton_35 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_35.setGeometry(QtCore.QRect(650, 180, 40, 40))
        self.elementButton_35.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_35.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_35.setFont(font)
        self.elementButton_35.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_35.setAutoRaise(True)
        self.elementButton_35.setObjectName("elementButton_35")
        self.elementButton_36 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_36.setGeometry(QtCore.QRect(690, 180, 40, 40))
        self.elementButton_36.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_36.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_36.setFont(font)
        self.elementButton_36.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_36.setAutoRaise(True)
        self.elementButton_36.setObjectName("elementButton_36")
        self.elementButton_37 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_37.setGeometry(QtCore.QRect(10, 220, 40, 40))
        self.elementButton_37.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_37.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_37.setFont(font)
        self.elementButton_37.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_37.setAutoRaise(True)
        self.elementButton_37.setObjectName("elementButton_37")
        self.elementButton_38 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_38.setGeometry(QtCore.QRect(50, 220, 40, 40))
        self.elementButton_38.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_38.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_38.setFont(font)
        self.elementButton_38.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_38.setAutoRaise(True)
        self.elementButton_38.setObjectName("elementButton_38")
        self.elementButton_39 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_39.setGeometry(QtCore.QRect(90, 220, 40, 40))
        self.elementButton_39.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_39.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_39.setFont(font)
        self.elementButton_39.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_39.setAutoRaise(True)
        self.elementButton_39.setObjectName("elementButton_39")
        self.elementButton_40 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_40.setGeometry(QtCore.QRect(130, 220, 40, 40))
        self.elementButton_40.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_40.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_40.setFont(font)
        self.elementButton_40.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_40.setAutoRaise(True)
        self.elementButton_40.setObjectName("elementButton_40")
        self.elementButton_41 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_41.setGeometry(QtCore.QRect(170, 220, 40, 40))
        self.elementButton_41.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_41.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_41.setFont(font)
        self.elementButton_41.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_41.setAutoRaise(True)
        self.elementButton_41.setObjectName("elementButton_41")
        self.elementButton_42 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_42.setGeometry(QtCore.QRect(210, 220, 40, 40))
        self.elementButton_42.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_42.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_42.setFont(font)
        self.elementButton_42.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_42.setAutoRaise(True)
        self.elementButton_42.setObjectName("elementButton_42")
        self.elementButton_43 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_43.setGeometry(QtCore.QRect(250, 220, 40, 40))
        self.elementButton_43.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_43.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_43.setFont(font)
        self.elementButton_43.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_43.setAutoRaise(True)
        self.elementButton_43.setObjectName("elementButton_43")
        self.elementButton_44 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_44.setGeometry(QtCore.QRect(290, 220, 40, 40))
        self.elementButton_44.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_44.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_44.setFont(font)
        self.elementButton_44.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_44.setAutoRaise(True)
        self.elementButton_44.setObjectName("elementButton_44")
        self.elementButton_45 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_45.setGeometry(QtCore.QRect(330, 220, 40, 40))
        self.elementButton_45.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_45.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_45.setFont(font)
        self.elementButton_45.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_45.setAutoRaise(True)
        self.elementButton_45.setObjectName("elementButton_45")
        self.elementButton_46 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_46.setGeometry(QtCore.QRect(370, 220, 40, 40))
        self.elementButton_46.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_46.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_46.setFont(font)
        self.elementButton_46.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_46.setAutoRaise(True)
        self.elementButton_46.setObjectName("elementButton_46")
        self.elementButton_47 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_47.setGeometry(QtCore.QRect(410, 220, 40, 40))
        self.elementButton_47.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_47.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_47.setFont(font)
        self.elementButton_47.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_47.setAutoRaise(True)
        self.elementButton_47.setObjectName("elementButton_47")
        self.elementButton_48 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_48.setGeometry(QtCore.QRect(450, 220, 40, 40))
        self.elementButton_48.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_48.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_48.setFont(font)
        self.elementButton_48.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_48.setAutoRaise(True)
        self.elementButton_48.setObjectName("elementButton_48")
        self.elementButton_49 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_49.setGeometry(QtCore.QRect(490, 220, 40, 40))
        self.elementButton_49.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_49.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_49.setFont(font)
        self.elementButton_49.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_49.setAutoRaise(True)
        self.elementButton_49.setObjectName("elementButton_49")
        self.elementButton_50 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_50.setGeometry(QtCore.QRect(530, 220, 40, 40))
        self.elementButton_50.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_50.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_50.setFont(font)
        self.elementButton_50.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_50.setAutoRaise(True)
        self.elementButton_50.setObjectName("elementButton_50")
        self.elementButton_51 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_51.setGeometry(QtCore.QRect(570, 220, 40, 40))
        self.elementButton_51.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_51.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_51.setFont(font)
        self.elementButton_51.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_51.setAutoRaise(True)
        self.elementButton_51.setObjectName("elementButton_51")
        self.elementButton_52 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_52.setGeometry(QtCore.QRect(610, 220, 40, 40))
        self.elementButton_52.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_52.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_52.setFont(font)
        self.elementButton_52.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_52.setAutoRaise(True)
        self.elementButton_52.setObjectName("elementButton_52")
        self.elementButton_53 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_53.setGeometry(QtCore.QRect(650, 220, 40, 40))
        self.elementButton_53.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_53.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_53.setFont(font)
        self.elementButton_53.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_53.setAutoRaise(True)
        self.elementButton_53.setObjectName("elementButton_53")
        self.elementButton_54 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_54.setGeometry(QtCore.QRect(690, 220, 40, 40))
        self.elementButton_54.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_54.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_54.setFont(font)
        self.elementButton_54.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_54.setAutoRaise(True)
        self.elementButton_54.setObjectName("elementButton_54")
        self.elementButton_55 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_55.setGeometry(QtCore.QRect(10, 260, 40, 40))
        self.elementButton_55.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_55.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_55.setFont(font)
        self.elementButton_55.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_55.setAutoRaise(True)
        self.elementButton_55.setObjectName("elementButton_55")
        self.elementButton_56 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_56.setGeometry(QtCore.QRect(50, 260, 40, 40))
        self.elementButton_56.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_56.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_56.setFont(font)
        self.elementButton_56.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_56.setAutoRaise(True)
        self.elementButton_56.setObjectName("elementButton_56")
        self.elementButton_57 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_57.setGeometry(QtCore.QRect(130, 360, 40, 40))
        self.elementButton_57.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_57.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_57.setFont(font)
        self.elementButton_57.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_57.setAutoRaise(True)
        self.elementButton_57.setObjectName("elementButton_57")
        self.elementButton_58 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_58.setGeometry(QtCore.QRect(170, 360, 40, 40))
        self.elementButton_58.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_58.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_58.setFont(font)
        self.elementButton_58.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_58.setAutoRaise(True)
        self.elementButton_58.setObjectName("elementButton_58")
        self.elementButton_59 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_59.setGeometry(QtCore.QRect(210, 360, 40, 40))
        self.elementButton_59.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_59.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_59.setFont(font)
        self.elementButton_59.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_59.setAutoRaise(True)
        self.elementButton_59.setObjectName("elementButton_59")
        self.elementButton_60 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_60.setGeometry(QtCore.QRect(250, 360, 40, 40))
        self.elementButton_60.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_60.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_60.setFont(font)
        self.elementButton_60.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_60.setAutoRaise(True)
        self.elementButton_60.setObjectName("elementButton_60")
        self.elementButton_61 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_61.setGeometry(QtCore.QRect(290, 360, 40, 40))
        self.elementButton_61.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_61.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_61.setFont(font)
        self.elementButton_61.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_61.setAutoRaise(True)
        self.elementButton_61.setObjectName("elementButton_61")
        self.elementButton_62 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_62.setGeometry(QtCore.QRect(330, 360, 40, 40))
        self.elementButton_62.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_62.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_62.setFont(font)
        self.elementButton_62.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_62.setAutoRaise(True)
        self.elementButton_62.setObjectName("elementButton_62")
        self.elementButton_63 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_63.setGeometry(QtCore.QRect(370, 360, 40, 40))
        self.elementButton_63.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_63.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_63.setFont(font)
        self.elementButton_63.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_63.setAutoRaise(True)
        self.elementButton_63.setObjectName("elementButton_63")
        self.elementButton_64 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_64.setGeometry(QtCore.QRect(410, 360, 40, 40))
        self.elementButton_64.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_64.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_64.setFont(font)
        self.elementButton_64.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_64.setAutoRaise(True)
        self.elementButton_64.setObjectName("elementButton_64")
        self.elementButton_65 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_65.setGeometry(QtCore.QRect(450, 360, 40, 40))
        self.elementButton_65.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_65.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_65.setFont(font)
        self.elementButton_65.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_65.setAutoRaise(True)
        self.elementButton_65.setObjectName("elementButton_65")
        self.elementButton_66 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_66.setGeometry(QtCore.QRect(490, 360, 40, 40))
        self.elementButton_66.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_66.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_66.setFont(font)
        self.elementButton_66.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_66.setAutoRaise(True)
        self.elementButton_66.setObjectName("elementButton_66")
        self.elementButton_67 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_67.setGeometry(QtCore.QRect(530, 360, 40, 40))
        self.elementButton_67.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_67.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_67.setFont(font)
        self.elementButton_67.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_67.setAutoRaise(True)
        self.elementButton_67.setObjectName("elementButton_67")
        self.elementButton_68 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_68.setGeometry(QtCore.QRect(570, 360, 40, 40))
        self.elementButton_68.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_68.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_68.setFont(font)
        self.elementButton_68.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_68.setAutoRaise(True)
        self.elementButton_68.setObjectName("elementButton_68")
        self.elementButton_69 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_69.setGeometry(QtCore.QRect(610, 360, 40, 40))
        self.elementButton_69.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_69.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_69.setFont(font)
        self.elementButton_69.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_69.setAutoRaise(True)
        self.elementButton_69.setObjectName("elementButton_69")
        self.elementButton_70 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_70.setGeometry(QtCore.QRect(650, 360, 40, 40))
        self.elementButton_70.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_70.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_70.setFont(font)
        self.elementButton_70.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_70.setAutoRaise(True)
        self.elementButton_70.setObjectName("elementButton_70")
        self.elementButton_71 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_71.setGeometry(QtCore.QRect(690, 360, 40, 40))
        self.elementButton_71.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_71.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_71.setFont(font)
        self.elementButton_71.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_lanthanides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_71.setAutoRaise(True)
        self.elementButton_71.setObjectName("elementButton_71")
        self.elementButton_72 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_72.setGeometry(QtCore.QRect(130, 260, 40, 40))
        self.elementButton_72.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_72.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_72.setFont(font)
        self.elementButton_72.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_72.setAutoRaise(True)
        self.elementButton_72.setObjectName("elementButton_72")
        self.elementButton_73 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_73.setGeometry(QtCore.QRect(170, 260, 40, 40))
        self.elementButton_73.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_73.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_73.setFont(font)
        self.elementButton_73.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_73.setAutoRaise(True)
        self.elementButton_73.setObjectName("elementButton_73")
        self.elementButton_74 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_74.setGeometry(QtCore.QRect(210, 260, 40, 40))
        self.elementButton_74.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_74.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_74.setFont(font)
        self.elementButton_74.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_74.setAutoRaise(True)
        self.elementButton_74.setObjectName("elementButton_74")
        self.elementButton_75 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_75.setGeometry(QtCore.QRect(250, 260, 40, 40))
        self.elementButton_75.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_75.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_75.setFont(font)
        self.elementButton_75.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_75.setAutoRaise(True)
        self.elementButton_75.setObjectName("elementButton_75")
        self.elementButton_76 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_76.setGeometry(QtCore.QRect(290, 260, 40, 40))
        self.elementButton_76.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_76.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_76.setFont(font)
        self.elementButton_76.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_76.setAutoRaise(True)
        self.elementButton_76.setObjectName("elementButton_76")
        self.elementButton_77 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_77.setGeometry(QtCore.QRect(330, 260, 40, 40))
        self.elementButton_77.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_77.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_77.setFont(font)
        self.elementButton_77.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_77.setAutoRaise(True)
        self.elementButton_77.setObjectName("elementButton_77")
        self.elementButton_78 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_78.setGeometry(QtCore.QRect(370, 260, 40, 40))
        self.elementButton_78.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_78.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_78.setFont(font)
        self.elementButton_78.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_78.setAutoRaise(True)
        self.elementButton_78.setObjectName("elementButton_78")
        self.elementButton_79 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_79.setGeometry(QtCore.QRect(410, 260, 40, 40))
        self.elementButton_79.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_79.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_79.setFont(font)
        self.elementButton_79.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_79.setAutoRaise(True)
        self.elementButton_79.setObjectName("elementButton_79")
        self.elementButton_80 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_80.setGeometry(QtCore.QRect(450, 260, 40, 40))
        self.elementButton_80.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_80.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_80.setFont(font)
        self.elementButton_80.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_80.setAutoRaise(True)
        self.elementButton_80.setObjectName("elementButton_80")
        self.elementButton_81 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_81.setGeometry(QtCore.QRect(490, 260, 40, 40))
        self.elementButton_81.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_81.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_81.setFont(font)
        self.elementButton_81.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_81.setAutoRaise(True)
        self.elementButton_81.setObjectName("elementButton_81")
        self.elementButton_82 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_82.setGeometry(QtCore.QRect(530, 260, 40, 40))
        self.elementButton_82.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_82.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_82.setFont(font)
        self.elementButton_82.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_82.setAutoRaise(True)
        self.elementButton_82.setObjectName("elementButton_82")
        self.elementButton_83 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_83.setGeometry(QtCore.QRect(570, 260, 40, 40))
        self.elementButton_83.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_83.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_83.setFont(font)
        self.elementButton_83.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_83.setAutoRaise(True)
        self.elementButton_83.setObjectName("elementButton_83")
        self.elementButton_84 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_84.setGeometry(QtCore.QRect(610, 260, 40, 40))
        self.elementButton_84.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_84.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_84.setFont(font)
        self.elementButton_84.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_metalloids_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_84.setAutoRaise(True)
        self.elementButton_84.setObjectName("elementButton_84")
        self.elementButton_85 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_85.setGeometry(QtCore.QRect(650, 260, 40, 40))
        self.elementButton_85.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_85.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_85.setFont(font)
        self.elementButton_85.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_85.setAutoRaise(True)
        self.elementButton_85.setObjectName("elementButton_85")
        self.elementButton_86 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_86.setGeometry(QtCore.QRect(690, 260, 40, 40))
        self.elementButton_86.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_86.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_86.setFont(font)
        self.elementButton_86.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_86.setAutoRaise(True)
        self.elementButton_86.setObjectName("elementButton_86")
        self.elementButton_87 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_87.setGeometry(QtCore.QRect(10, 300, 40, 40))
        self.elementButton_87.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_87.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_87.setFont(font)
        self.elementButton_87.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_87.setAutoRaise(True)
        self.elementButton_87.setObjectName("elementButton_87")
        self.elementButton_88 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_88.setGeometry(QtCore.QRect(50, 300, 40, 40))
        self.elementButton_88.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_88.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_88.setFont(font)
        self.elementButton_88.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_alkaliEarthMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_88.setAutoRaise(True)
        self.elementButton_88.setObjectName("elementButton_88")
        self.elementButton_89 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_89.setGeometry(QtCore.QRect(130, 400, 40, 40))
        self.elementButton_89.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_89.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_89.setFont(font)
        self.elementButton_89.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_89.setAutoRaise(True)
        self.elementButton_89.setObjectName("elementButton_89")
        self.elementButton_90 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_90.setGeometry(QtCore.QRect(170, 400, 40, 40))
        self.elementButton_90.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_90.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_90.setFont(font)
        self.elementButton_90.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_90.setAutoRaise(True)
        self.elementButton_90.setObjectName("elementButton_90")
        self.elementButton_91 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_91.setGeometry(QtCore.QRect(210, 400, 40, 40))
        self.elementButton_91.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_91.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_91.setFont(font)
        self.elementButton_91.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_91.setAutoRaise(True)
        self.elementButton_91.setObjectName("elementButton_91")
        self.elementButton_92 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_92.setGeometry(QtCore.QRect(250, 400, 40, 40))
        self.elementButton_92.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_92.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_92.setFont(font)
        self.elementButton_92.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_92.setAutoRaise(True)
        self.elementButton_92.setObjectName("elementButton_92")
        self.elementButton_93 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_93.setGeometry(QtCore.QRect(290, 400, 40, 40))
        self.elementButton_93.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_93.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_93.setFont(font)
        self.elementButton_93.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_93.setAutoRaise(True)
        self.elementButton_93.setObjectName("elementButton_93")
        self.elementButton_94 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_94.setGeometry(QtCore.QRect(330, 400, 40, 40))
        self.elementButton_94.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_94.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_94.setFont(font)
        self.elementButton_94.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_94.setAutoRaise(True)
        self.elementButton_94.setObjectName("elementButton_94")
        self.elementButton_95 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_95.setGeometry(QtCore.QRect(370, 400, 40, 40))
        self.elementButton_95.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_95.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_95.setFont(font)
        self.elementButton_95.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_95.setAutoRaise(True)
        self.elementButton_95.setObjectName("elementButton_95")
        self.elementButton_96 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_96.setGeometry(QtCore.QRect(410, 400, 40, 40))
        self.elementButton_96.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_96.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_96.setFont(font)
        self.elementButton_96.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_96.setAutoRaise(True)
        self.elementButton_96.setObjectName("elementButton_96")
        self.elementButton_97 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_97.setGeometry(QtCore.QRect(450, 400, 40, 40))
        self.elementButton_97.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_97.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_97.setFont(font)
        self.elementButton_97.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_97.setAutoRaise(True)
        self.elementButton_97.setObjectName("elementButton_97")
        self.elementButton_98 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_98.setGeometry(QtCore.QRect(490, 400, 40, 40))
        self.elementButton_98.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_98.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_98.setFont(font)
        self.elementButton_98.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_98.setAutoRaise(True)
        self.elementButton_98.setObjectName("elementButton_98")
        self.elementButton_99 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_99.setGeometry(QtCore.QRect(530, 400, 40, 40))
        self.elementButton_99.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_99.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_99.setFont(font)
        self.elementButton_99.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_99.setAutoRaise(True)
        self.elementButton_99.setObjectName("elementButton_99")
        self.elementButton_100 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_100.setGeometry(QtCore.QRect(570, 400, 40, 40))
        self.elementButton_100.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_100.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_100.setFont(font)
        self.elementButton_100.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_100.setAutoRaise(True)
        self.elementButton_100.setObjectName("elementButton_100")
        self.elementButton_101 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_101.setGeometry(QtCore.QRect(610, 400, 40, 40))
        self.elementButton_101.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_101.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_101.setFont(font)
        self.elementButton_101.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_101.setAutoRaise(True)
        self.elementButton_101.setObjectName("elementButton_101")
        self.elementButton_102 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_102.setGeometry(QtCore.QRect(650, 400, 40, 40))
        self.elementButton_102.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_102.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_102.setFont(font)
        self.elementButton_102.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_102.setAutoRaise(True)
        self.elementButton_102.setObjectName("elementButton_102")
        self.elementButton_103 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_103.setGeometry(QtCore.QRect(690, 400, 40, 40))
        self.elementButton_103.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_103.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_103.setFont(font)
        self.elementButton_103.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_actinides_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_103.setAutoRaise(True)
        self.elementButton_103.setObjectName("elementButton_103")
        self.elementButton_104 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_104.setGeometry(QtCore.QRect(130, 300, 40, 40))
        self.elementButton_104.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_104.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_104.setFont(font)
        self.elementButton_104.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_104.setAutoRaise(True)
        self.elementButton_104.setObjectName("elementButton_104")
        self.elementButton_105 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_105.setGeometry(QtCore.QRect(170, 300, 40, 40))
        self.elementButton_105.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_105.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_105.setFont(font)
        self.elementButton_105.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_105.setAutoRaise(True)
        self.elementButton_105.setObjectName("elementButton_105")
        self.elementButton_106 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_106.setGeometry(QtCore.QRect(210, 300, 40, 40))
        self.elementButton_106.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_106.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_106.setFont(font)
        self.elementButton_106.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_106.setAutoRaise(True)
        self.elementButton_106.setObjectName("elementButton_106")
        self.elementButton_107 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_107.setGeometry(QtCore.QRect(250, 300, 40, 40))
        self.elementButton_107.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_107.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_107.setFont(font)
        self.elementButton_107.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_107.setAutoRaise(True)
        self.elementButton_107.setObjectName("elementButton_107")
        self.elementButton_108 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_108.setGeometry(QtCore.QRect(290, 300, 40, 40))
        self.elementButton_108.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_108.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_108.setFont(font)
        self.elementButton_108.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_108.setAutoRaise(True)
        self.elementButton_108.setObjectName("elementButton_108")
        self.elementButton_109 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_109.setGeometry(QtCore.QRect(330, 300, 40, 40))
        self.elementButton_109.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_109.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_109.setFont(font)
        self.elementButton_109.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_109.setAutoRaise(True)
        self.elementButton_109.setObjectName("elementButton_109")
        self.elementButton_110 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_110.setGeometry(QtCore.QRect(370, 300, 40, 40))
        self.elementButton_110.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_110.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_110.setFont(font)
        self.elementButton_110.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_110.setAutoRaise(True)
        self.elementButton_110.setObjectName("elementButton_110")
        self.elementButton_111 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_111.setGeometry(QtCore.QRect(410, 300, 40, 40))
        self.elementButton_111.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_111.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_111.setFont(font)
        self.elementButton_111.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_111.setAutoRaise(True)
        self.elementButton_111.setObjectName("elementButton_111")
        self.elementButton_112 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_112.setGeometry(QtCore.QRect(450, 300, 40, 40))
        self.elementButton_112.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_112.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_112.setFont(font)
        self.elementButton_112.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_transitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_112.setAutoRaise(True)
        self.elementButton_112.setObjectName("elementButton_112")
        self.elementButton_113 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_113.setGeometry(QtCore.QRect(490, 300, 40, 40))
        self.elementButton_113.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_113.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_113.setFont(font)
        self.elementButton_113.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_113.setAutoRaise(True)
        self.elementButton_113.setObjectName("elementButton_113")
        self.elementButton_114 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_114.setGeometry(QtCore.QRect(530, 300, 40, 40))
        self.elementButton_114.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_114.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_114.setFont(font)
        self.elementButton_114.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_114.setAutoRaise(True)
        self.elementButton_114.setObjectName("elementButton_114")
        self.elementButton_115 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_115.setGeometry(QtCore.QRect(570, 300, 40, 40))
        self.elementButton_115.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_115.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_115.setFont(font)
        self.elementButton_115.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_115.setAutoRaise(True)
        self.elementButton_115.setObjectName("elementButton_115")
        self.elementButton_116 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_116.setGeometry(QtCore.QRect(610, 300, 40, 40))
        self.elementButton_116.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_116.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_116.setFont(font)
        self.elementButton_116.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_postTransitionMetals_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_116.setAutoRaise(True)
        self.elementButton_116.setObjectName("elementButton_116")
        self.elementButton_117 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_117.setGeometry(QtCore.QRect(650, 300, 40, 40))
        self.elementButton_117.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_117.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_117.setFont(font)
        self.elementButton_117.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_halogens_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_117.setAutoRaise(True)
        self.elementButton_117.setObjectName("elementButton_117")
        self.elementButton_118 = QtWidgets.QToolButton(self.periodicTable)
        self.elementButton_118.setGeometry(QtCore.QRect(690, 300, 40, 40))
        self.elementButton_118.setMinimumSize(QtCore.QSize(40, 40))
        self.elementButton_118.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.elementButton_118.setFont(font)
        self.elementButton_118.setStyleSheet("QToolButton {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases.png);\n"
"    }\n"
"\n"
"QToolButton:hover {\n"
"    border-image: url(:/periodicTable/periodicTableButton_nobleGases_hovered.png);\n"
"    }\n"
"\n"
"QToolButton:pressed {\n"
"    border-image: url(:/periodicTable/periodicTableButton_selected.png);\n"
"    }")
        self.elementButton_118.setAutoRaise(True)
        self.elementButton_118.setObjectName("elementButton_118")
        self.label_groupIA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIA.setGeometry(QtCore.QRect(20, 40, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIA.setFont(font)
        self.label_groupIA.setObjectName("label_groupIA")
        self.label_groupIIA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIIA.setGeometry(QtCore.QRect(60, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIIA.setFont(font)
        self.label_groupIIA.setObjectName("label_groupIIA")
        self.label_groupIIIB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIIIB.setGeometry(QtCore.QRect(100, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIIIB.setFont(font)
        self.label_groupIIIB.setObjectName("label_groupIIIB")
        self.label_groupIVB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIVB.setGeometry(QtCore.QRect(140, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIVB.setFont(font)
        self.label_groupIVB.setObjectName("label_groupIVB")
        self.label_groupVB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVB.setGeometry(QtCore.QRect(180, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVB.setFont(font)
        self.label_groupVB.setObjectName("label_groupVB")
        self.label_group1 = QtWidgets.QLabel(self.periodicTable)
        self.label_group1.setGeometry(QtCore.QRect(20, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group1.setFont(font)
        self.label_group1.setObjectName("label_group1")
        self.label_groupVIB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVIB.setGeometry(QtCore.QRect(220, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVIB.setFont(font)
        self.label_groupVIB.setObjectName("label_groupVIB")
        self.label_groupVIIB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVIIB.setGeometry(QtCore.QRect(260, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVIIB.setFont(font)
        self.label_groupVIIB.setObjectName("label_groupVIIB")
        self.label_groupVIIIB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVIIIB.setGeometry(QtCore.QRect(300, 160, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVIIIB.setFont(font)
        self.label_groupVIIIB.setObjectName("label_groupVIIIB")
        self.label_groupIB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIB.setGeometry(QtCore.QRect(420, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIB.setFont(font)
        self.label_groupIB.setObjectName("label_groupIB")
        self.label_groupIIB = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIIB.setGeometry(QtCore.QRect(460, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIIB.setFont(font)
        self.label_groupIIB.setObjectName("label_groupIIB")
        self.label_groupIIIA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIIIA.setGeometry(QtCore.QRect(500, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIIIA.setFont(font)
        self.label_groupIIIA.setObjectName("label_groupIIIA")
        self.label_groupIVA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIVA.setGeometry(QtCore.QRect(540, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIVA.setFont(font)
        self.label_groupIVA.setObjectName("label_groupIVA")
        self.label_groupIVA_2 = QtWidgets.QLabel(self.periodicTable)
        self.label_groupIVA_2.setGeometry(QtCore.QRect(580, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupIVA_2.setFont(font)
        self.label_groupIVA_2.setObjectName("label_groupIVA_2")
        self.label_groupVIA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVIA.setGeometry(QtCore.QRect(620, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVIA.setFont(font)
        self.label_groupVIA.setObjectName("label_groupVIA")
        self.label_groupVIIA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVIIA.setGeometry(QtCore.QRect(660, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVIIA.setFont(font)
        self.label_groupVIIA.setObjectName("label_groupVIIA")
        self.label_groupVIIIA = QtWidgets.QLabel(self.periodicTable)
        self.label_groupVIIIA.setGeometry(QtCore.QRect(690, 40, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_groupVIIIA.setFont(font)
        self.label_groupVIIIA.setObjectName("label_groupVIIIA")
        self.label_group2 = QtWidgets.QLabel(self.periodicTable)
        self.label_group2.setGeometry(QtCore.QRect(60, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group2.setFont(font)
        self.label_group2.setObjectName("label_group2")
        self.label_group3 = QtWidgets.QLabel(self.periodicTable)
        self.label_group3.setGeometry(QtCore.QRect(100, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group3.setFont(font)
        self.label_group3.setObjectName("label_group3")
        self.label_group4 = QtWidgets.QLabel(self.periodicTable)
        self.label_group4.setGeometry(QtCore.QRect(140, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group4.setFont(font)
        self.label_group4.setObjectName("label_group4")
        self.label_group5 = QtWidgets.QLabel(self.periodicTable)
        self.label_group5.setGeometry(QtCore.QRect(180, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group5.setFont(font)
        self.label_group5.setObjectName("label_group5")
        self.label_group6 = QtWidgets.QLabel(self.periodicTable)
        self.label_group6.setGeometry(QtCore.QRect(220, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group6.setFont(font)
        self.label_group6.setObjectName("label_group6")
        self.label_group7 = QtWidgets.QLabel(self.periodicTable)
        self.label_group7.setGeometry(QtCore.QRect(260, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group7.setFont(font)
        self.label_group7.setObjectName("label_group7")
        self.label_group8 = QtWidgets.QLabel(self.periodicTable)
        self.label_group8.setGeometry(QtCore.QRect(300, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group8.setFont(font)
        self.label_group8.setObjectName("label_group8")
        self.label_group9 = QtWidgets.QLabel(self.periodicTable)
        self.label_group9.setGeometry(QtCore.QRect(340, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group9.setFont(font)
        self.label_group9.setObjectName("label_group9")
        self.label_group10 = QtWidgets.QLabel(self.periodicTable)
        self.label_group10.setGeometry(QtCore.QRect(380, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group10.setFont(font)
        self.label_group10.setObjectName("label_group10")
        self.label_group11 = QtWidgets.QLabel(self.periodicTable)
        self.label_group11.setGeometry(QtCore.QRect(420, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group11.setFont(font)
        self.label_group11.setObjectName("label_group11")
        self.label_group12 = QtWidgets.QLabel(self.periodicTable)
        self.label_group12.setGeometry(QtCore.QRect(460, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group12.setFont(font)
        self.label_group12.setObjectName("label_group12")
        self.label_group13 = QtWidgets.QLabel(self.periodicTable)
        self.label_group13.setGeometry(QtCore.QRect(500, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group13.setFont(font)
        self.label_group13.setObjectName("label_group13")
        self.label_group14 = QtWidgets.QLabel(self.periodicTable)
        self.label_group14.setGeometry(QtCore.QRect(540, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group14.setFont(font)
        self.label_group14.setObjectName("label_group14")
        self.label_group15 = QtWidgets.QLabel(self.periodicTable)
        self.label_group15.setGeometry(QtCore.QRect(580, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group15.setFont(font)
        self.label_group15.setObjectName("label_group15")
        self.label_group16 = QtWidgets.QLabel(self.periodicTable)
        self.label_group16.setGeometry(QtCore.QRect(620, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group16.setFont(font)
        self.label_group16.setObjectName("label_group16")
        self.label_group17 = QtWidgets.QLabel(self.periodicTable)
        self.label_group17.setGeometry(QtCore.QRect(660, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group17.setFont(font)
        self.label_group17.setObjectName("label_group17")
        self.label_group18 = QtWidgets.QLabel(self.periodicTable)
        self.label_group18.setGeometry(QtCore.QRect(700, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_group18.setFont(font)
        self.label_group18.setObjectName("label_group18")
        self.periodicTableTitle = QtWidgets.QLabel(self.periodicTable)
        self.periodicTableTitle.setGeometry(QtCore.QRect(100, 20, 381, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.periodicTableTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.periodicTableTitle.setFont(font)
        self.periodicTableTitle.setStyleSheet("font: 25 26pt \"Segoe UI Light\";")
        self.periodicTableTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.periodicTableTitle.setObjectName("periodicTableTitle")
        self.label_lanthanides = QtWidgets.QLabel(self.periodicTable)
        self.label_lanthanides.setGeometry(QtCore.QRect(90, 260, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.label_lanthanides.setFont(font)
        self.label_lanthanides.setStyleSheet("border-image: url(:/periodicTable/periodicTableButton_lanthanides.png);")
        self.label_lanthanides.setObjectName("label_lanthanides")
        self.label_actinides = QtWidgets.QLabel(self.periodicTable)
        self.label_actinides.setGeometry(QtCore.QRect(90, 300, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.label_actinides.setFont(font)
        self.label_actinides.setStyleSheet("border-image: url(:/periodicTable/periodicTableButton_actinides.png);")
        self.label_actinides.setObjectName("label_actinides")
        self.periodicTableBG = QtWidgets.QLabel(self.periodicTable)
        self.periodicTableBG.setGeometry(QtCore.QRect(520, 310, 241, 221))
        self.periodicTableBG.setText("")
        self.periodicTableBG.setPixmap(QtGui.QPixmap(":/backGround/atom-1.svg"))
        self.periodicTableBG.setScaledContents(True)
        self.periodicTableBG.setObjectName("periodicTableBG")
        self.periodicTableBG.raise_()
        for j in range(1,119):
                eval(f"self.elementButton_{j}.raise_()")
        self.label_groupIA.raise_()
        self.label_groupIIA.raise_()
        self.label_groupIIIB.raise_()
        self.label_groupIVB.raise_()
        self.label_groupVB.raise_()
        self.label_group1.raise_()
        self.label_groupVIB.raise_()
        self.label_groupVIIB.raise_()
        self.label_groupVIIIB.raise_()
        self.label_groupIB.raise_()
        self.label_groupIIB.raise_()
        self.label_groupIIIA.raise_()
        self.label_groupIVA.raise_()
        self.label_groupIVA_2.raise_()
        self.label_groupVIA.raise_()
        self.label_groupVIIA.raise_()
        self.label_groupVIIIA.raise_()
        self.label_group2.raise_()
        self.label_group3.raise_()
        self.label_group4.raise_()
        self.label_group5.raise_()
        self.label_group6.raise_()
        self.label_group7.raise_()
        self.label_group8.raise_()
        self.label_group9.raise_()
        self.label_group10.raise_()
        self.label_group11.raise_()
        self.label_group12.raise_()
        self.label_group13.raise_()
        self.label_group14.raise_()
        self.label_group15.raise_()
        self.label_group16.raise_()
        self.label_group17.raise_()
        self.label_group18.raise_()
        self.periodicTableTitle.raise_()
        self.label_lanthanides.raise_()
        self.label_actinides.raise_()
        for n in range(1,119):                                                  # Generate Signal for Element Window
                eval(f"self.elementButton_{n}.clicked.connect(self.getElementClick)")

        # CHEMICAL EQUATION BALANCER
        self.equationBalancer = QtWidgets.QWidget(self.centralwidget)
        self.equationBalancer.setGeometry(QtCore.QRect(80, 0, 740, 500))
        self.equationBalancer.setMaximumSize(QtCore.QSize(740, 500))
        self.equationBalancer.setObjectName("equationBalancer")
        self.balancerTitle = QtWidgets.QLabel(self.equationBalancer)
        self.balancerTitle.setGeometry(QtCore.QRect(160, 20, 421, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.balancerTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.balancerTitle.setFont(font)
        self.balancerTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.balancerTitle.setObjectName("balancerTitle")
        self.balancerSubTitle = QtWidgets.QLabel(self.equationBalancer)
        self.balancerSubTitle.setGeometry(QtCore.QRect(200, 70, 341, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.balancerSubTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.balancerSubTitle.setFont(font)
        self.balancerSubTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.balancerSubTitle.setObjectName("balancerSubTitle")
        self.balancer_sample = QtWidgets.QLabel(self.equationBalancer)
        self.balancer_sample.setGeometry(QtCore.QRect(270, 230, 201, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.balancer_sample.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.balancer_sample.setFont(font)
        self.balancer_sample.setAlignment(QtCore.Qt.AlignCenter)
        self.balancer_sample.setObjectName("balancer_sample")
        self.balancer_sample.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.lineEdit_equationInput = QtWidgets.QLineEdit(self.equationBalancer)
        self.lineEdit_equationInput.setGeometry(QtCore.QRect(210, 200, 321, 31))
        self.lineEdit_equationInput.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_equationInput.setObjectName("lineEdit_equationInput")
        self.label_equation = QtWidgets.QLabel(self.equationBalancer)
        self.label_equation.setGeometry(QtCore.QRect(330, 170, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_equation.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_equation.setFont(font)
        self.label_equation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_equation.setObjectName("label_equation")
        self.label_instruction1 = QtWidgets.QLabel(self.equationBalancer)
        self.label_instruction1.setGeometry(QtCore.QRect(220, 120, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_instruction1.setFont(font)
        self.label_instruction1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_instruction1.setObjectName("label_instruction1")
        self.label_instruction2 = QtWidgets.QLabel(self.equationBalancer)
        self.label_instruction2.setGeometry(QtCore.QRect(220, 140, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_instruction2.setFont(font)
        self.label_instruction2.setObjectName("label_instruction2")
        self.label_balancedEquation = QtWidgets.QLabel(self.equationBalancer)
        self.label_balancedEquation.setGeometry(QtCore.QRect(280, 300, 181, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_balancedEquation.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_balancedEquation.setFont(font)
        self.label_balancedEquation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_balancedEquation.setObjectName("label_balancedEquation")
        self.label_underline = QtWidgets.QLabel(self.equationBalancer)
        self.label_underline.setGeometry(QtCore.QRect(210, 370, 321, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_underline.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_underline.setFont(font)
        self.label_underline.setObjectName("label_underline")
        self.label_result = QtWidgets.QLabel(self.equationBalancer)
        self.label_result.setGeometry(QtCore.QRect(160, 340, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_result.setObjectName("label_result")
        self.label_13 = QtWidgets.QLabel(self.equationBalancer)
        self.label_13.setGeometry(QtCore.QRect(530, 260, 271, 261))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/backGround/test-tube-5.svg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.equationBalancer)
        self.label_14.setGeometry(QtCore.QRect(0, 340, 211, 201))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/backGround/test-tube-4.svg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.pushButton_balance = QtWidgets.QPushButton(self.equationBalancer)
        self.pushButton_balance.setGeometry(QtCore.QRect(540, 200, 81, 31))
        self.pushButton_clear = QtWidgets.QPushButton(self.equationBalancer)
        self.pushButton_clear.setGeometry(QtCore.QRect(120, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_balance.setFont(font)
        self.pushButton_balance.setFlat(False)
        self.pushButton_balance.setObjectName("pushButton_balance")
        self.pushButton_balance.clicked.connect(self.balanceEquation)           # Signal to get result
        self.lineEdit_equationInput.returnPressed.connect(self.balanceEquation) # Also emits signal when Enter is pressed
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setFlat(False)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_clear.clicked.connect(self.clearInput)                  # Signal to clear input
        self.label_14.raise_()
        self.label_13.raise_()
        self.balancerTitle.raise_()
        self.balancerSubTitle.raise_()
        self.balancer_sample.raise_()
        self.lineEdit_equationInput.raise_()
        self.label_equation.raise_()
        self.label_instruction1.raise_()
        self.label_instruction2.raise_()
        self.label_balancedEquation.raise_()
        self.label_underline.raise_()
        self.label_result.raise_()
        self.pushButton_balance.raise_()

        # CREDITS
        self.credits = QtWidgets.QWidget(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(80, 0, 740, 500))
        self.credits.setMaximumSize(QtCore.QSize(740, 500))
        self.credits.setObjectName("credits")
        self.creditsTitle = QtWidgets.QLabel(self.credits)
        self.creditsTitle.setGeometry(QtCore.QRect(320, 60, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.creditsTitle.setFont(font)
        self.creditsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.creditsTitle.setObjectName("creditsTitle")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        self.creditsTitle.setPalette(palette)
        self.label_Freepik = QtWidgets.QLabel(self.credits)
        self.label_Freepik.setGeometry(QtCore.QRect(286, 140, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 108, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_Freepik.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Freepik.setFont(font)
        self.label_Freepik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Freepik.setOpenExternalLinks(True)
        self.label_Freepik.setObjectName("label_Freepik")
        self.label_FreepikSub = QtWidgets.QLabel(self.credits)
        self.label_FreepikSub.setGeometry(QtCore.QRect(240, 180, 261, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_FreepikSub.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_FreepikSub.setFont(font)
        self.label_FreepikSub.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FreepikSub.setObjectName("label_FreepikSub")
        self.label_ChernykhSub = QtWidgets.QLabel(self.credits)
        self.label_ChernykhSub.setGeometry(QtCore.QRect(210, 240, 321, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_ChernykhSub.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_ChernykhSub.setFont(font)
        self.label_ChernykhSub.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChernykhSub.setWordWrap(False)
        self.label_ChernykhSub.setObjectName("label_ChernykhSub")
        self.label_Chernykh = QtWidgets.QLabel(self.credits)
        self.label_Chernykh.setGeometry(QtCore.QRect(286, 200, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 150, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_Chernykh.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Chernykh.setFont(font)
        self.label_Chernykh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Chernykh.setWordWrap(False)
        self.label_Chernykh.setOpenExternalLinks(True)
        self.label_Chernykh.setObjectName("label_Chernykh")
        self.label_SyntheticProg = QtWidgets.QLabel(self.credits)
        self.label_SyntheticProg.setGeometry(QtCore.QRect(246, 270, 251, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 210, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.label_SyntheticProg.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_SyntheticProg.setFont(font)
        self.label_SyntheticProg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SyntheticProg.setWordWrap(False)
        self.label_SyntheticProg.setOpenExternalLinks(True)
        self.label_SyntheticProg.setObjectName("label_SyntheticProg")
        self.label_SyntheticProgSub = QtWidgets.QLabel(self.credits)
        self.label_SyntheticProgSub.setGeometry(QtCore.QRect(200, 310, 341, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 81, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_SyntheticProgSub.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_SyntheticProgSub.setFont(font)
        self.label_SyntheticProgSub.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SyntheticProgSub.setWordWrap(False)
        self.label_SyntheticProgSub.setObjectName("label_SyntheticProgSub")
        self.safetyGogglesBG = QtWidgets.QLabel(self.credits)
        self.safetyGogglesBG.setGeometry(QtCore.QRect(590, -30, 211, 171))
        self.safetyGogglesBG.setText("")
        self.safetyGogglesBG.setPixmap(QtGui.QPixmap(":/backGround/safety-glasses.svg"))
        self.safetyGogglesBG.setScaledContents(True)
        self.safetyGogglesBG.setObjectName("safetyGogglesBG")
        self.labCoatBG = QtWidgets.QLabel(self.credits)
        self.labCoatBG.setGeometry(QtCore.QRect(550, 120, 291, 311))
        self.labCoatBG.setText("")
        self.labCoatBG.setPixmap(QtGui.QPixmap(":/backGround/lab-coat.svg"))
        self.labCoatBG.setScaledContents(True)
        self.labCoatBG.setAlignment(QtCore.Qt.AlignCenter)
        self.labCoatBG.setObjectName("labCoatBG")
        self.loupeBG = QtWidgets.QLabel(self.credits)
        self.loupeBG.setGeometry(QtCore.QRect(0, 300, 201, 201))
        self.loupeBG.setText("")
        self.loupeBG.setPixmap(QtGui.QPixmap(":/backGround/loupe.svg"))
        self.loupeBG.setScaledContents(True)
        self.loupeBG.setObjectName("loupeBG")
        self.beakerBG = QtWidgets.QLabel(self.credits)
        self.beakerBG.setGeometry(QtCore.QRect(240, 360, 161, 171))
        self.beakerBG.setText("")
        self.beakerBG.setPixmap(QtGui.QPixmap(":/backGround/beaker-2.svg"))
        self.beakerBG.setScaledContents(True)
        self.beakerBG.setObjectName("beakerBG")
        self.flaskBG = QtWidgets.QLabel(self.credits)
        self.flaskBG.setGeometry(QtCore.QRect(380, 340, 201, 211))
        self.flaskBG.setText("")
        self.flaskBG.setPixmap(QtGui.QPixmap(":/backGround/flask-6.svg"))
        self.flaskBG.setScaledContents(True)
        self.flaskBG.setObjectName("flaskBG")
        self.microscopeBG = QtWidgets.QLabel(self.credits)
        self.microscopeBG.setGeometry(QtCore.QRect(-60, -40, 331, 311))
        self.microscopeBG.setText("")
        self.microscopeBG.setPixmap(QtGui.QPixmap(":/backGround/microscope.svg"))
        self.microscopeBG.setScaledContents(True)
        self.microscopeBG.setObjectName("microscopeBG")
        self.dnaBG = QtWidgets.QLabel(self.credits)
        self.dnaBG.setGeometry(QtCore.QRect(200, -140, 231, 231))
        self.dnaBG.setText("")
        self.dnaBG.setPixmap(QtGui.QPixmap(":/backGround/dna.svg"))
        self.dnaBG.setScaledContents(True)
        self.dnaBG.setObjectName("dnaBG")
        self.label_SyntheticProgSub.raise_()
        self.creditsTitle.raise_()
        self.label_Freepik.raise_()
        self.label_FreepikSub.raise_()
        self.label_ChernykhSub.raise_()
        self.label_Chernykh.raise_()
        self.label_SyntheticProg.raise_()
        self.safetyGogglesBG.raise_()
        self.labCoatBG.raise_()
        self.loupeBG.raise_()
        self.beakerBG.raise_()
        self.flaskBG.raise_()
        self.microscopeBG.raise_()
        self.dnaBG.raise_()
        self.sideBar_BG.raise_()
        self.sideBar_2.raise_()
        self.credits.raise_()
        self.equationBalancer.raise_()
        self.periodicTable.raise_()
        self.home.raise_()
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.home.show()                                                                # Set to only show home widget at startup
        self.periodicTable.hide()
        self.equationBalancer.hide()
        self.credits.hide()

    def showHome(self):                                                                 # Shows Home Widget
        self.periodicTable.hide()
        self.equationBalancer.hide()
        self.credits.hide()
        self.home.show()

    def showPeriodicTable(self):                                                        # Shows Periodic Widget
        self.equationBalancer.hide()
        self.credits.hide()
        self.home.hide()
        self.periodicTable.show()

    def showEquationBalancer(self):                                                     # Shows Equation Balancer Widget
        self.credits.hide()
        self.home.hide()
        self.periodicTable.hide()
        self.equationBalancer.show()

    def showCredits(self):                                                              # Shows Credits Widget
        self.home.hide()
        self.periodicTable.hide()
        self.equationBalancer.hide()
        self.credits.show()

    def openHowToUseWindow(self):                                                       # opens the How To Use Window
        self.howToUseWindow = QtWidgets.QMainWindow()
        self.howToUseUI = Ui_howToUse()
        self.howToUseUI.setupUi(self.howToUseWindow)
        self.howToUseWindow.show()

    def getElementClick(self):                                                        # Once signal is emitted from the elementButton,
        getElementN = self.sender().objectName()                                      # it will now get the number assigned to that button
        if len(getElementN) == 15:                                                    # and sends that integer to the next function
                element_n = int(getElementN[-1])                                      # to represent the element
        elif len(getElementN) == 16:
                element_n = int(getElementN[-2:16])
        elif len(getElementN) == 17:
                element_n = int(getElementN[-3:17])
        self.openElementWindow(element_n)

    def openElementWindow(self,element_n):                                            # Once element is received, it will now
        element = Elements()                                                          # get the information about that element
        try:                                                                          # and generate a window using the 
                eval(f"element.element_{element_n}()")                                # elementWindow class
                elementName = element.elementName
                atomicSymbol = element.atomicSymbol
                atomicNumber = element.atomicNumber
                atomicWeight = element.atomicWeight
                density = element.density
                meltingPointKelvin = element.meltingPointKelvin
                boilingPointKelvin = element.boilingPointKelvin
                oxidationState = element.oxidationState
                electronegativity = element.electronegativity
                period = element.period
                groupNumber = element.groupNumber
                group = element.group
                elementGroup = element.elementGroup
                electronConfiguration = element.electronConfiguration
                self.elementWindow = QtWidgets.QWidget()                                    
                self.elementUI = Ui_elementWindow(elementName,atomicSymbol,atomicNumber,\
                        atomicWeight,density,meltingPointKelvin,boilingPointKelvin,oxidationState,\
                                electronegativity,period,groupNumber,group,elementGroup,\
                                        electronConfiguration)
                self.elementUI.setupUi(self.elementWindow)
                self.elementWindow.show()                                                    # Opens the new window
        except AttributeError:
                self.errorHandler()                                                       # Error Handling
        
    def balanceEquation(self):                                                  # Balance the equation input
        user_input = self.lineEdit_equationInput.text()                         # using the equation balancer class
        try:
                equation = balanceChemicalEquation(user_input)
                self.label_result.setText(equation.balance())                   # Set the output to a QLabel Widget
        except IndexError:
                self.label_result.setText("Invalid Input.")                     # Handles Error

    def clearInput(self):                                                       # opens the How To Use Window
        self.label_result.setText("")
        self.lineEdit_equationInput.setText("")

    def closeEvent(self, event):                                                # Handles Close Event
        exitReply = QMessageBox.question(self, 'See you again!', 'Do you wish to exit program?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if exitReply == QMessageBox.Yes:
                event.accept()
        else:
                event.ignore()

    def errorHandler(self, event):                                                # Handles Error
        exitReply = QMessageBox.warning(self, 'Error', 'Unexpected error occured.',
                                        QMessageBox.Ok, QMessageBox.Ok)

    def retranslateUi(self):                                                      # This is where you can edit texts and 
        _translate = QtCore.QCoreApplication.translate                            # translation to other language.
        self.setWindowTitle(_translate("chemWizWindow", "ChemWiz"))
        self.label_chemWiz_sub.setText(_translate("chemWizWindow", "a Minimal Chemistry Application."))
        self.label_chemWiz.setText(_translate("chemWizWindow", "ChemWiz"))
        self.label_howToUse.setText(_translate("chemWizWindow", "How to use?"))
        self.label_developed.setText(_translate("chemWizWindow", "Developed by: John Carlo Dela Cruz"))
        self.sideBarButton1.setToolTip(_translate("chemWizWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Home</span></p></body></html>"))
        self.sideBarButton2.setToolTip(_translate("chemWizWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Periodic Table of Elements</span></p><p>See the elements and its information.</p></body></html>"))
        self.sideBarButton3.setToolTip(_translate("chemWizWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Chemical Equation Balancer</span></p><p>Input a chemical equation to balance it.</p></body></html>"))
        self.sideBarButton4.setText(_translate("chemWizWindow", "Credits"))
        self.elementButton_1.setText(_translate("chemWizWindow", "¹H"))
        self.elementButton_2.setText(_translate("chemWizWindow", "²He"))
        self.elementButton_3.setText(_translate("chemWizWindow", "³Li"))
        self.elementButton_4.setText(_translate("chemWizWindow", "⁴Be"))
        self.elementButton_5.setText(_translate("chemWizWindow", "⁵B"))
        self.elementButton_6.setText(_translate("chemWizWindow", "⁶C"))
        self.elementButton_7.setText(_translate("chemWizWindow", "⁷N"))
        self.elementButton_8.setText(_translate("chemWizWindow", "⁸O"))
        self.elementButton_9.setText(_translate("chemWizWindow", "⁹F"))
        self.elementButton_10.setText(_translate("chemWizWindow", "¹⁰Ne"))
        self.elementButton_11.setText(_translate("chemWizWindow", "¹¹Na"))
        self.elementButton_12.setText(_translate("chemWizWindow", "¹²Mg"))
        self.elementButton_13.setText(_translate("chemWizWindow", "¹³Al"))
        self.elementButton_14.setText(_translate("chemWizWindow", "¹⁴Si"))
        self.elementButton_15.setText(_translate("chemWizWindow", "¹⁵P"))
        self.elementButton_16.setText(_translate("chemWizWindow", "¹⁶S"))
        self.elementButton_17.setText(_translate("chemWizWindow", "¹⁷Cl"))
        self.elementButton_18.setText(_translate("chemWizWindow", "¹⁸Ar"))
        self.elementButton_19.setText(_translate("chemWizWindow", "¹⁹K"))
        self.elementButton_20.setText(_translate("chemWizWindow", "²⁰Ca"))
        self.elementButton_21.setText(_translate("chemWizWindow", "²¹Sc"))
        self.elementButton_22.setText(_translate("chemWizWindow", "²²Ti"))
        self.elementButton_23.setText(_translate("chemWizWindow", "²³V"))
        self.elementButton_24.setText(_translate("chemWizWindow", "²⁴Cr"))
        self.elementButton_25.setText(_translate("chemWizWindow", "²⁵Mn"))
        self.elementButton_26.setText(_translate("chemWizWindow", "²⁶Fe"))
        self.elementButton_27.setText(_translate("chemWizWindow", "²⁷Co"))
        self.elementButton_28.setText(_translate("chemWizWindow", "²⁸Ni"))
        self.elementButton_29.setText(_translate("chemWizWindow", "²⁹Cu"))
        self.elementButton_30.setText(_translate("chemWizWindow", "³⁰Zn"))
        self.elementButton_31.setText(_translate("chemWizWindow", "³¹Ga"))
        self.elementButton_32.setText(_translate("chemWizWindow", "³²Ge"))
        self.elementButton_33.setText(_translate("chemWizWindow", "³³As"))
        self.elementButton_34.setText(_translate("chemWizWindow", "³⁴Se"))
        self.elementButton_35.setText(_translate("chemWizWindow", "³⁵Br"))
        self.elementButton_36.setText(_translate("chemWizWindow", "³⁶Kr"))
        self.elementButton_37.setText(_translate("chemWizWindow", "³⁷Rb"))
        self.elementButton_38.setText(_translate("chemWizWindow", "³⁸Sr"))
        self.elementButton_39.setText(_translate("chemWizWindow", "³⁹Y"))
        self.elementButton_40.setText(_translate("chemWizWindow", "⁴⁰Zr"))
        self.elementButton_41.setText(_translate("chemWizWindow", "⁴¹Nb"))
        self.elementButton_42.setText(_translate("chemWizWindow", "⁴²Mo"))
        self.elementButton_43.setText(_translate("chemWizWindow", "⁴³Tc"))
        self.elementButton_44.setText(_translate("chemWizWindow", "⁴⁴Ru"))
        self.elementButton_45.setText(_translate("chemWizWindow", "⁴⁵Rh"))
        self.elementButton_46.setText(_translate("chemWizWindow", "⁴⁶Pd"))
        self.elementButton_47.setText(_translate("chemWizWindow", "⁴⁷Ag"))
        self.elementButton_48.setText(_translate("chemWizWindow", "⁴⁸Cd"))
        self.elementButton_49.setText(_translate("chemWizWindow", "⁴⁹In"))
        self.elementButton_50.setText(_translate("chemWizWindow", "⁵⁰Sn"))
        self.elementButton_51.setText(_translate("chemWizWindow", "⁵¹Sb"))
        self.elementButton_52.setText(_translate("chemWizWindow", "⁵²Te"))
        self.elementButton_53.setText(_translate("chemWizWindow", "⁵³I"))
        self.elementButton_54.setText(_translate("chemWizWindow", "⁵⁴Xe"))
        self.elementButton_55.setText(_translate("chemWizWindow", "⁵⁵Cs"))
        self.elementButton_56.setText(_translate("chemWizWindow", "⁵⁶Ba"))
        self.elementButton_57.setText(_translate("chemWizWindow", "⁵⁷La"))
        self.elementButton_58.setText(_translate("chemWizWindow", "⁵⁸Ce"))
        self.elementButton_59.setText(_translate("chemWizWindow", "⁵⁹Pr"))
        self.elementButton_60.setText(_translate("chemWizWindow", "⁶⁰Nd"))
        self.elementButton_61.setText(_translate("chemWizWindow", "⁶¹Pm"))
        self.elementButton_62.setText(_translate("chemWizWindow", "⁶²Sm"))
        self.elementButton_63.setText(_translate("chemWizWindow", "⁶³Eu"))
        self.elementButton_64.setText(_translate("chemWizWindow", "⁶⁴Gd"))
        self.elementButton_65.setText(_translate("chemWizWindow", "⁶⁵Tb"))
        self.elementButton_66.setText(_translate("chemWizWindow", "⁶⁶Dy"))
        self.elementButton_67.setText(_translate("chemWizWindow", "⁶⁷Ho"))
        self.elementButton_68.setText(_translate("chemWizWindow", "⁶⁸Er"))
        self.elementButton_69.setText(_translate("chemWizWindow", "⁶⁹Tm"))
        self.elementButton_70.setText(_translate("chemWizWindow", "⁷⁰Yb"))
        self.elementButton_71.setText(_translate("chemWizWindow", "⁷¹Lu"))
        self.elementButton_72.setText(_translate("chemWizWindow", "⁷²Hf"))
        self.elementButton_73.setText(_translate("chemWizWindow", "⁷³Ta"))
        self.elementButton_74.setText(_translate("chemWizWindow", "⁷⁴W"))
        self.elementButton_75.setText(_translate("chemWizWindow", "⁷⁵Re"))
        self.elementButton_76.setText(_translate("chemWizWindow", "⁷⁶Os"))
        self.elementButton_77.setText(_translate("chemWizWindow", "⁷⁷Ir"))
        self.elementButton_78.setText(_translate("chemWizWindow", "⁷⁸Pt"))
        self.elementButton_79.setText(_translate("chemWizWindow", "⁷⁹Au"))
        self.elementButton_80.setText(_translate("chemWizWindow", "⁸⁰Hg"))
        self.elementButton_81.setText(_translate("chemWizWindow", "⁸¹Ti"))
        self.elementButton_82.setText(_translate("chemWizWindow", "⁸²Pb"))
        self.elementButton_83.setText(_translate("chemWizWindow", "⁸³Bi"))
        self.elementButton_84.setText(_translate("chemWizWindow", "⁸⁴Po"))
        self.elementButton_85.setText(_translate("chemWizWindow", "⁸⁵At"))
        self.elementButton_86.setText(_translate("chemWizWindow", "⁸⁶Rn"))
        self.elementButton_87.setText(_translate("chemWizWindow", "⁸⁷Fr"))
        self.elementButton_88.setText(_translate("chemWizWindow", "⁸⁸Ra"))
        self.elementButton_89.setText(_translate("chemWizWindow", "⁸⁹Ac"))
        self.elementButton_90.setText(_translate("chemWizWindow", "⁹⁰Th"))
        self.elementButton_91.setText(_translate("chemWizWindow", "⁹¹Pa"))
        self.elementButton_92.setText(_translate("chemWizWindow", "⁹²U"))
        self.elementButton_93.setText(_translate("chemWizWindow", "⁹³Np"))
        self.elementButton_94.setText(_translate("chemWizWindow", "⁹⁴Pu"))
        self.elementButton_95.setText(_translate("chemWizWindow", "⁹⁵Am"))
        self.elementButton_96.setText(_translate("chemWizWindow", "⁹⁶Cm"))
        self.elementButton_97.setText(_translate("chemWizWindow", "⁹⁷Bk"))
        self.elementButton_98.setText(_translate("chemWizWindow", "⁹⁸Cf"))
        self.elementButton_99.setText(_translate("chemWizWindow", "⁹⁹Es"))
        self.elementButton_100.setText(_translate("chemWizWindow", "¹⁰⁰Fm"))
        self.elementButton_101.setText(_translate("chemWizWindow", "¹⁰¹Md"))
        self.elementButton_102.setText(_translate("chemWizWindow", "¹⁰²No"))
        self.elementButton_103.setText(_translate("chemWizWindow", "¹⁰³Lr"))
        self.elementButton_104.setText(_translate("chemWizWindow", "¹⁰⁴Rf"))
        self.elementButton_105.setText(_translate("chemWizWindow", "¹⁰⁵Db"))
        self.elementButton_106.setText(_translate("chemWizWindow", "¹⁰⁶Sg"))
        self.elementButton_107.setText(_translate("chemWizWindow", "¹⁰⁷Bh"))
        self.elementButton_108.setText(_translate("chemWizWindow", "¹⁰⁵Hs"))
        self.elementButton_109.setText(_translate("chemWizWindow", "¹⁰⁹Mt"))
        self.elementButton_110.setText(_translate("chemWizWindow", "¹¹⁰Ds"))
        self.elementButton_111.setText(_translate("chemWizWindow", "¹¹¹Rg"))
        self.elementButton_112.setText(_translate("chemWizWindow", "¹¹²Cn"))
        self.elementButton_113.setText(_translate("chemWizWindow", "¹¹³Nh"))
        self.elementButton_114.setText(_translate("chemWizWindow", "¹¹⁴Fl"))
        self.elementButton_115.setText(_translate("chemWizWindow", "¹¹⁵Mc"))
        self.elementButton_116.setText(_translate("chemWizWindow", "¹¹⁶Lv"))
        self.elementButton_117.setText(_translate("chemWizWindow", "¹¹⁷Ts"))
        self.elementButton_118.setText(_translate("chemWizWindow", "¹¹⁸Og"))

        for n in range(1,119):                                                                  # Generate ToolTips for Elements
                try:
                        element = Elements()
                        eval(f"element.element_{n}()")
                        eval(f'self.elementButton_{n}.setToolTip("{element.elementName}")')
                except AttributeError:
                        break

        self.label_groupIA.setText(_translate("chemWizWindow", " IA"))
        self.label_groupIIA.setText(_translate("chemWizWindow", " IIA"))
        self.label_groupIIIB.setText(_translate("chemWizWindow", " IIIB"))
        self.label_groupIVB.setText(_translate("chemWizWindow", " IVB"))
        self.label_groupVB.setText(_translate("chemWizWindow", " VB"))
        self.label_groupVIB.setText(_translate("chemWizWindow", "VIB"))
        self.label_groupVIIB.setText(_translate("chemWizWindow", "VIIB"))
        self.label_groupVIIIB.setText(_translate("chemWizWindow", "———VIIIB———"))
        self.label_groupIB.setText(_translate("chemWizWindow", " IB"))
        self.label_groupIIB.setText(_translate("chemWizWindow", " IIB"))
        self.label_groupIIIA.setText(_translate("chemWizWindow", " IIIA"))
        self.label_groupIVA.setText(_translate("chemWizWindow", "IVA"))
        self.label_groupIVA_2.setText(_translate("chemWizWindow", " VA"))
        self.label_groupVIA.setText(_translate("chemWizWindow", "VIA"))
        self.label_groupVIIA.setText(_translate("chemWizWindow", "VIIA"))
        self.label_groupVIIIA.setText(_translate("chemWizWindow", "  VIIIA"))
        self.label_group1.setText(_translate("chemWizWindow", "  1"))
        self.label_group2.setText(_translate("chemWizWindow", "  2"))
        self.label_group3.setText(_translate("chemWizWindow", "  3"))
        self.label_group4.setText(_translate("chemWizWindow", "  4"))
        self.label_group5.setText(_translate("chemWizWindow", "  5"))
        self.label_group6.setText(_translate("chemWizWindow", " 6"))
        self.label_group7.setText(_translate("chemWizWindow", "  7"))
        self.label_group8.setText(_translate("chemWizWindow", "  8"))
        self.label_group9.setText(_translate("chemWizWindow", " 9"))
        self.label_group10.setText(_translate("chemWizWindow", " 10"))
        self.label_group11.setText(_translate("chemWizWindow", " 11"))
        self.label_group12.setText(_translate("chemWizWindow", " 12"))
        self.label_group13.setText(_translate("chemWizWindow", " 13"))
        self.label_group14.setText(_translate("chemWizWindow", " 14"))
        self.label_group15.setText(_translate("chemWizWindow", " 15"))
        self.label_group16.setText(_translate("chemWizWindow", " 16"))
        self.label_group17.setText(_translate("chemWizWindow", " 17"))
        self.label_group18.setText(_translate("chemWizWindow", " 18"))
        self.periodicTableTitle.setText(_translate("chemWizWindow", "Periodic Table of Elements"))
        self.label_lanthanides.setText(_translate("chemWizWindow", "  57-71"))
        self.label_actinides.setText(_translate("chemWizWindow", " 89-103"))
        self.balancerTitle.setText(_translate("chemWizWindow", "Chemical Equation Balancer"))
        self.balancerSubTitle.setText(_translate("chemWizWindow", "Input a chemical equation to get its balanced equation."))
        self.balancer_sample.setText(_translate("chemWizWindow", "Example: [H]2 + [O]2 -> [H]2[O]1"))
        self.lineEdit_equationInput.setPlaceholderText(_translate("chemWizWindow", "Enter chemical equation here"))
        self.label_equation.setText(_translate("chemWizWindow", "Equation"))
        self.label_instruction1.setText(_translate("chemWizWindow", "• Enclose the element in brackets '[ ]'  and its number beside it."))
        self.label_instruction2.setText(_translate("chemWizWindow", "• Separate the reactants and products using an arrow '->'."))
        self.label_balancedEquation.setText(_translate("chemWizWindow", "Balanced Equation"))
        self.label_underline.setText(_translate("chemWizWindow", "______________________________________________________"))
        self.pushButton_balance.setText(_translate("chemWizWindow", "Balance"))
        self.pushButton_clear.setText(_translate("chemWizWindow", "Clear"))
        self.creditsTitle.setText(_translate("chemWizWindow", "Credits"))
        self.label_Freepik.setText(_translate("chemWizWindow", "<a href=\"https://www.flaticon.com/authors/freepik\">Freepik</a>"))
        self.label_FreepikSub.setText(_translate("chemWizWindow", "for the Chemistry icons used in this project."))
        self.label_ChernykhSub.setText(_translate("chemWizWindow", "for the data used in the Periodic Table of Elements."))
        self.label_Chernykh.setText(_translate("chemWizWindow", "<a href=\"https://chernykh.tech\">Chernykh.tech</a>"))
        self.label_SyntheticProg.setText(_translate("chemWizWindow", "<a href=\"https://www.syntheticprogramming.com\">Synthetic Programming</a>"))
        self.label_SyntheticProgSub.setText(_translate("chemWizWindow", "for the code and guidance in the Chemical Equation Balancer."))


import assets_rc


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = chemWiz()
    ui.show()
    sys.exit(app.exec_())
