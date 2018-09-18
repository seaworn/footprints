# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/product_form.ui'
#
# Created: Sun Aug 26 15:58:38 2018
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProductForm(object):
    def setupUi(self, ProductForm):
        ProductForm.setObjectName("ProductForm")
        ProductForm.resize(506, 292)
        ProductForm.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ProductForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(ProductForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.percent_rb = QtGui.QRadioButton(self.groupBox)
        self.percent_rb.setChecked(True)
        self.percent_rb.setObjectName("percent_rb")
        self.horizontalLayout.addWidget(self.percent_rb)
        self.absolute_rb = QtGui.QRadioButton(self.groupBox)
        self.absolute_rb.setObjectName("absolute_rb")
        self.horizontalLayout.addWidget(self.absolute_rb)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 3, 1, 1)
        self.name_le = QtGui.QLineEdit(self.groupBox)
        self.name_le.setObjectName("name_le")
        self.gridLayout.addWidget(self.name_le, 0, 1, 1, 3)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.price_le = QtGui.QLineEdit(self.groupBox)
        self.price_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price_le.setObjectName("price_le")
        self.gridLayout.addWidget(self.price_le, 2, 3, 1, 1)
        self.sku_le = QtGui.QLineEdit(self.groupBox)
        self.sku_le.setObjectName("sku_le")
        self.gridLayout.addWidget(self.sku_le, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.profit_le = QtGui.QLineEdit(self.groupBox)
        self.profit_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profit_le.setObjectName("profit_le")
        self.gridLayout.addWidget(self.profit_le, 3, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.category_cb = QtGui.QComboBox(self.groupBox)
        self.category_cb.setObjectName("category_cb")
        self.gridLayout.addWidget(self.category_cb, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.cost_le = QtGui.QLineEdit(self.groupBox)
        self.cost_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cost_le.setObjectName("cost_le")
        self.gridLayout.addWidget(self.cost_le, 1, 3, 1, 1)
        self.units_sb = QtGui.QSpinBox(self.groupBox)
        self.units_sb.setObjectName("units_sb")
        self.gridLayout.addWidget(self.units_sb, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.description_te = QtGui.QTextEdit(self.groupBox)
        self.description_te.setObjectName("description_te")
        self.gridLayout.addWidget(self.description_te, 5, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ProductForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label_5.setBuddy(self.price_le)
        self.label.setBuddy(self.name_le)
        self.label_4.setBuddy(self.sku_le)
        self.label_8.setBuddy(self.profit_le)
        self.label_6.setBuddy(self.category_cb)
        self.label_2.setBuddy(self.cost_le)
        self.label_3.setBuddy(self.units_sb)
        self.label_7.setBuddy(self.description_te)

        self.retranslateUi(ProductForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProductForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProductForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ProductForm)
        ProductForm.setTabOrder(self.name_le, self.sku_le)
        ProductForm.setTabOrder(self.sku_le, self.category_cb)
        ProductForm.setTabOrder(self.category_cb, self.units_sb)
        ProductForm.setTabOrder(self.units_sb, self.cost_le)
        ProductForm.setTabOrder(self.cost_le, self.price_le)
        ProductForm.setTabOrder(self.price_le, self.percent_rb)
        ProductForm.setTabOrder(self.percent_rb, self.absolute_rb)
        ProductForm.setTabOrder(self.absolute_rb, self.profit_le)
        ProductForm.setTabOrder(self.profit_le, self.description_te)
        ProductForm.setTabOrder(self.description_te, self.buttonBox)

    def retranslateUi(self, ProductForm):
        ProductForm.setWindowTitle(QtGui.QApplication.translate("ProductForm", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProductForm", "Add new product", None, QtGui.QApplication.UnicodeUTF8))
        self.percent_rb.setText(QtGui.QApplication.translate("ProductForm", "P&ercent", None, QtGui.QApplication.UnicodeUTF8))
        self.absolute_rb.setText(QtGui.QApplication.translate("ProductForm", "M&onetary", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProductForm", "Unit &Price :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductForm", "&Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.price_le.setPlaceholderText(QtGui.QApplication.translate("ProductForm", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ProductForm", "&SKU :", None, QtGui.QApplication.UnicodeUTF8))
        self.profit_le.setPlaceholderText(QtGui.QApplication.translate("ProductForm", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ProductForm", "Profit &Margin :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProductForm", "C&ategory :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProductForm", "Unit &Cost :", None, QtGui.QApplication.UnicodeUTF8))
        self.cost_le.setPlaceholderText(QtGui.QApplication.translate("ProductForm", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProductForm", "Un&its :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ProductForm", "&Description :", None, QtGui.QApplication.UnicodeUTF8))

