# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripts/gui/multibootusb.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(644, 516)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_persistence_value = QtWidgets.QLabel(self.tab_3)
        self.label_persistence_value.setObjectName("label_persistence_value")
        self.gridLayout.addWidget(self.label_persistence_value, 5, 2, 1, 1)
        self.labelstep3 = QtWidgets.QLabel(self.tab_3)
        self.labelstep3.setObjectName("labelstep3")
        self.gridLayout.addWidget(self.labelstep3, 5, 5, 1, 1)
        self.slider_persistence = QtWidgets.QSlider(self.tab_3)
        self.slider_persistence.setEnabled(False)
        self.slider_persistence.setAutoFillBackground(False)
        self.slider_persistence.setOrientation(QtCore.Qt.Horizontal)
        self.slider_persistence.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider_persistence.setTickInterval(0)
        self.slider_persistence.setObjectName("slider_persistence")
        self.gridLayout.addWidget(self.slider_persistence, 5, 1, 1, 1)
        self.close = QtWidgets.QPushButton(self.tab_3)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 5, 3, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.detect_usb = QtWidgets.QPushButton(self.groupBox_11)
        self.detect_usb.setObjectName("detect_usb")
        self.horizontalLayout_8.addWidget(self.detect_usb)
        self.verticalLayout_11.addWidget(self.groupBox_11)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 3, 1, 2)
        self.labelstep1 = QtWidgets.QLabel(self.tab_3)
        self.labelstep1.setObjectName("labelstep1")
        self.gridLayout.addWidget(self.labelstep1, 0, 5, 1, 1)
        self.labelstep2 = QtWidgets.QLabel(self.tab_3)
        self.labelstep2.setObjectName("labelstep2")
        self.gridLayout.addWidget(self.labelstep2, 4, 5, 1, 1)
        self.create = QtWidgets.QPushButton(self.tab_3)
        self.create.setObjectName("create")
        self.gridLayout.addWidget(self.create, 5, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uninstall = QtWidgets.QPushButton(self.groupBox)
        self.uninstall.setObjectName("uninstall")
        self.gridLayout_5.addWidget(self.uninstall, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout.addWidget(self.groupBox, 3, 3, 1, 2)
        self.browse_iso = QtWidgets.QPushButton(self.tab_3)
        self.browse_iso.setObjectName("browse_iso")
        self.gridLayout.addWidget(self.browse_iso, 4, 4, 1, 1)
        self.label_persistence = QtWidgets.QLabel(self.tab_3)
        self.label_persistence.setObjectName("label_persistence")
        self.gridLayout.addWidget(self.label_persistence, 5, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 4, 3)
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 6)
        self.status = QtWidgets.QLabel(self.tab_3)
        self.status.setMinimumSize(QtCore.QSize(0, 0))
        self.status.setAcceptDrops(False)
        self.status.setAutoFillBackground(False)
        self.status.setFrameShadow(QtWidgets.QFrame.Plain)
        self.status.setText("")
        self.status.setScaledContents(False)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 6, 0, 1, 6)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.usb_dev = QtWidgets.QLabel(self.groupBox_6)
        self.usb_dev.setObjectName("usb_dev")
        self.verticalLayout_5.addWidget(self.usb_dev)
        self.usb_vendor = QtWidgets.QLabel(self.groupBox_6)
        self.usb_vendor.setObjectName("usb_vendor")
        self.verticalLayout_5.addWidget(self.usb_vendor)
        self.usb_model = QtWidgets.QLabel(self.groupBox_6)
        self.usb_model.setObjectName("usb_model")
        self.verticalLayout_5.addWidget(self.usb_model)
        self.usb_size = QtWidgets.QLabel(self.groupBox_6)
        self.usb_size.setObjectName("usb_size")
        self.verticalLayout_5.addWidget(self.usb_size)
        self.usb_mount = QtWidgets.QLabel(self.groupBox_6)
        self.usb_mount.setObjectName("usb_mount")
        self.verticalLayout_5.addWidget(self.usb_mount)
        self.gridLayout.addWidget(self.groupBox_6, 2, 3, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, "")
        self.imager = QtWidgets.QWidget()
        self.imager.setObjectName("imager")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.imager)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.imager)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_8.addWidget(self.comboBox_2)
        self.pushbtn_imager_refreshusb = QtWidgets.QPushButton(self.groupBox_9)
        self.pushbtn_imager_refreshusb.setObjectName("pushbtn_imager_refreshusb")
        self.verticalLayout_8.addWidget(self.pushbtn_imager_refreshusb)
        self.imager_disk_label = QtWidgets.QLabel(self.groupBox_9)
        self.imager_disk_label.setObjectName("imager_disk_label")
        self.verticalLayout_8.addWidget(self.imager_disk_label)
        self.imager_total_size = QtWidgets.QLabel(self.groupBox_9)
        self.imager_total_size.setObjectName("imager_total_size")
        self.verticalLayout_8.addWidget(self.imager_total_size)
        self.imager_uuid = QtWidgets.QLabel(self.groupBox_9)
        self.imager_uuid.setObjectName("imager_uuid")
        self.verticalLayout_8.addWidget(self.imager_uuid)
        self.gridLayout_11.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_9.addWidget(self.lineEdit_3)
        self.imager_bootable = QtWidgets.QLabel(self.groupBox_10)
        self.imager_bootable.setObjectName("imager_bootable")
        self.verticalLayout_9.addWidget(self.imager_bootable)
        self.imager_iso_size = QtWidgets.QLabel(self.groupBox_10)
        self.imager_iso_size.setObjectName("imager_iso_size")
        self.verticalLayout_9.addWidget(self.imager_iso_size)
        self.gridLayout_11.addWidget(self.groupBox_10, 0, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_11)
        self.gridLayout_9.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.imager)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.imager_label_status = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imager_label_status.sizePolicy().hasHeightForWidth())
        self.imager_label_status.setSizePolicy(sizePolicy)
        self.imager_label_status.setText("")
        self.imager_label_status.setObjectName("imager_label_status")
        self.verticalLayout_7.addWidget(self.imager_label_status)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.imager_write = QtWidgets.QPushButton(self.groupBox_8)
        self.imager_write.setObjectName("imager_write")
        self.gridLayout_12.addWidget(self.imager_write, 2, 2, 1, 1)
        self.imager_close = QtWidgets.QPushButton(self.groupBox_8)
        self.imager_close.setObjectName("imager_close")
        self.gridLayout_12.addWidget(self.imager_close, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 1, 0, 1, 3)
        self.imager_progressbar = QtWidgets.QProgressBar(self.groupBox_8)
        self.imager_progressbar.setProperty("value", 0)
        self.imager_progressbar.setObjectName("imager_progressbar")
        self.gridLayout_12.addWidget(self.imager_progressbar, 0, 0, 1, 3)
        self.verticalLayout_7.addLayout(self.gridLayout_12)
        self.gridLayout_9.addWidget(self.groupBox_8, 2, 0, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.imager, "")
        self.syslinux_ab = QtWidgets.QWidget()
        self.syslinux_ab.setObjectName("syslinux_ab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.syslinux_ab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.syslinux_ab)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.install_syslinux = QtWidgets.QPushButton(self.groupBox_2)
        self.install_syslinux.setObjectName("install_syslinux")
        self.gridLayout_3.addWidget(self.install_syslinux, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.install_sys_all = QtWidgets.QRadioButton(self.groupBox_2)
        self.install_sys_all.setObjectName("install_sys_all")
        self.gridLayout_3.addWidget(self.install_sys_all, 1, 0, 1, 2)
        self.install_sys_only = QtWidgets.QRadioButton(self.groupBox_2)
        self.install_sys_only.setObjectName("install_sys_only")
        self.gridLayout_3.addWidget(self.install_sys_only, 0, 0, 1, 2)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.syslinux_ab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.edit_syslinux = QtWidgets.QPushButton(self.groupBox_3)
        self.edit_syslinux.setObjectName("edit_syslinux")
        self.gridLayout_4.addWidget(self.edit_syslinux, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.syslinux_ab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ram_iso_2048 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_2048.setObjectName("ram_iso_2048")
        self.gridLayout_7.addWidget(self.ram_iso_2048, 4, 4, 1, 1)
        self.ram_iso_1024 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_1024.setObjectName("ram_iso_1024")
        self.gridLayout_7.addWidget(self.ram_iso_1024, 4, 3, 1, 1)
        self.ram_iso_256 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_256.setObjectName("ram_iso_256")
        self.gridLayout_7.addWidget(self.ram_iso_256, 4, 0, 1, 1)
        self.browse_iso_qemu = QtWidgets.QPushButton(self.groupBox_5)
        self.browse_iso_qemu.setObjectName("browse_iso_qemu")
        self.gridLayout_7.addWidget(self.browse_iso_qemu, 2, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 5)
        self.ram_iso_512 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_512.setObjectName("ram_iso_512")
        self.gridLayout_7.addWidget(self.ram_iso_512, 4, 1, 1, 1)
        self.boot_iso_qemu = QtWidgets.QPushButton(self.groupBox_5)
        self.boot_iso_qemu.setObjectName("boot_iso_qemu")
        self.gridLayout_7.addWidget(self.boot_iso_qemu, 6, 4, 1, 1)
        self.ram_iso_768 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_768.setObjectName("ram_iso_768")
        self.gridLayout_7.addWidget(self.ram_iso_768, 4, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_7.addWidget(self.lineEdit_2, 2, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 6, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ram_usb_768 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_768.setObjectName("ram_usb_768")
        self.gridLayout_8.addWidget(self.ram_usb_768, 2, 2, 1, 1)
        self.ram_usb_256 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_256.setObjectName("ram_usb_256")
        self.gridLayout_8.addWidget(self.ram_usb_256, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 5)
        self.ram_usb_1024 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_1024.setObjectName("ram_usb_1024")
        self.gridLayout_8.addWidget(self.ram_usb_1024, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 4, 0, 1, 4)
        self.ram_usb_512 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_512.setObjectName("ram_usb_512")
        self.gridLayout_8.addWidget(self.ram_usb_512, 2, 1, 1, 1)
        self.boot_usb_qemu = QtWidgets.QPushButton(self.groupBox_4)
        self.boot_usb_qemu.setObjectName("boot_usb_qemu")
        self.gridLayout_8.addWidget(self.boot_usb_qemu, 4, 4, 1, 1)
        self.ram_usb_2048 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_2048.setObjectName("ram_usb_2048")
        self.gridLayout_8.addWidget(self.ram_usb_2048, 2, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem8, 5, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem10, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem11, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem12, 1, 2, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_10)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "multibootusb"))
        self.label_persistence_value.setText(_translate("Dialog", "0 MB"))
        self.labelstep3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Step 3</span></p></body></html>"))
        self.slider_persistence.setToolTip(_translate("Dialog", "Choose Persistence size. Not all distros supports persistence..."))
        self.close.setText(_translate("Dialog", "Close"))
        self.groupBox_11.setTitle(_translate("Dialog", "Detect USB"))
        self.detect_usb.setText(_translate("Dialog", "Refresh USB"))
        self.labelstep1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Step 1</span></p></body></html>"))
        self.labelstep2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Step 2</span></p></body></html>"))
        self.create.setText(_translate("Dialog", "Create"))
        self.groupBox.setTitle(_translate("Dialog", "Uninstall (Optional)"))
        self.uninstall.setText(_translate("Dialog", "Uninstall Distro"))
        self.browse_iso.setText(_translate("Dialog", "Browse ISO"))
        self.label_persistence.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Persistence</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("Dialog", "USB Details"))
        self.usb_dev.setText(_translate("Dialog", "Drive ::"))
        self.usb_vendor.setText(_translate("Dialog", "Vendor ::"))
        self.usb_model.setText(_translate("Dialog", "Model::"))
        self.usb_size.setText(_translate("Dialog", "Size ::"))
        self.usb_mount.setText(_translate("Dialog", "Mount ::"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "MultiBootUSB"))
        self.groupBox_7.setTitle(_translate("Dialog", "Imager"))
        self.groupBox_9.setTitle(_translate("Dialog", "--------------  USB details  -------------------"))
        self.pushbtn_imager_refreshusb.setText(_translate("Dialog", "Refresh USB"))
        self.imager_disk_label.setText(_translate("Dialog", "Disk Label ::"))
        self.imager_total_size.setText(_translate("Dialog", "Disk Size"))
        self.imager_uuid.setText(_translate("Dialog", "Disk Label ::"))
        self.groupBox_10.setTitle(_translate("Dialog", "------------------------------  ISO details  ----------------------------------"))
        self.pushButton.setText(_translate("Dialog", "Browse ISO"))
        self.imager_bootable.setText(_translate("Dialog", "Bootable ISO"))
        self.imager_iso_size.setText(_translate("Dialog", "ISO Size"))
        self.groupBox_8.setTitle(_translate("Dialog", "Imager Progress"))
        self.imager_write.setText(_translate("Dialog", "Write/Create"))
        self.imager_close.setText(_translate("Dialog", "Close"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">WARNING</span> : Any bootable USB made using<span style=\" font-weight:600;\"> ISO Imager will destroy all data </span>on the selected USB disk. </p><p>Use it at your own risk. Developers are not responsile for loss of any data.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imager), _translate("Dialog", "ISO Imager"))
        self.groupBox_2.setTitle(_translate("Dialog", "Install Syslinux"))
        self.install_syslinux.setText(_translate("Dialog", "Install"))
        self.install_sys_all.setText(_translate("Dialog", "Install syslinux and copy all required files."))
        self.install_sys_only.setText(_translate("Dialog", "Install only syslinux (existing configurations will not be altred)."))
        self.groupBox_3.setTitle(_translate("Dialog", "Edit syslinux.cfg"))
        self.edit_syslinux.setText(_translate("Dialog", "Edit"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\">Using this option user can edit syslinux.cfg file directly. It directly uses </p><p align=\"justify\">default editor of host system. Be careful while editing syslinux.cfg file.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.syslinux_ab), _translate("Dialog", "Syslinux"))
        self.groupBox_5.setTitle(_translate("Dialog", "Boot ISO"))
        self.ram_iso_2048.setText(_translate("Dialog", "2048 MB"))
        self.ram_iso_1024.setText(_translate("Dialog", "1024 MB"))
        self.ram_iso_256.setText(_translate("Dialog", "256 MB"))
        self.browse_iso_qemu.setText(_translate("Dialog", "Browse ISO"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>Best way to test your downloaded ISOs. </p></body></html>"))
        self.ram_iso_512.setText(_translate("Dialog", "512 MB"))
        self.boot_iso_qemu.setText(_translate("Dialog", "Boot ISO"))
        self.ram_iso_768.setText(_translate("Dialog", "768 MB"))
        self.label_3.setText(_translate("Dialog", "Choose desired RAM and click on Boot ISO button."))
        self.groupBox_4.setTitle(_translate("Dialog", "Boot USB"))
        self.ram_usb_768.setText(_translate("Dialog", "768 MB"))
        self.ram_usb_256.setText(_translate("Dialog", "256 MB"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\">Use this option if you want to check USB installation without reboot.</p></body></html>"))
        self.ram_usb_1024.setText(_translate("Dialog", "1024 MB"))
        self.label_4.setText(_translate("Dialog", "Choose desired RAM and click on Boot USB button."))
        self.ram_usb_512.setText(_translate("Dialog", "512 MB"))
        self.boot_usb_qemu.setText(_translate("Dialog", "Boot USB"))
        self.ram_usb_2048.setText(_translate("Dialog", "2048 MB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "QEMU"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">An advanced bootable usb creator with option to install/uninstall </p><p align=\"center\">multiple distros. This software is written in python and pyqt. </p><p align=\"center\">Copyright 2010-2016 Sundar</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Author(s)</span>: Sundar, Ian Bruce, Lee</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Licence:</span> GPL version 2 or later</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Home page</span>: <a href=\" http://multibootusb.org\"><span style=\" text-decoration: underline; color:#0000ff;\">http://multibootusb.org</span></a></p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Help/Email:</span>  feedback.multibootusb@gmail.com</p><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Source Code:</span><span style=\" font-weight:600;\"/><a href=\"https://github.com/mbusb/multibootusb\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/mbusb/multibootusb</span></a></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

