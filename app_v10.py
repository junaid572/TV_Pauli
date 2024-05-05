# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designer_V3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

import pyqtgraph as pg
#####
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas)
from matplotlib.figure import Figure

from SCAPE_functions_V2 import fixed_tomography, SCAPE_tomography


#######


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_sim_parameters = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_sim_parameters.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_sim_parameters.setFont(font)
        self.groupBox_sim_parameters.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_sim_parameters.setObjectName("groupBox_sim_parameters")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_sim_parameters)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox_sim_parameters)
        self.splitter.setFrameShape(QtWidgets.QFrame.Panel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(3, 0, 3, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_amplitude = QtWidgets.QLabel(self.layoutWidget)
        self.label_amplitude.setObjectName("label_amplitude")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_amplitude)
        self.SpinBox_amplitude = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.SpinBox_amplitude.setAutoFillBackground(False)
        self.SpinBox_amplitude.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_amplitude.setProperty("showGroupSeparator", False)
        self.SpinBox_amplitude.setDecimals(3)
        self.SpinBox_amplitude.setMaximum(1.0)
        self.SpinBox_amplitude.setSingleStep(0.05)
        self.SpinBox_amplitude.setProperty("value", 0.3)
        self.SpinBox_amplitude.setObjectName("SpinBox_amplitude")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SpinBox_amplitude)
        self.label_bias = QtWidgets.QLabel(self.layoutWidget)
        self.label_bias.setObjectName("label_bias")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_bias)
        self.SpinBox_bias = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.SpinBox_bias.setAutoFillBackground(False)
        self.SpinBox_bias.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_bias.setProperty("showGroupSeparator", False)
        self.SpinBox_bias.setDecimals(3)
        self.SpinBox_bias.setMaximum(1.0)
        self.SpinBox_bias.setSingleStep(0.05)
        self.SpinBox_bias.setProperty("value", 0.7)
        self.SpinBox_bias.setObjectName("SpinBox_bias")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SpinBox_bias)
        self.label_frequency = QtWidgets.QLabel(self.layoutWidget)
        self.label_frequency.setObjectName("label_frequency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_frequency)
        self.SpinBox_frequency = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.SpinBox_frequency.setAutoFillBackground(False)
        self.SpinBox_frequency.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_frequency.setProperty("showGroupSeparator", False)
        self.SpinBox_frequency.setDecimals(3)
        self.SpinBox_frequency.setMinimum(0.1)
        self.SpinBox_frequency.setMaximum(100.0)
        self.SpinBox_frequency.setSingleStep(0.1)
        self.SpinBox_frequency.setProperty("value", 1.0)
        self.SpinBox_frequency.setObjectName("SpinBox_frequency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SpinBox_frequency)
        self.SpinBox_sampling_rate = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.SpinBox_sampling_rate.setAutoFillBackground(False)
        self.SpinBox_sampling_rate.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_sampling_rate.setProperty("showGroupSeparator", False)
        self.SpinBox_sampling_rate.setDecimals(0)
        self.SpinBox_sampling_rate.setMinimum(10.0)
        self.SpinBox_sampling_rate.setMaximum(10000000.0)
        self.SpinBox_sampling_rate.setSingleStep(100.0)
        self.SpinBox_sampling_rate.setProperty("value", 10000.0)
        self.SpinBox_sampling_rate.setObjectName("SpinBox_sampling_rate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SpinBox_sampling_rate)
        self.label_frequency_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_frequency_3.setObjectName("label_frequency_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_frequency_3)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(3, 0, 3, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkBox_adaptive = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_adaptive.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_adaptive.setObjectName("checkBox_adaptive")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.checkBox_adaptive)
        self.label_bias_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_bias_2.setObjectName("label_bias_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_bias_2)
        self.SpinBox_code_rate = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.SpinBox_code_rate.setAutoFillBackground(False)
        self.SpinBox_code_rate.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_code_rate.setProperty("showGroupSeparator", False)
        self.SpinBox_code_rate.setDecimals(0)
        self.SpinBox_code_rate.setMinimum(5.0)
        self.SpinBox_code_rate.setMaximum(131.0)
        self.SpinBox_code_rate.setSingleStep(2.0)
        self.SpinBox_code_rate.setProperty("value", 13.0)
        self.SpinBox_code_rate.setObjectName("SpinBox_code_rate")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SpinBox_code_rate)
        self.SpinBox_adaptive_increment = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.SpinBox_adaptive_increment.setEnabled(False)
        self.SpinBox_adaptive_increment.setAutoFillBackground(False)
        self.SpinBox_adaptive_increment.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_adaptive_increment.setProperty("showGroupSeparator", False)
        self.SpinBox_adaptive_increment.setDecimals(0)
        self.SpinBox_adaptive_increment.setMinimum(2.0)
        self.SpinBox_adaptive_increment.setMaximum(10.0)
        self.SpinBox_adaptive_increment.setSingleStep(2.0)
        self.SpinBox_adaptive_increment.setProperty("value", 4.0)
        self.SpinBox_adaptive_increment.setObjectName("SpinBox_adaptive_increment")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SpinBox_adaptive_increment)
        self.label_bias_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_bias_4.setObjectName("label_bias_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_bias_4)
        self.SpinBox_adaptive_decrement = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.SpinBox_adaptive_decrement.setEnabled(False)
        self.SpinBox_adaptive_decrement.setAutoFillBackground(False)
        self.SpinBox_adaptive_decrement.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_adaptive_decrement.setProperty("showGroupSeparator", False)
        self.SpinBox_adaptive_decrement.setDecimals(0)
        self.SpinBox_adaptive_decrement.setMinimum(2.0)
        self.SpinBox_adaptive_decrement.setMaximum(10.0)
        self.SpinBox_adaptive_decrement.setSingleStep(2.0)
        self.SpinBox_adaptive_decrement.setProperty("value", 2.0)
        self.SpinBox_adaptive_decrement.setObjectName("SpinBox_adaptive_decrement")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SpinBox_adaptive_decrement)
        self.label_bias_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_bias_5.setObjectName("label_bias_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_bias_5)
        self.label_bias_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_bias_6.setObjectName("label_bias_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_bias_6)
        self.SpinBox_target_CRI = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.SpinBox_target_CRI.setEnabled(False)
        self.SpinBox_target_CRI.setAutoFillBackground(False)
        self.SpinBox_target_CRI.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_target_CRI.setProperty("showGroupSeparator", False)
        self.SpinBox_target_CRI.setDecimals(0)
        self.SpinBox_target_CRI.setMinimum(0.0)
        self.SpinBox_target_CRI.setMaximum(20.0)
        self.SpinBox_target_CRI.setSingleStep(1.0)
        self.SpinBox_target_CRI.setProperty("value", 2.0)
        self.SpinBox_target_CRI.setObjectName("SpinBox_target_CRI")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.SpinBox_target_CRI)
        self.label_bias_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_bias_7.setObjectName("label_bias_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_bias_7)
        self.SpinBox_CRI_margin_up = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.SpinBox_CRI_margin_up.setEnabled(False)
        self.SpinBox_CRI_margin_up.setAutoFillBackground(False)
        self.SpinBox_CRI_margin_up.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_CRI_margin_up.setProperty("showGroupSeparator", False)
        self.SpinBox_CRI_margin_up.setDecimals(0)
        self.SpinBox_CRI_margin_up.setMinimum(1.0)
        self.SpinBox_CRI_margin_up.setMaximum(10.0)
        self.SpinBox_CRI_margin_up.setSingleStep(1.0)
        self.SpinBox_CRI_margin_up.setProperty("value", 3.0)
        self.SpinBox_CRI_margin_up.setObjectName("SpinBox_CRI_margin_up")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.SpinBox_CRI_margin_up)
        self.SpinBox_CRI_margin_down = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.SpinBox_CRI_margin_down.setEnabled(False)
        self.SpinBox_CRI_margin_down.setAutoFillBackground(False)
        self.SpinBox_CRI_margin_down.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_CRI_margin_down.setProperty("showGroupSeparator", False)
        self.SpinBox_CRI_margin_down.setDecimals(0)
        self.SpinBox_CRI_margin_down.setMinimum(1.0)
        self.SpinBox_CRI_margin_down.setMaximum(10.0)
        self.SpinBox_CRI_margin_down.setSingleStep(1.0)
        self.SpinBox_CRI_margin_down.setProperty("value", 1.0)
        self.SpinBox_CRI_margin_down.setObjectName("SpinBox_CRI_margin_down")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.SpinBox_CRI_margin_down)
        self.label_bias_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_bias_8.setObjectName("label_bias_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_bias_8)
        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(3, 0, 3, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_amplitude_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_amplitude_2.setObjectName("label_amplitude_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_amplitude_2)
        self.SpinBox_samples_N = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.SpinBox_samples_N.setAutoFillBackground(False)
        self.SpinBox_samples_N.setFrame(True)
        self.SpinBox_samples_N.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_samples_N.setProperty("showGroupSeparator", False)
        self.SpinBox_samples_N.setDecimals(0)
        self.SpinBox_samples_N.setMinimum(150.0)
        self.SpinBox_samples_N.setMaximum(100000.0)
        self.SpinBox_samples_N.setSingleStep(50.0)
        self.SpinBox_samples_N.setProperty("value", 300.0)
        self.SpinBox_samples_N.setObjectName("SpinBox_samples_N")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SpinBox_samples_N)
        #self.label_bias_3 = QtWidgets.QLabel(self.layoutWidget_2)
        #self.label_bias_3.setObjectName("label_bias_3")
        #self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_bias_3)
        # self.SpinBox_averages_M = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        # self.SpinBox_averages_M.setAutoFillBackground(False)
        # self.SpinBox_averages_M.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        # self.SpinBox_averages_M.setProperty("showGroupSeparator", False)
        # self.SpinBox_averages_M.setDecimals(0)
        # self.SpinBox_averages_M.setMinimum(1.0)
        # self.SpinBox_averages_M.setMaximum(100.0)
        # self.SpinBox_averages_M.setSingleStep(1.0)
        # self.SpinBox_averages_M.setProperty("value", 1.0)
        # self.SpinBox_averages_M.setObjectName("SpinBox_averages_M")
        # self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SpinBox_averages_M)
        self.gridLayout_3.addLayout(self.formLayout_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.groupBox_sim_parameters)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_4)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label = QtWidgets.QLabel(self.splitter_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.dial = QtWidgets.QDial(self.splitter_3)
        self.dial.setMinimum(1)
        self.dial.setMaximum(200)
        self.dial.setProperty("value", 10)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(4.7)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.pushButton_stop = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_start = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_clear = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_reset = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout.addWidget(self.splitter_3)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        ###
        # canvas 1: Pauli Paramters
        #############
        styles = {'color': 'r', 'font-size': '12px'}
        self.dynamic_canvas_1 = pg.PlotWidget()
        self.verticalLayout_3.addWidget(self.dynamic_canvas_1)
        self._dynamic_ax_1 = self.dynamic_canvas_1.plot()
        self.dynamic_canvas_1.setBackground((255, 255, 255))  # RGB each 0-255
        self.dynamic_canvas_1.setTitle("Channel Estimation", color="b", size="10pt")

        self.dynamic_canvas_1.setLabel('left', 'Pauli Parameters', **styles)
        self.dynamic_canvas_1.setLabel('bottom', 'Time (s)', **styles)

        ############## canvas 2: DN Distance
        self.dynamic_canvas_2 = pg.PlotWidget()
        self.verticalLayout_3.addWidget(self.dynamic_canvas_2)
        self._dynamic_ax_1 = self.dynamic_canvas_2.plot()
        self.dynamic_canvas_2.setBackground((255, 255, 255))  # RGB each 0-255
        self.dynamic_canvas_2.setTitle("Estimation Error", color="b", size="10pt")

        self.dynamic_canvas_2.setLabel('left', 'DN Distance', **styles)
        self.dynamic_canvas_2.setLabel('bottom', 'Time (s)', **styles)
        ############# canvas 3: Code Rates
        self.dynamic_canvas_3 = pg.PlotWidget()
        self.verticalLayout_3.addWidget(self.dynamic_canvas_3)
        self._dynamic_ax_3 = self.dynamic_canvas_3.plot()
        self.dynamic_canvas_3.setBackground((255, 255, 255))  # RGB each 0-255
        self.dynamic_canvas_3.setTitle("Repetition Rates", color="b", size="10pt")

        self.dynamic_canvas_3.setLabel('left', 'k', **styles)
        self.dynamic_canvas_3.setLabel('bottom', 'Time (s)', **styles)
        #
        ############# canvas 4: Codeword Reliability
        self.dynamic_canvas_4 = pg.PlotWidget()
        self.verticalLayout_3.addWidget(self.dynamic_canvas_4)
        self._dynamic_ax_4 = self.dynamic_canvas_4.plot()
        self.dynamic_canvas_4.setBackground((255, 255, 255))  # RGB each 0-255
        self.dynamic_canvas_4.setTitle("Codeword Reliability", color="b", size="10pt")

        self.dynamic_canvas_4.setLabel('left', 'CRI', **styles)
        self.dynamic_canvas_4.setLabel('bottom', 'Time (s)', **styles)
        #
        ####
        # self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView_2.setObjectName("graphicsView_2")
        # self.verticalLayout_3.addWidget(self.graphicsView_2)
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setObjectName("graphicsView")
        # self.verticalLayout_3.addWidget(self.graphicsView)
        # self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView_4.setObjectName("graphicsView_4")
        # self.verticalLayout_3.addWidget(self.graphicsView_4)
        # self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView_3.setObjectName("graphicsView_3")
        # self.verticalLayout_3.addWidget(self.graphicsView_3)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.splitter_6 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_12 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.widget = QtWidgets.QWidget(self.splitter_4)
        self.widget.setObjectName("widget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_4.setContentsMargins(10, 0, 10, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.spinBox_X = QtWidgets.QSpinBox(self.widget)
        self.spinBox_X.setMinimum(10)
        self.spinBox_X.setMaximum(1000)
        self.spinBox_X.setSingleStep(10)
        self.spinBox_X.setObjectName("spinBox_X")
        self.spinBox_X.setValue(100)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_X)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_dn_error_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_dn_error_1.setEnabled(True)
        self.lineEdit_dn_error_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_dn_error_1.setReadOnly(True)
        self.lineEdit_dn_error_1.setObjectName("lineEdit_dn_error_1")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dn_error_1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_estimation_deviation_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_estimation_deviation_1.setEnabled(True)
        self.lineEdit_estimation_deviation_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_estimation_deviation_1.setReadOnly(True)
        self.lineEdit_estimation_deviation_1.setObjectName("lineEdit_estimation_deviation_1")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_estimation_deviation_1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_capacity_actual_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_capacity_actual_1.setEnabled(True)
        self.lineEdit_capacity_actual_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_capacity_actual_1.setReadOnly(True)
        self.lineEdit_capacity_actual_1.setObjectName("lineEdit_capacity_actual_1")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_capacity_actual_1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_capacity_estimated_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_capacity_estimated_1.setEnabled(True)
        self.lineEdit_capacity_estimated_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_capacity_estimated_1.setReadOnly(True)
        self.lineEdit_capacity_estimated_1.setObjectName("lineEdit_capacity_estimated_1")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_capacity_estimated_1)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.lineEdit_dn_error_time_invariant_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_dn_error_time_invariant_1.setEnabled(True)
        self.lineEdit_dn_error_time_invariant_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_dn_error_time_invariant_1.setReadOnly(True)
        self.lineEdit_dn_error_time_invariant_1.setObjectName("lineEdit_dn_error_time_invariant_1")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dn_error_time_invariant_1)
        self.horizontalLayout_4.addWidget(self.splitter_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_18 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.formLayout_6 = QtWidgets.QFormLayout(self.layoutWidget_3)
        self.formLayout_6.setContentsMargins(10, 0, 10, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.spinBox_Y = QtWidgets.QSpinBox(self.layoutWidget_3)
        self.spinBox_Y.setSuffix("")
        self.spinBox_Y.setMinimum(10)
        self.spinBox_Y.setMaximum(1000)
        self.spinBox_Y.setSingleStep(10)
        self.spinBox_Y.setObjectName("spinBox_Y")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_Y)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_dn_error_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_dn_error_2.setEnabled(True)
        self.lineEdit_dn_error_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_dn_error_2.setReadOnly(True)
        self.lineEdit_dn_error_2.setObjectName("lineEdit_dn_error_2")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dn_error_2)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_estimation_deviation_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_estimation_deviation_2.setEnabled(True)
        self.lineEdit_estimation_deviation_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_estimation_deviation_2.setReadOnly(True)
        self.lineEdit_estimation_deviation_2.setObjectName("lineEdit_estimation_deviation_2")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_estimation_deviation_2)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_capacity_actual_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_capacity_actual_2.setEnabled(True)
        self.lineEdit_capacity_actual_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_capacity_actual_2.setReadOnly(True)
        self.lineEdit_capacity_actual_2.setObjectName("lineEdit_capacity_actual_2")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_capacity_actual_2)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_capacity_estimated_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_capacity_estimated_2.setEnabled(True)
        self.lineEdit_capacity_estimated_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_capacity_estimated_2.setReadOnly(True)
        self.lineEdit_capacity_estimated_2.setObjectName("lineEdit_capacity_estimated_2")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_capacity_estimated_2)
        self.lineEdit_dn_error_time_invariant_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_dn_error_time_invariant_2.setEnabled(True)
        self.lineEdit_dn_error_time_invariant_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_dn_error_time_invariant_2.setReadOnly(True)
        self.lineEdit_dn_error_time_invariant_2.setObjectName("lineEdit_dn_error_time_invariant_2")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dn_error_time_invariant_2)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.horizontalLayout_3.addWidget(self.splitter_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_channel_period = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_channel_period.setEnabled(True)
        self.lineEdit_channel_period.setReadOnly(True)
        self.lineEdit_channel_period.setObjectName("lineEdit_channel_period")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_channel_period)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_estimates_per_period = QtWidgets.QLabel(self.groupBox_4)
        self.label_estimates_per_period.setObjectName("label_estimates_per_period")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_estimates_per_period)
        self.lineEdit_estimation_period = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_estimation_period.setEnabled(True)
        self.lineEdit_estimation_period.setReadOnly(True)
        self.lineEdit_estimation_period.setObjectName("lineEdit_estimation_period")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_estimation_period)
        ####
        self.lineEdit_samples_per_period = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_samples_per_period.setEnabled(True)
        self.lineEdit_samples_per_period.setReadOnly(True)
        self.lineEdit_samples_per_period.setObjectName("lineEdit_samples_per_period")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_samples_per_period)
        ####
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setObjectName("label_25")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.doubleSpinBox_X_2 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_X_2.setDecimals(1)
        self.doubleSpinBox_X_2.setMinimum(0.1)
        self.doubleSpinBox_X_2.setMaximum(10.0)
        self.doubleSpinBox_X_2.setSingleStep(0.2)
        self.doubleSpinBox_X_2.setProperty("value", 2.0)
        self.doubleSpinBox_X_2.setObjectName("doubleSpinBox_X_2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_X_2)
        self.horizontalLayout_5.addLayout(self.formLayout_5)
        #self.horizontalLayout_5.addLayout(self.formLayout_5)
        ########
        self.groupBox_5 = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # canvas 5: Bit Errors
        ############# canvas 4: Codeword Reliability
        self.dynamic_canvas_5 = pg.PlotWidget()
        self.verticalLayout_2.addWidget(self.dynamic_canvas_5)
        self._dynamic_ax_5 = self.dynamic_canvas_4.plot()
        self.dynamic_canvas_5.setBackground((255, 255, 255))  # RGB each 0-255
        self.dynamic_canvas_5.setTitle("Communication Errors", color="b", size="10pt")
        self.dynamic_canvas_5.setLabel('left', 'BER', **styles)
        self.dynamic_canvas_5.setLabel('bottom', 'Time (s)', **styles)
        ########
        self.dynamic_canvas_1.showGrid(x=True, y=True)
        self.dynamic_canvas_2.showGrid(x=True, y=True)
        self.dynamic_canvas_3.showGrid(x=True, y=True)
        self.dynamic_canvas_4.showGrid(x=True, y=True)
        self.dynamic_canvas_5.showGrid(x=True, y=True)
        #self.groupBox_5 = QtWidgets.QGroupBox(self.splitter_6)
        #self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        #self.groupBox_5.setObjectName("groupBox_5")
        #self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        #self.verticalLayout_2.setObjectName("verticalLayout_2")
        #self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.label_19.setFont(font)
        #self.label_19.setObjectName("label_19")
        #self.verticalLayout_2.addWidget(self.label_19)
        #self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        #self.label_20.setObjectName("label_20")
        #self.verticalLayout_2.addWidget(self.label_20)
        #self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        #self.label_21.setObjectName("label_21")
        #self.verticalLayout_2.addWidget(self.label_21)
        #self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        #self.label_22.setObjectName("label_22")
        #self.verticalLayout_2.addWidget(self.label_22)
        self.gridLayout_4.addWidget(self.splitter_6, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.SpinBox_amplitude.valueChanged['double'].connect(self.SpinBox_bias.setValue)
        #self.SpinBox_bias.valueChanged['double'].connect(self.SpinBox_amplitude.setValue)
        self.checkBox_adaptive.clicked['bool'].connect(self.SpinBox_code_rate.setDisabled)
        self.checkBox_adaptive.clicked['bool'].connect(self.SpinBox_CRI_margin_down.setEnabled)
        self.checkBox_adaptive.clicked['bool'].connect(self.SpinBox_CRI_margin_up.setEnabled)
        self.checkBox_adaptive.clicked['bool'].connect(self.SpinBox_adaptive_decrement.setEnabled)
        self.checkBox_adaptive.clicked['bool'].connect(self.SpinBox_adaptive_increment.setEnabled)
        self.checkBox_adaptive.clicked['bool'].connect(self.SpinBox_target_CRI.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##### Custom code start here
        #self.pushButton_start.setCheckable(True)
        #self.pushButton_stop.setCheckable(True)
        self.lineEdit_channel_period.setText("1.000 seconds")
        self.lineEdit_estimation_period.setText("0.030 seconds")
        self.lineEdit_samples_per_period.setText("33.333")

        self.SpinBox_frequency.valueChanged.connect(self._freq_changed)
        self.SpinBox_sampling_rate.valueChanged.connect(self._sampling_changed)
        self.SpinBox_samples_N.valueChanged.connect(self._samples_changed)
        self.doubleSpinBox_X_2.valueChanged.connect(self._display_changed)

        self.SpinBox_amplitude.valueChanged.connect(self._amp_validation)
        self.SpinBox_bias.valueChanged.connect(self._bias_validation)

        self.SpinBox_adaptive_increment.valueChanged.connect(self._increment_changed)
        self.SpinBox_adaptive_decrement.valueChanged.connect(self._decrement_changed)


        self.pushButton_start.clicked.connect(self._start_clicked)
        self.pushButton_stop.clicked.connect(self._stop_clicked)
        self.pushButton_clear.clicked.connect(self._clear_clicked)
        self.pushButton_reset.clicked.connect(self._reset_clicked)
        self.pushButton_stop.setEnabled(False)


        self.simulation_running = False
        self.simulation_data1 = []
        self.simulation_data2 = []
        self.simulation_time = [0]
        self.estimates_time = [0]
        self.ch_estimates = []
        self.DN_fixed = []
        self.ch_actual = []
        self.DN_SCAPE = []
        self.CRI = []
        self.k_vals = []
        self.bit_errors = []
        self.history_Error_fixed = []
        self.history_Error_adaptive = []
        self.history_capacity_actual = []
        self.history_capacity_estimated = []
        self.history_differential = []
        self._line_1 = None
        self._line_2 = None
        self._line_3 = None
        self._line_4 = None
        self._line_5 = None
        self._line_6 = None
        self._line_7 = None
        self._line_8 = None
        self._line_9 = None
        self._line_10 = None
        self._line_11 = None
        self._line_12 = None
        self._line_13 = None
        self._line_14 = None
        self._line_15 = None
        self._line_16 = None
        self._line_17 = None
        self._line_18 = None
        self._line_19 = None
        self.config_change = True
        self.counter_gen = 0
        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adaptive SCAPE"))
        self.groupBox_sim_parameters.setTitle(_translate("MainWindow", "Simulation Parameters"))
        self.label_amplitude.setText(_translate("MainWindow", "Amplitude (a)"))
        self.label_bias.setText(_translate("MainWindow", "Bias (b)"))
        self.label_frequency.setText(_translate("MainWindow", "Frequency (f)"))
        self.SpinBox_frequency.setSuffix(_translate("MainWindow", " Hz"))
        self.SpinBox_sampling_rate.setSuffix(_translate("MainWindow", " Hz"))
        self.label_frequency_3.setText(_translate("MainWindow", "Sampling Rate"))
        self.label_2.setText(_translate("MainWindow", "Channel"))
        self.label_3.setText(_translate("MainWindow", "Code"))
        self.checkBox_adaptive.setText(_translate("MainWindow", "Adaptive Rate  "))
        self.label_bias_2.setText(_translate("MainWindow", "Repetition Rate"))
        self.label_bias_4.setText(_translate("MainWindow", "Adaptive Increment"))
        self.label_bias_5.setText(_translate("MainWindow", "Adaptive Decrement"))
        self.label_bias_6.setText(_translate("MainWindow", "Target CRI"))
        self.label_bias_7.setText(_translate("MainWindow", "CRI Margin Up"))
        self.label_bias_8.setText(_translate("MainWindow", "CRI Margin Down"))
        self.label_amplitude_2.setText(_translate("MainWindow", "Number of Samples (N)"))
        #self.label_bias_3.setText(_translate("MainWindow", "Number of Averages (M)"))
        self.label_4.setText(_translate("MainWindow", "Estimation"))
        self.groupBox.setTitle(_translate("MainWindow", "Simulation Control"))
        self.label.setText(_translate("MainWindow", "Simulation Speed (delay in ms)"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop Simulation"))
        self.pushButton_start.setText(_translate("MainWindow", "Start Simulation"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear All Data"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset to Defaults"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Moving Averag Over X Estimates"))
        self.label_12.setText(_translate("MainWindow", "Average 1"))
        self.label_11.setText(_translate("MainWindow", "X"))
        self.spinBox_X.setSuffix(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "Error"))
        self.lineEdit_dn_error_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Estimate Deviation"))
        self.lineEdit_estimation_deviation_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Capacity (actual)"))
        self.lineEdit_capacity_actual_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Capacity (estimated)"))
        self.lineEdit_capacity_estimated_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "Error (time-invariant)"))
        self.lineEdit_dn_error_time_invariant_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Moving Averag Over Y Estimates"))
        self.label_18.setText(_translate("MainWindow", "Average 2"))
        self.label_13.setText(_translate("MainWindow", "Y"))
        self.label_14.setText(_translate("MainWindow", "Error"))
        self.lineEdit_dn_error_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "Estimate Deviation"))
        self.lineEdit_estimation_deviation_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Capacity (actual)"))
        self.lineEdit_capacity_actual_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Capacity (estimated)"))
        self.lineEdit_capacity_estimated_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_dn_error_time_invariant_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "Error (time-invariant)"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Time Scales"))
        self.label_5.setText(_translate("MainWindow", "Channel Period (T)"))
        self.lineEdit_channel_period.setPlaceholderText(_translate("MainWindow", "seconds"))
        self.label_6.setText(_translate("MainWindow", "Estimation Period"))
        self.label_estimates_per_period.setText(_translate("MainWindow", "Estimates per period"))
        self.lineEdit_estimation_period.setPlaceholderText(_translate("MainWindow", "seconds"))
        self.label_25.setText(_translate("MainWindow", "Display Width (T units)"))
        #self.groupBox_5.setTitle(_translate("MainWindow", "COPYRIGHT"))
        #self.label_19.setText(_translate("MainWindow", "Junaid ur Rehman"))
        #self.label_20.setText(_translate("MainWindow", "junaid.urrehman@uni.lu"))
        #self.label_21.setText(_translate("MainWindow", "SigCom-SnT"))
        #self.label_22.setText(_translate("MainWindow", "University of Luxembourg"))

    def _increment_changed(self):
        val = self.SpinBox_adaptive_increment.value()
        self.SpinBox_adaptive_increment.setValue(val + val % 2)

    def _decrement_changed(self):
        val = self.SpinBox_adaptive_decrement.value()
        self.SpinBox_adaptive_decrement.setValue(val + val % 2)

    def _freq_changed(self):
        sampling_rate = self.SpinBox_sampling_rate.value()
        sample_N = self.SpinBox_samples_N.value()
        freq = self.SpinBox_frequency.value()
        self.lineEdit_channel_period.setText("{:.3f}".format(1/freq) + " seconds")
        self.lineEdit_samples_per_period.setText("{:.3f}".format(sampling_rate / (freq * sample_N)))
        self.config_change = True

    def _sampling_changed(self):
        sampling_rate = self.SpinBox_sampling_rate.value()
        sample_N = self.SpinBox_samples_N.value()
        freq = self.SpinBox_frequency.value()
        self.lineEdit_estimation_period.setText("{:.3f}".format(sample_N/sampling_rate) + " seconds")
        #self.lineEdit_samples_per_period.setText("{:.3f}".format(sampling_rate/sample_N))
        self.lineEdit_samples_per_period.setText("{:.3f}".format(sampling_rate / (freq * sample_N)))
        self.config_change = True

    def _samples_changed(self):
        sampling_rate = self.SpinBox_sampling_rate.value()
        sample_N = self.SpinBox_samples_N.value()
        freq = self.SpinBox_frequency.value()
        self.lineEdit_estimation_period.setText("{:.3f}".format(sample_N/sampling_rate)  + " seconds")
        self.lineEdit_samples_per_period.setText("{:.3f}".format(sampling_rate / (freq * sample_N)))
        self.config_change = True

    def _display_changed(self):
        self.config_change = True

    def _amp_validation(self):
        self.config_change = True
        bias = self.SpinBox_bias.value()
        amplitude = self.SpinBox_amplitude.value()
        if bias + amplitude > 1:
            self.SpinBox_bias.setValue(1 - amplitude)

    def _bias_validation(self):
        self.config_change = True
        bias = self.SpinBox_bias.value()
        amplitude = self.SpinBox_amplitude.value()
        if bias + amplitude > 1:
            self.SpinBox_amplitude.setValue(1 - bias)

    #@QtCore.pyqtSlot()
    def _start_clicked(self):
        if not self.simulation_running:
            self.simulation_running = True
            self.pushButton_start.setEnabled(False)
            self.pushButton_clear.setEnabled(False)
            self.pushButton_reset.setEnabled(False)
            self.pushButton_stop.setEnabled(True)
            self.dial.setEnabled(False)
            delay = self.dial.value()
            print("delay: ", delay)
            #self.timer = self.dynamic_canvas_1.new_timer(interval=1000/(0.01 + delay))
            #self.timer.add_callback(self.update_simulation)
            #self.timer.start()
            self.timer = QtCore.QTimer()
            self.timer.setInterval(delay)
            self.timer.timeout.connect(self.update_simulation)
            self.timer.start()

    def update_simulation(self):
        if self.simulation_running:
            #M = int(self.SpinBox_averages_M.value())
            self.counter_gen += 1
            N_tomo = int(self.SpinBox_samples_N.value())
            freq = self.SpinBox_frequency.value()
            k = 3*[int(self.SpinBox_code_rate.value())]
            bias = self.SpinBox_bias.value()
            amplitude = self.SpinBox_amplitude.value()
            sample_rate = self.SpinBox_sampling_rate.value()
            phase = np.mod(np.pi*2*freq*self.estimates_time[-1], 2*np.pi)

            ## fixed channel
            new_data1 = fixed_tomography(N_tomo, freq, k, bias, amplitude, sample_rate, phase)
            DN_distance_t = new_data1[2]
            self.DN_fixed.append(DN_distance_t)



            if self.checkBox_adaptive.isChecked():
                ## Adaptove SCAPE
                if len(self.k_vals) > 0:
                    k_previous = self.k_vals[-1]
                    CRI_previous = self.CRI[-1]
                    #X
                    if CRI_previous[0] < self.SpinBox_target_CRI.value()-self.SpinBox_CRI_margin_down.value():
                        k_x = k_previous[0] + self.SpinBox_adaptive_increment.value()
                    elif CRI_previous[0] > self.SpinBox_target_CRI.value()+self.SpinBox_CRI_margin_up.value():
                        k_x = k_previous[0] - self.SpinBox_adaptive_decrement.value()
                    else:
                        k_x = k_previous[0]

                    # Y
                    if CRI_previous[1] < self.SpinBox_target_CRI.value() - self.SpinBox_CRI_margin_down.value():
                        k_y = k_previous[1] + self.SpinBox_adaptive_increment.value()
                    elif CRI_previous[1] > self.SpinBox_target_CRI.value() + self.SpinBox_CRI_margin_up.value():
                        k_y = k_previous[1] - self.SpinBox_adaptive_decrement.value()
                    else:
                        k_y = k_previous[1]

                    # Z
                    if CRI_previous[2] < self.SpinBox_target_CRI.value() - self.SpinBox_CRI_margin_down.value():
                        k_z = k_previous[2] + self.SpinBox_adaptive_increment.value()
                    elif CRI_previous[2] > self.SpinBox_target_CRI.value() + self.SpinBox_CRI_margin_up.value():
                        k_z = k_previous[2] - self.SpinBox_adaptive_decrement.value()
                    else:
                        k_z = k_previous[2]

                    if k_x > np.floor(N_tomo/3):
                        k_x = (int(np.floor(N_tomo/3)) & ~1) - 1

                    if k_y > np.floor(N_tomo / 3):
                        k_y = (int(np.floor(N_tomo/3)) & ~1) - 1

                    if k_z > np.floor(N_tomo/3):
                        #print("disaster averted Z")
                        k_z = (int(np.floor(N_tomo/3)) & ~1) - 1
                    k = [int(k_x), int(k_y), int(k_z)]
                    #print(k, np.floor(N_tomo / 3))
                else:
                    k = 3 * [int(self.SpinBox_code_rate.value())]

                data_SCAPE = SCAPE_tomography(N_tomo, freq, k, bias, amplitude, sample_rate, phase)
                self.k_vals.append(k)

            else:
                ## Fixed SCAPE
                self.k_vals.append(3 * [int(self.SpinBox_code_rate.value())])
                data_SCAPE = SCAPE_tomography(N_tomo, freq, k, bias, amplitude, sample_rate, phase)


            self.estimates_time.append(self.estimates_time[-1] + N_tomo/sample_rate)
            self.simulation_time += np.linspace(self.estimates_time[-2], self.estimates_time[-1], N_tomo).tolist()

            ch_estimates_t = data_SCAPE[0]
            ch_original_t = data_SCAPE[1]
            DN_distance_t = data_SCAPE[2]
            CRI_t = data_SCAPE[3]
            err_t = data_SCAPE[4]
            #print(new_data1)

            # new_data1 = np.random.rand(10)  # Replace with your simulation function
            #new_data2 = np.random.rand(10)  # Replace with your simulation function
            self.ch_estimates.append(ch_estimates_t)
            self.ch_actual += ch_original_t
            self.DN_SCAPE.append(DN_distance_t)
            self.CRI.append(CRI_t)
            self.bit_errors.append(err_t)

            #keeping 1000 historical values
            self.history_Error_fixed.append(self.DN_fixed[-1])
            self.history_Error_adaptive.append(self.DN_SCAPE[-1])
            ch = [np.min([1, np.abs(pp)+0.000001]) for pp in ch_estimates_t]
            vals = [np.min([1, ch[0] + ch[1]]), \
                    np.min([1, ch[0] + ch[2]]), \
                    np.min([1, ch[0] + ch[3]])]
            cap = np.max([1 + pp*np.log2(pp) + (1.000001-pp)*np.log2(1.000001-pp) \
                          for pp in vals])
            #print(vals, cap)
            self.history_capacity_estimated.append(cap)
            ch = [np.min([1, np.abs(pp)+0.000001]) for pp in ch_original_t[-1]]
            vals = [np.min([1, ch[0] + ch[1]]), \
                    np.min([1, ch[0] + ch[2]]), \
                    np.min([1, ch[0] + ch[3]])]
            cap = np.max([1 + pp*np.log2(pp) + (1.000001-pp)*np.log2(1.000001-pp) \
                          for pp in vals])
            self.history_capacity_actual.append(cap)
            #print(cap)
            if len(self.history_differential) == 0:
                self.history_differential.append(0)
            else:
                dev = np.sum(np.abs(np.array(self.ch_estimates[-1]) - np.array(self.ch_estimates[-2])))
                self.history_differential.append(dev)

            if len(self.history_Error_fixed) > 1000:
                self.history_Error_fixed = self.history_Error_fixed[-1000:]
                self.history_Error_adaptive = self.history_Error_adaptive[-1000:]
                self.history_differential = self.history_differential[-1000:]
                self.history_capacity_estimated = self.history_capacity_estimated[-1000:]
                self.history_capacity_actual = self.history_capacity_actual[-1000:]


            #
            #print(np.linspace(self.estimates_time[-2], self.estimates_time[-1], N_tomo))
            #print(len(self.simulation_time[1:]))
            #print(self.ch_actual)
            #
            plot_width = self.doubleSpinBox_X_2.value()
            if len(self.estimates_time) > plot_width*sample_rate/(freq*N_tomo):
                retained_samples = int(np.round(plot_width*sample_rate/(freq*N_tomo)))
                self.estimates_time = self.estimates_time[-(retained_samples+2):]
                self.ch_estimates = self.ch_estimates[-(retained_samples+1):]

                self.simulation_time = self.simulation_time[-(N_tomo*retained_samples+2):]
                self.ch_actual = self.ch_actual[-(N_tomo*retained_samples+1):]

                self.DN_fixed = self.DN_fixed[-(retained_samples + 1):]
                self.DN_SCAPE = self.DN_SCAPE[-(retained_samples + 1):]
                self.CRI = self.CRI[-(retained_samples + 1):]
                self.k_vals = self.k_vals[-(retained_samples + 1):]
                self.bit_errors = self.bit_errors[-(retained_samples + 1):]




            X_avg = self.spinBox_X.value()
            err_X_fix = np.mean(self.history_Error_fixed[-X_avg:])
            self.lineEdit_dn_error_time_invariant_1.setText("{:.3f}".format(err_X_fix))
            err_X_SCAPE = np.mean(self.history_Error_adaptive[-X_avg:])
            self.lineEdit_dn_error_1.setText("{:.3f}".format(err_X_SCAPE))
            est_dev = np.mean(self.history_differential[-X_avg:])
            self.lineEdit_estimation_deviation_1.setText("{:.3f}".format(est_dev))
            cap_est = np.mean(self.history_capacity_estimated[-X_avg:])
            self.lineEdit_capacity_estimated_1.setText("{:.3f}".format(cap_est))
            cap_act = np.mean(self.history_capacity_actual[-X_avg:])
            self.lineEdit_capacity_actual_1.setText("{:.3f}".format(cap_act))

            # averages over Y
            X_avg = self.spinBox_Y.value()
            err_X_fix = np.mean(self.history_Error_fixed[-X_avg:])
            self.lineEdit_dn_error_time_invariant_2.setText("{:.3f}".format(err_X_fix))
            err_X_SCAPE = np.mean(self.history_Error_adaptive[-X_avg:])
            self.lineEdit_dn_error_2.setText("{:.3f}".format(err_X_SCAPE))
            est_dev = np.mean(self.history_differential[-X_avg:])
            self.lineEdit_estimation_deviation_2.setText("{:.3f}".format(est_dev))
            cap_est = np.mean(self.history_capacity_estimated[-X_avg:])
            self.lineEdit_capacity_estimated_2.setText("{:.3f}".format(cap_est))
            cap_act = np.mean(self.history_capacity_actual[-X_avg:])
            self.lineEdit_capacity_actual_2.setText("{:.3f}".format(cap_act))

            redraw = 15
            #print(len(self.estimates_time) != int(np.round(plot_width*sample_rate/(freq*N_tomo)))+2, self.config_change, self.counter_gen%redraw == 0)

            if len(self.estimates_time) < 4: #self._line_1 is None:
                #print("if if if")

                self.dynamic_canvas_1.clear()
                self.dynamic_canvas_2.clear()
                self.dynamic_canvas_3.clear()
                self.dynamic_canvas_4.clear()
                self.dynamic_canvas_5.clear()
                
                


                # Estimates
                # penRD = pg.mkPen(color=(255, 0, 0), width=3, style=QtCore.Qt.DashLine)
                # penRS = pg.mkPen(color=(255, 0, 0), style=QtCore.Qt.SolidLine, width = 3)
                # penBD = pg.mkPen(color=(0, 0, 255), width=3, style=QtCore.Qt.DashLine)
                # penBS = pg.mkPen(color=(0, 0, 255), width=3, style=QtCore.Qt.SolidLine)
                # penGD = pg.mkPen(color=(46, 139, 87), width=3, style=QtCore.Qt.DashLine)
                # penGS = pg.mkPen(color=(46, 139, 87), width=3, style=QtCore.Qt.SolidLine)
                # penKD = pg.mkPen(color=(0, 0, 0), width=3, style=QtCore.Qt.DashLine)
                # penKS = pg.mkPen(color=(0, 0, 0), width=3, style=QtCore.Qt.SolidLine)
                
                penRD = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.DashLine)
                penRS = pg.mkPen(color=(255, 0, 0), style=QtCore.Qt.SolidLine, width = 1)
                penBD = pg.mkPen(color=(0, 0, 255), width=2, style=QtCore.Qt.DashLine)
                penBS = pg.mkPen(color=(0, 0, 255), width=1, style=QtCore.Qt.SolidLine)
                penGD = pg.mkPen(color=(46, 139, 87), width=2, style=QtCore.Qt.DashLine)
                penGS = pg.mkPen(color=(46, 139, 87), width=1, style=QtCore.Qt.SolidLine)
                penKD = pg.mkPen(color=(0, 0, 0), width=2, style=QtCore.Qt.DashLine)
                penKS = pg.mkPen(color=(0, 0, 0), width=1, style=QtCore.Qt.SolidLine)
                
                self._line_1 = self.dynamic_canvas_1.plot(self.estimates_time[1:], [L[0] for L in self.ch_estimates], pen = penKD, name = "Estimated")
                self._line_2 = self.dynamic_canvas_1.plot(self.estimates_time[1:], [L[1] for L in self.ch_estimates], pen = penRD)
                self._line_3 = self.dynamic_canvas_1.plot(self.estimates_time[1:], [L[2] for L in self.ch_estimates], pen = penBD)
                self._line_4 = self.dynamic_canvas_1.plot(self.estimates_time[1:], [L[3] for L in self.ch_estimates], pen = penGD)

                # # Actual
                self._line_5 = self.dynamic_canvas_1.plot(self.simulation_time[1:], [L[0] for L in self.ch_actual], pen = penKS, name = "Actual")
                self._line_6 = self.dynamic_canvas_1.plot(self.simulation_time[1:], [L[1] for L in self.ch_actual], pen = penRS)
                self._line_7 = self.dynamic_canvas_1.plot(self.simulation_time[1:], [L[2] for L in self.ch_actual], pen = penBS)
                self._line_8 = self.dynamic_canvas_1.plot(self.simulation_time[1:], [L[3] for L in self.ch_actual], pen = penGS)

                self.dynamic_canvas_1.addLegend(brush=pg.mkBrush(255, 255, 255, 190), offset = (2,2))


                self._line_9 = self.dynamic_canvas_2.plot(self.estimates_time[1:], self.DN_fixed, pen = penRD, name = "Fixed Channel")
                self._line_10 = self.dynamic_canvas_2.plot(self.estimates_time[1:], self.DN_SCAPE, pen = penBD, name = "SCAPE")
                self.dynamic_canvas_2.addLegend(brush=pg.mkBrush(255, 255, 255, 190), offset=(2, 2))
                # #
                self._line_11 = self.dynamic_canvas_3.plot(self.estimates_time[1:], [L[0] for L in self.k_vals], pen = penRD, name = "k_X")
                self._line_12 = self.dynamic_canvas_3.plot(self.estimates_time[1:], [L[1] for L in self.k_vals], pen = penBD, name = "k_Y")
                self._line_13 = self.dynamic_canvas_3.plot(self.estimates_time[1:], [L[2] for L in self.k_vals], pen = penGD, name = "k_Z")
                self.dynamic_canvas_3.addLegend(brush=pg.mkBrush(255, 255, 255, 190), offset=(2, 2))
                # #
                self._line_14 = self.dynamic_canvas_4.plot(self.estimates_time[1:], [L[0] for L in self.CRI], pen = penRD, name = "CRI_X")
                self._line_15 = self.dynamic_canvas_4.plot(self.estimates_time[1:], [L[1] for L in self.CRI], pen = penBD, name = "CRI_Y")
                self._line_16 = self.dynamic_canvas_4.plot(self.estimates_time[1:], [L[2] for L in self.CRI], pen = penGD, name = "CRI_Z")
                self.dynamic_canvas_4.addLegend(brush=pg.mkBrush(255, 255, 255, 190), offset=(2, 2))
                # #
                self._line_17 = self.dynamic_canvas_5.plot(self.estimates_time[1:], [L[0] for L in self.bit_errors], pen = penRD, name = "e_X")
                self._line_18 = self.dynamic_canvas_5.plot(self.estimates_time[1:], [L[1] for L in self.bit_errors], pen = penBD, name = "e_Y")
                self._line_19 = self.dynamic_canvas_5.plot(self.estimates_time[1:], [L[2] for L in self.bit_errors], pen = penGD, name = "e_Z")
                self.dynamic_canvas_5.addLegend(brush=pg.mkBrush(255, 255, 255, 190), offset=(2, 2))
                
                #self.counter_gen +=1
                




            else:
                # print("if if if")
                #time.sleep(0.5)
                self._line_1.setData(self.estimates_time[1:], [L[0] for L in self.ch_estimates], name = "Estimated")
                self._line_2.setData(self.estimates_time[1:], [L[1] for L in self.ch_estimates])
                self._line_3.setData(self.estimates_time[1:], [L[2] for L in self.ch_estimates])
                self._line_4.setData(self.estimates_time[1:], [L[3] for L in self.ch_estimates])
                self._line_5.setData(self.simulation_time[1:], [L[0] for L in self.ch_actual])
                self._line_6.setData(self.simulation_time[1:], [L[1] for L in self.ch_actual])
                self._line_7.setData(self.simulation_time[1:], [L[2] for L in self.ch_actual])
                self._line_8.setData(self.simulation_time[1:], [L[3] for L in self.ch_actual])
                # self._line_1.figure.canvas.draw()
                #
                self._line_9.setData(self.estimates_time[1:], self.DN_fixed)
                self._line_10.setData(self.estimates_time[1:], self.DN_SCAPE)
                # self._line_10.figure.canvas.draw()
                #self.dynamic_canvas_1.addLegend(brush=pg.mkBrush(255, 255, 255, 190))
                #
                self._line_11.setData(self.estimates_time[1:], [L[0] for L in self.k_vals])
                self._line_12.setData(self.estimates_time[1:], [L[1] for L in self.k_vals])
                self._line_13.setData(self.estimates_time[1:], [L[2] for L in self.k_vals])
                # self._line_11.figure.canvas.draw()
                #
                self._line_14.setData(self.estimates_time[1:], [L[0] for L in self.CRI])
                self._line_15.setData(self.estimates_time[1:], [L[1] for L in self.CRI])
                self._line_16.setData(self.estimates_time[1:], [L[2] for L in self.CRI])
                # self._line_14.figure.canvas.draw()
                #
                self._line_17.setData(self.estimates_time[1:], [L[0] for L in self.bit_errors])
                self._line_18.setData(self.estimates_time[1:], [L[1] for L in self.bit_errors])
                self._line_19.setData(self.estimates_time[1:], [L[2] for L in self.bit_errors])
                # self._line_17.figure.canvas.draw()


    #@QtCore.pyqtSlot()
    def _stop_clicked(self):
        if self.simulation_running:
            self.simulation_running = False
            self.pushButton_start.setEnabled(True)
            self.pushButton_clear.setEnabled(True)
            self.pushButton_reset.setEnabled(True)
            self.pushButton_stop.setEnabled(False)
            self.dial.setEnabled(True)
            self.counter_gen = 0
            self.timer.stop()

    def _clear_clicked(self):
        self.simulation_data1 = []
        self.simulation_data2 = []
        self.simulation_time = [0]
        self.estimates_time = [0]
        self.ch_estimates = []
        self.DN_fixed = []
        self.ch_actual = []
        self.DN_SCAPE = []
        self.CRI = []
        self.k_vals = []
        self.bit_errors = []
        self.history_Error_fixed = []
        self.history_Error_adaptive = []
        self.history_capacity_actual = []
        self.history_capacity_estimated = []
        self.history_differential = []
        self._line_1 = None
        self._line_2 = None
        self._line_3 = None
        self._line_4 = None
        self._line_5 = None
        self._line_6 = None
        self._line_7 = None
        self._line_8 = None
        self._line_9 = None
        self._line_10 = None
        self._line_11 = None
        self._line_12 = None
        self._line_13 = None
        self._line_14 = None
        self._line_15 = None
        self._line_16 = None
        self._line_17 = None
        self._line_18 = None
        self._line_19 = None
        self.dynamic_canvas_1.clear()
        self.dynamic_canvas_2.clear()
        self.dynamic_canvas_3.clear()
        self.dynamic_canvas_4.clear()
        self.dynamic_canvas_5.clear()
        self.config_change = True
        self.counter_gen = 0
        self.lineEdit_dn_error_time_invariant_1.setText("")
        self.lineEdit_dn_error_1.setText("")
        self.lineEdit_estimation_deviation_1.setText("")
        self.lineEdit_capacity_estimated_1.setText("")
        self.lineEdit_capacity_actual_1.setText("")

        # averages over Y
        self.lineEdit_dn_error_time_invariant_2.setText("")
        self.lineEdit_dn_error_2.setText("")
        self.lineEdit_estimation_deviation_2.setText("")
        self.lineEdit_capacity_estimated_2.setText("")
        self.lineEdit_capacity_actual_2.setText("")

        

    def _reset_clicked(self):
        self._clear_clicked()
        self.lineEdit_channel_period.setText("1.000")
        self.lineEdit_estimation_period.setText("0.030")
        self.lineEdit_samples_per_period.setText("33.333")
        self.doubleSpinBox_X_2.setProperty("value", 2.0)
        self.SpinBox_bias.setProperty("value", 0.7)
        self.SpinBox_frequency.setProperty("value", 1.0)
        self.SpinBox_sampling_rate.setProperty("value", 10000.0)
        self.SpinBox_code_rate.setProperty("value", 13.0)
        self.SpinBox_adaptive_increment.setProperty("value", 4.0)
        self.SpinBox_adaptive_decrement.setProperty("value", 2.0)
        self.SpinBox_target_CRI.setProperty("value", 2.0)
        self.SpinBox_CRI_margin_up.setProperty("value", 3.0)
        self.SpinBox_CRI_margin_down.setProperty("value", 1.0)
        self.SpinBox_samples_N.setProperty("value", 300.0)
        self.dial.setProperty("value", 49)
        self.spinBox_X.setValue(100)
        self.spinBox_Y.setValue(10)
        self.checkBox_adaptive.setChecked(False)
        self.SpinBox_code_rate.setEnabled(True)
        self.SpinBox_CRI_margin_up.setDisabled(True)
        self.SpinBox_CRI_margin_down.setDisabled(True)
        self.SpinBox_adaptive_decrement.setDisabled(True)
        self.SpinBox_adaptive_increment.setDisabled(True)
        self.SpinBox_target_CRI.setDisabled(True)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

