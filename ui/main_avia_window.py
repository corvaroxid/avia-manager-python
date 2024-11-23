# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_avia_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 705)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balances_frame = QFrame(self.centralwidget)
        self.balances_frame.setObjectName(u"balances_frame")
        self.balances_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.balances_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.balances_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_flights = QLabel(self.balances_frame)
        self.lbl_flights.setObjectName(u"lbl_flights")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbl_flights.setFont(font1)
        self.lbl_flights.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_21.addWidget(self.lbl_flights)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_from = QLabel(self.balances_frame)
        self.lbl_from.setObjectName(u"lbl_from")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.lbl_from.setFont(font2)
        self.lbl_from.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_from.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lbl_from)

        self.le_from = QLineEdit(self.balances_frame)
        self.le_from.setObjectName(u"le_from")

        self.horizontalLayout_9.addWidget(self.le_from)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_to = QLabel(self.balances_frame)
        self.lbl_to.setObjectName(u"lbl_to")
        self.lbl_to.setFont(font2)
        self.lbl_to.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-right: 10pt;")

        self.horizontalLayout_10.addWidget(self.lbl_to)

        self.le_to = QLineEdit(self.balances_frame)
        self.le_to.setObjectName(u"le_to")

        self.horizontalLayout_10.addWidget(self.le_to)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.btn_search_flights = QPushButton(self.balances_frame)
        self.btn_search_flights.setObjectName(u"btn_search_flights")
        self.btn_search_flights.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_search_flights)


        self.horizontalLayout_2.addWidget(self.balances_frame)

        self.balances_frame_2 = QFrame(self.centralwidget)
        self.balances_frame_2.setObjectName(u"balances_frame_2")
        self.balances_frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.balances_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.balances_frame_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 12, 12, 12)
        self.lbl_airports = QLabel(self.balances_frame_2)
        self.lbl_airports.setObjectName(u"lbl_airports")
        self.lbl_airports.setFont(font1)
        self.lbl_airports.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_20.addWidget(self.lbl_airports)

        self.lbl_latitude = QLabel(self.balances_frame_2)
        self.lbl_latitude.setObjectName(u"lbl_latitude")

        self.verticalLayout_20.addWidget(self.lbl_latitude)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_min_lat = QLabel(self.balances_frame_2)
        self.icon_min_lat.setObjectName(u"icon_min_lat")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_min_lat.sizePolicy().hasHeightForWidth())
        self.icon_min_lat.setSizePolicy(sizePolicy)
        self.icon_min_lat.setMaximumSize(QSize(24, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.icon_min_lat.setFont(font3)
        self.icon_min_lat.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_min_lat.setPixmap(QPixmap(u":/icons/icons/edit_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icon_min_lat)

        self.lbl_min_lat = QLabel(self.balances_frame_2)
        self.lbl_min_lat.setObjectName(u"lbl_min_lat")
        self.lbl_min_lat.setFont(font3)
        self.lbl_min_lat.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lbl_min_lat)

        self.le_min_lat = QLineEdit(self.balances_frame_2)
        self.le_min_lat.setObjectName(u"le_min_lat")

        self.horizontalLayout_3.addWidget(self.le_min_lat)


        self.verticalLayout_20.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_max_lat = QLabel(self.balances_frame_2)
        self.icon_max_lat.setObjectName(u"icon_max_lat")
        self.icon_max_lat.setMaximumSize(QSize(24, 16777215))
        self.icon_max_lat.setFont(font3)
        self.icon_max_lat.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_max_lat.setPixmap(QPixmap(u":/icons/icons/edit_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.icon_max_lat)

        self.lbl_max_lat = QLabel(self.balances_frame_2)
        self.lbl_max_lat.setObjectName(u"lbl_max_lat")
        self.lbl_max_lat.setFont(font3)
        self.lbl_max_lat.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lbl_max_lat)

        self.le_max_lat = QLineEdit(self.balances_frame_2)
        self.le_max_lat.setObjectName(u"le_max_lat")

        self.horizontalLayout_4.addWidget(self.le_max_lat)


        self.verticalLayout_20.addLayout(self.horizontalLayout_4)

        self.lbl_longitude = QLabel(self.balances_frame_2)
        self.lbl_longitude.setObjectName(u"lbl_longitude")

        self.verticalLayout_20.addWidget(self.lbl_longitude)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_min_long = QLabel(self.balances_frame_2)
        self.icon_min_long.setObjectName(u"icon_min_long")
        self.icon_min_long.setMaximumSize(QSize(24, 16777215))
        self.icon_min_long.setFont(font3)
        self.icon_min_long.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_min_long.setPixmap(QPixmap(u":/icons/icons/edit_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.icon_min_long)

        self.lbl_min_long = QLabel(self.balances_frame_2)
        self.lbl_min_long.setObjectName(u"lbl_min_long")
        self.lbl_min_long.setFont(font3)
        self.lbl_min_long.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lbl_min_long)

        self.le_min_long = QLineEdit(self.balances_frame_2)
        self.le_min_long.setObjectName(u"le_min_long")

        self.horizontalLayout_5.addWidget(self.le_min_long)


        self.verticalLayout_20.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_max_long = QLabel(self.balances_frame_2)
        self.icon_max_long.setObjectName(u"icon_max_long")
        self.icon_max_long.setMaximumSize(QSize(24, 16777215))
        self.icon_max_long.setFont(font3)
        self.icon_max_long.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_max_long.setPixmap(QPixmap(u":/icons/icons/edit_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icon_max_long)

        self.lbl_max_long = QLabel(self.balances_frame_2)
        self.lbl_max_long.setObjectName(u"lbl_max_long")
        self.lbl_max_long.setFont(font3)
        self.lbl_max_long.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.lbl_max_long)

        self.le_max_long = QLineEdit(self.balances_frame_2)
        self.le_max_long.setObjectName(u"le_max_long")

        self.horizontalLayout_6.addWidget(self.le_max_long)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.airport_search = QPushButton(self.balances_frame_2)
        self.airport_search.setObjectName(u"airport_search")
        self.airport_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_7.addWidget(self.airport_search)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_2.addWidget(self.balances_frame_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.rb_airports = QRadioButton(self.centralwidget)
        self.rb_airports.setObjectName(u"rb_airports")
        self.rb_airports.setChecked(True)

        self.verticalLayout_2.addWidget(self.rb_airports)

        self.rb_flights = QRadioButton(self.centralwidget)
        self.rb_flights.setObjectName(u"rb_flights")

        self.verticalLayout_2.addWidget(self.rb_flights)

        self.btn_frame = QFrame(self.centralwidget)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_transaction = QPushButton(self.btn_frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        font4 = QFont()
        font4.setFamilies([u"Noto Sans SC"])
        font4.setBold(True)
        self.btn_new_transaction.setFont(font4)
        self.btn_new_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_new_transaction)

        self.btn_edit_transaction = QPushButton(self.btn_frame)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setMinimumSize(QSize(230, 50))
        self.btn_edit_transaction.setFont(font4)
        self.btn_edit_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_edit_transaction)

        self.btn_delete_transaction = QPushButton(self.btn_frame)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setMinimumSize(QSize(230, 50))
        self.btn_delete_transaction.setFont(font4)
        self.btn_delete_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_transaction.setIcon(icon2)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_transaction)


        self.verticalLayout_2.addWidget(self.btn_frame)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableView.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(155)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Avia Manager", None))
        self.lbl_flights.setText(QCoreApplication.translate("MainWindow", u"Flights", None))
        self.lbl_from.setText(QCoreApplication.translate("MainWindow", u"FROM", None))
        self.lbl_to.setText(QCoreApplication.translate("MainWindow", u"TO", None))
        self.btn_search_flights.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lbl_airports.setText(QCoreApplication.translate("MainWindow", u"Airports", None))
        self.lbl_latitude.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.icon_min_lat.setText("")
        self.lbl_min_lat.setText(QCoreApplication.translate("MainWindow", u"MIN", None))
        self.icon_max_lat.setText("")
        self.lbl_max_lat.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.lbl_longitude.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.icon_min_long.setText("")
        self.lbl_min_long.setText(QCoreApplication.translate("MainWindow", u"MIN", None))
        self.icon_max_long.setText("")
        self.lbl_max_long.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.airport_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.rb_airports.setText(QCoreApplication.translate("MainWindow", u"Airports", None))
        self.rb_flights.setText(QCoreApplication.translate("MainWindow", u"Flights", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

