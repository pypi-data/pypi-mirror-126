# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parsec/core/gui/forms/settings_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.resize(583, 430)
        SettingsWidget.setMinimumSize(QtCore.QSize(400, 300))
        SettingsWidget.setStyleSheet("#SettingsWidget {\n"
"    background-color: #F4F4F4;\n"
"}\n"
"\n"
"#scrollArea {\n"
"    background-color: #F4F4F4;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(SettingsWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 549, 563))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(30, 20, 30, 20)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_behavior = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_behavior.setObjectName("widget_behavior")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_behavior)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_behavior)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.check_box_tray = QtWidgets.QCheckBox(self.widget_behavior)
        self.check_box_tray.setObjectName("check_box_tray")
        self.verticalLayout_4.addWidget(self.check_box_tray)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addWidget(self.widget_behavior)
        self.widget_locale = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_locale.setObjectName("widget_locale")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_locale)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget_locale)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.widget_locale)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.combo_languages = ComboBox(self.widget_locale)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_languages.sizePolicy().hasHeightForWidth())
        self.combo_languages.setSizePolicy(sizePolicy)
        self.combo_languages.setMinimumSize(QtCore.QSize(0, 32))
        self.combo_languages.setObjectName("combo_languages")
        self.horizontalLayout_9.addWidget(self.combo_languages)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_2.addWidget(self.widget_locale)
        self.widget_version = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_version.setObjectName("widget_version")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_version)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_version)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_box_check_at_startup = QtWidgets.QCheckBox(self.widget_version)
        self.check_box_check_at_startup.setObjectName("check_box_check_at_startup")
        self.horizontalLayout_2.addWidget(self.check_box_check_at_startup)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_check_version = QtWidgets.QPushButton(self.widget_version)
        self.button_check_version.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_check_version.setFont(font)
        self.button_check_version.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_check_version.setStyleSheet("")
        self.button_check_version.setObjectName("button_check_version")
        self.horizontalLayout_4.addWidget(self.button_check_version)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addWidget(self.widget_version)
        self.widget_error_reporting = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_error_reporting.setObjectName("widget_error_reporting")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_error_reporting)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_error_reporting)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.check_box_send_data = QtWidgets.QCheckBox(self.widget_error_reporting)
        self.check_box_send_data.setObjectName("check_box_send_data")
        self.horizontalLayout_7.addWidget(self.check_box_send_data)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.widget_error_reporting)
        self.widget_interface = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_interface.setObjectName("widget_interface")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_interface)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.widget_interface)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.check_box_show_confined = QtWidgets.QCheckBox(self.widget_interface)
        self.check_box_show_confined.setObjectName("check_box_show_confined")
        self.horizontalLayout_12.addWidget(self.check_box_show_confined)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.check_box_workspace_color = QtWidgets.QCheckBox(self.widget_interface)
        self.check_box_workspace_color.setObjectName("check_box_workspace_color")
        self.horizontalLayout_11.addWidget(self.check_box_workspace_color)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addWidget(self.widget_interface)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.button_save = QtWidgets.QPushButton(SettingsWidget)
        self.button_save.setMinimumSize(QtCore.QSize(0, 0))
        self.button_save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_save.setStyleSheet("")
        self.button_save.setIconSize(QtCore.QSize(16, 16))
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_5.addWidget(self.button_save)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def retranslateUi(self, SettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingsWidget.setWindowTitle(_translate("SettingsWidget", "Form"))
        self.label_4.setText(_translate("SettingsWidget", "TEXT_SETTINGS_BEHAVIOR_TITLE"))
        self.check_box_tray.setText(_translate("SettingsWidget", "TEXT_SETTINGS_CHECK_MINIMIZE_IN_TRAY"))
        self.label_8.setText(_translate("SettingsWidget", "TEXT_SETTINGS_LOCALIZATION_TITLE"))
        self.label_10.setText(_translate("SettingsWidget", "TEXT_LABEL_LANGUAGE"))
        self.label_2.setText(_translate("SettingsWidget", "TEXT_SETTINGS_VERSION_TITLE"))
        self.check_box_check_at_startup.setText(_translate("SettingsWidget", "TEXT_SETTINGS_CHECK_NEW_VERSION_ON_STARTUP"))
        self.button_check_version.setText(_translate("SettingsWidget", "ACTION_SETTINGS_CHECK_NEW_VERSION"))
        self.label_5.setText(_translate("SettingsWidget", "TEXT_SETTINGS_TELEMETRY_TITLE"))
        self.check_box_send_data.setText(_translate("SettingsWidget", "TEXT_SETTINGS_ENABLE_TELEMETRY"))
        self.label_11.setText(_translate("SettingsWidget", "TEXT_SETTINGS_INTERFACE_TITLE"))
        self.check_box_show_confined.setText(_translate("SettingsWidget", "TEXT_SETTINGS_CHECK_SHOW_CONFINED_FILES"))
        self.check_box_workspace_color.setText(_translate("SettingsWidget", "TEXT_SETTINGS_CHECK_USE_WORKSPACES_COLORS"))
        self.button_save.setText(_translate("SettingsWidget", "ACTION_SAVE"))
from parsec.core.gui.custom_widgets import ComboBox
