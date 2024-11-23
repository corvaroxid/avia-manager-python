# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'airports_modify_modal.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(422, 450)
        Dialog.setStyleSheet(u"font-family: Noto Sans SC;\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_transaction = QFrame(Dialog)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.new_transaction.setFrameShape(QFrame.Shape.NoFrame)
        self.new_transaction.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.new_transaction)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_new_transaction = QLabel(self.new_transaction)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_new_transaction.setFont(font)
        self.lbl_new_transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transaction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lbl_new_transaction)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.new_transaction)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.le_name = QLineEdit(self.new_transaction)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout_21.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.new_transaction)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.le_city = QLineEdit(self.new_transaction)
        self.le_city.setObjectName(u"le_city")

        self.horizontalLayout_2.addWidget(self.le_city)


        self.verticalLayout_21.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.new_transaction)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.le_country = QLineEdit(self.new_transaction)
        self.le_country.setObjectName(u"le_country")

        self.horizontalLayout_3.addWidget(self.le_country)


        self.verticalLayout_21.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.new_transaction)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.le_iata = QLineEdit(self.new_transaction)
        self.le_iata.setObjectName(u"le_iata")

        self.horizontalLayout_4.addWidget(self.le_iata)


        self.verticalLayout_21.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.new_transaction)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.le_icao = QLineEdit(self.new_transaction)
        self.le_icao.setObjectName(u"le_icao")

        self.horizontalLayout_5.addWidget(self.le_icao)


        self.verticalLayout_21.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.new_transaction)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.le_longitude = QLineEdit(self.new_transaction)
        self.le_longitude.setObjectName(u"le_longitude")

        self.horizontalLayout_8.addWidget(self.le_longitude)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.new_transaction)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.le_latitude = QLineEdit(self.new_transaction)
        self.le_latitude.setObjectName(u"le_latitude")

        self.horizontalLayout_7.addWidget(self.le_latitude)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.btn_new_transaction = QPushButton(self.new_transaction)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setBold(True)
        self.btn_new_transaction.setFont(font1)
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

        self.verticalLayout_21.addWidget(self.btn_new_transaction)


        self.verticalLayout.addWidget(self.new_transaction)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"Airports", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Airport name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"     City        ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"  Country     ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"    IATA       ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"    ICAO      ", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"  Longitude ", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"  Latitude    ", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

