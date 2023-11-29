from PyQt5 import QtCore, QtGui, QtWidgets

import modules.annotation_dataset as ann
import modules.dataset_aloin as aloin
import modules.dataset_random as ran
import modules.next as nx
import os
import shutil

class Ui_MainWindow(object):

        def setupUi(self, MainWindow):
                
                global one, two, three, four, five, first, second, threering, fourty, fivety, dataset

                # print("Введи путь к датасету: ")

                # dataset = str(input())

                dataset = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, 'Select Folder')

                # print(dataset)

                try:
                    ann.annotation_dataset(dataset, "data_base/ann.csv")
                except:
                    print(dataset)
                    print(" Выход ")
                    exit()

                one = nx.ClassIterator("data_base/ann.csv", "1")
                two = nx.ClassIterator("data_base/ann.csv", "2")
                three = nx.ClassIterator("data_base/ann.csv", "3")
                four = nx.ClassIterator("data_base/ann.csv", "4")
                five = nx.ClassIterator("data_base/ann.csv", "5")

                first = False
                second = False
                threering = False
                fourty = False
                fivety = False

                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1200, 800)
                MainWindow.setStyleSheet("background-color: rgb(58, 58, 58);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.name = QtWidgets.QLabel(self.centralwidget)
                self.name.setGeometry(QtCore.QRect(0, 0, 1200, 100))
                font = QtGui.QFont()
                font.setFamily("Purisa")
                font.setPointSize(25)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.name.setFont(font)
                self.name.setStyleSheet("background-color: rgb(31, 31, 31);\n"
                                        "color: rgb(225, 178, 72);")
                self.name.setScaledContents(True)
                self.name.setAlignment(QtCore.Qt.AlignCenter)
                self.name.setWordWrap(True)
                self.name.setObjectName("name")
                self.star_1 = QtWidgets.QPushButton(self.centralwidget)
                self.star_1.setGeometry(QtCore.QRect(1050, 380, 150, 140))
                font = QtGui.QFont()
                font.setFamily("D050000L")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.star_1.setFont(font)
                self.star_1.setStyleSheet("background-color: rgb(40, 40, 40);\n"
                                          "color: rgb(225, 178, 72);")
                self.star_1.setObjectName("star_1")
                self.star_2 = QtWidgets.QPushButton(self.centralwidget)
                self.star_2.setGeometry(QtCore.QRect(1050, 520, 150, 140))
                font = QtGui.QFont()
                font.setFamily("D050000L")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.star_2.setFont(font)
                self.star_2.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.star_2.setObjectName("star_2")
                self.star_4 = QtWidgets.QPushButton(self.centralwidget)
                self.star_4.setGeometry(QtCore.QRect(1050, 240, 150, 140))
                font = QtGui.QFont()
                font.setFamily("D050000L")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.star_4.setFont(font)
                self.star_4.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.star_4.setObjectName("star_4")
                self.star_5 = QtWidgets.QPushButton(self.centralwidget)
                self.star_5.setGeometry(QtCore.QRect(1050, 100, 150, 140))
                font = QtGui.QFont()
                font.setFamily("D050000L")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.star_5.setFont(font)
                self.star_5.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.star_5.setObjectName("star_5")
                self.star_3 = QtWidgets.QPushButton(self.centralwidget)
                self.star_3.setGeometry(QtCore.QRect(1050, 660, 150, 140))
                font = QtGui.QFont()
                font.setFamily("D050000L")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.star_3.setFont(font)
                self.star_3.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.star_3.setObjectName("star_3")
                self.random = QtWidgets.QPushButton(self.centralwidget)
                self.random.setGeometry(QtCore.QRect(670, 720, 381, 80))
                font = QtGui.QFont()
                font.setFamily("Purisa")
                font.setPointSize(15)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.random.setFont(font)
                self.random.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.random.setObjectName("random")
                self.original = QtWidgets.QPushButton(self.centralwidget)
                self.original.setGeometry(QtCore.QRect(0, 720, 331, 80))
                font = QtGui.QFont()
                font.setFamily("Purisa")
                font.setPointSize(15)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.original.setFont(font)
                self.original.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.original.setObjectName("original")
                self.aloin = QtWidgets.QPushButton(self.centralwidget)
                self.aloin.setGeometry(QtCore.QRect(330, 720, 341, 80))
                font = QtGui.QFont()
                font.setFamily("Purisa")
                font.setPointSize(15)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.aloin.setFont(font)
                self.aloin.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(225, 178, 72);")
                self.aloin.setObjectName("aloin")
                self.rewievs = QtWidgets.QLabel(self.centralwidget)
                self.rewievs.setGeometry(QtCore.QRect(0, 100, 1051, 621))
                font = QtGui.QFont()
                font.setFamily("Purisa")
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.rewievs.setFont(font)
                self.rewievs.setAutoFillBackground(False)
                self.rewievs.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"color: rgb(225, 178, 72);")
                self.rewievs.setTextFormat(QtCore.Qt.AutoText)
                self.rewievs.setScaledContents(True)
                self.rewievs.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                self.rewievs.setWordWrap(True)
                self.rewievs.setOpenExternalLinks(False)
                self.rewievs.setObjectName("rewievs")
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.add_functions()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.name.setText(_translate("MainWindow", "//App"))
                self.star_1.setText(_translate("MainWindow", "444"))
                self.star_2.setText(_translate("MainWindow", "4444"))
                self.star_4.setText(_translate("MainWindow", "44"))
                self.star_5.setText(_translate("MainWindow", "4"))
                self.star_3.setText(_translate("MainWindow", "44444"))
                self.random.setText(_translate("MainWindow", "random"))
                self.original.setText(_translate("MainWindow", "original"))
                self.aloin.setText(_translate("MainWindow", "all on in"))
                self.rewievs.setText(_translate("MainWindow", "Сделай что-то"))

        def add_functions(self):
            self.original.clicked.connect( lambda: self.original_click() )
            self.random.clicked.connect( lambda: self.random_click() )
            self.aloin.clicked.connect( lambda: self.aloin_click() )

            self.star_5.clicked.connect( lambda: self.one_click() )
            self.star_4.clicked.connect( lambda: self.two_click() )
            self.star_1.clicked.connect(lambda: self.three_click() )
            self.star_2.clicked.connect(lambda: self.four_click() )
            self.star_3.clicked.connect(lambda: self.five_click() )



        def one_click(self):
               
            global one, first

            if first:
                try:
                    next( one )
                except:
                      first = False
            else:
                  first = True

            with open(one.getRel(), "r") as file:
                
                text = file.read()
            
            self.rewievs.setText( text )
        
        def two_click(self):
               
            global two, second

            if second:
                try:
                    next( two )
                except:
                      second = False
            else:
                  second = True

            with open(two.getRel(), "r") as file:
                
                text = file.read()
            
            self.rewievs.setText( text )

        def three_click(self):
               
            global three, threering

            if threering:
                try:
                    next( three )
                except:
                      threering = False
            else:
                  threering = True

            with open(three.getRel(), "r") as file:
                
                text = file.read()
            
            self.rewievs.setText( text )


        def four_click(self):
            global four, fourty

            if fourty:
                try:
                    next( four )
                except:
                      fourty = False
            else:
                  fourty = True

            with open(four.getRel(), "r") as file:
                
                text = file.read()
            
            self.rewievs.setText( text )


        def five_click(self):
            global five, fivety

            if fivety:
                try:
                    next( five )
                except:
                      fivety = False
            else:
                  fivety = True

            with open(five.getRel(), "r") as file:
                
                text = file.read()
            
            self.rewievs.setText( text )

        def original_click(self):
            
            global one, two, three, four, five, first, second, threering, fourty, fivety

            first = False
            second = False
            threering = False
            fourty = False
            fivety = False

            ann.annotation_dataset(dataset, "data_base/ann.csv")
            one = nx.ClassIterator("data_base/ann.csv", "1")
            two = nx.ClassIterator("data_base/ann.csv", "2")
            three = nx.ClassIterator("data_base/ann.csv", "3")
            four = nx.ClassIterator("data_base/ann.csv", "4")
            five = nx.ClassIterator("data_base/ann.csv", "5")

        def random_click(self):
            
            global one, two, three, four, five, first, second, threering, fourty, fivety

            first = False
            second = False
            threering = False
            fourty = False
            fivety = False

            try:
                ran.dataset_random_annotation(dataset, "data_base/ran.csv")
            except:
                shutil.rmtree(dataset + ".random")
                os.remove("data_base/ran.csv")
                ran.dataset_random_annotation(dataset, "data_base/ran.csv")

            one = nx.ClassIterator("data_base/ran.csv", "1")
            two = nx.ClassIterator("data_base/ran.csv", "2")
            three = nx.ClassIterator("data_base/ran.csv", "3")
            four = nx.ClassIterator("data_base/ran.csv", "4")
            five = nx.ClassIterator("data_base/ran.csv", "5")

        def random_click(self):
            
            global one, two, three, four, five, first, second, threering, fourty, fivety

            first = False
            second = False
            threering = False
            fourty = False
            fivety = False

            try:
                ran.dataset_random_annotation(dataset, "data_base/ran.csv")
            except:
                shutil.rmtree(dataset + ".random")
                os.remove("data_base/ran.csv")
                ran.dataset_random_annotation(dataset, "data_base/ran.csv")

            one = nx.ClassIterator("data_base/ran.csv", "1")
            two = nx.ClassIterator("data_base/ran.csv", "2")
            three = nx.ClassIterator("data_base/ran.csv", "3")
            four = nx.ClassIterator("data_base/ran.csv", "4")
            five = nx.ClassIterator("data_base/ran.csv", "5")

        def aloin_click(self):
            
            global one, two, three, four, five, first, second, threering, fourty, fivety

            first = False
            second = False
            threering = False
            fourty = False
            fivety = False

            try:
                aloin.dataset_aloin(dataset)
                aloin.annotation_aloin(dataset + ".aloin", "data_base/aloin.csv")
            except:
                shutil.rmtree(dataset + ".aloin")
                os.remove("data_base/aloin.csv")
                aloin.dataset_aloin(dataset)
                aloin.annotation_aloin(dataset + ".aloin", "data_base/aloin.csv")
                
            one = nx.ClassIterator("data_base/aloin.csv", "1")
            two = nx.ClassIterator("data_base/aloin.csv", "2")
            three = nx.ClassIterator("data_base/aloin.csv", "3")
            four = nx.ClassIterator("data_base/aloin.csv", "4")
            five = nx.ClassIterator("data_base/aloin.csv", "5")

                

                
if __name__ == "__main__":
        
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
