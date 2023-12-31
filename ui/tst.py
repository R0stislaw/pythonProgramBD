# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(40, 60, 171, 341))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setTabletTracking(False)
        self.listWidget_2.setAutoFillBackground(False)
        self.listWidget_2.setStyleSheet("color: white;\n"
"border-radius: 7px;\n"
"background-color: #2C313C;\n"
"")
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setLineWidth(1)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget_2.setAutoScroll(True)
        self.listWidget_2.setTabKeyNavigation(False)
        self.listWidget_2.setProperty("showDropIndicator", True)
        self.listWidget_2.setDragDropOverwriteMode(False)
        self.listWidget_2.setAlternatingRowColors(False)
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget_2.setMovement(QtWidgets.QListView.Static)
        self.listWidget_2.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_2.setProperty("isWrapping", False)
        self.listWidget_2.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_2.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_2.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_2.setUniformItemSizes(False)
        self.listWidget_2.setWordWrap(False)
        self.listWidget_2.setSelectionRectVisible(False)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget_2.itemClicked.connect(self.on_item_click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.listWidget_2.setSortingEnabled(False)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "New Item1"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "New Item2"))
        item = self.listWidget_2.item(2)
    def on_item_click(self, item):
        QMessageBox.information(None, "Item Clicked", f"Clicked: {item.text()}")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
