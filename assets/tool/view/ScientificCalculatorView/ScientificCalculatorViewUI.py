# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-24 18:35:57
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-24 18:35:57
import math;

import wx;

from _Global import _GG;
from function.base import *;

itemConfig = [
	{"val" : "CL", "normalColor" : wx.Colour(205, 155, 155), "enterColor" : wx.Colour(205, 96, 96)},
	{"val" : "asin", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "acos", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "atan", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "<", "normalColor" : wx.Colour(205, 186, 150), "enterColor" : wx.Colour(205, 149, 12)},
	
	{"val" : "e", "normalColor" : wx.Colour(210, 250, 210), "enterColor" : wx.Colour(156, 250, 156)},
	{"val" : "sin", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "cos", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "tan", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "Pi", "normalColor" : wx.Colour(210, 250, 210), "enterColor" : wx.Colour(156, 250, 156)},
	
	{"val" : "C(x, y)", "normalColor" : wx.Colour(210, 210, 250), "enterColor" : wx.Colour(181, 160, 255)},
	{"val" : "1/x", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "|x|", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "n!", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "mod", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	
	{"val" : "A(x, y)", "normalColor" : wx.Colour(210, 210, 250), "enterColor" : wx.Colour(181, 160, 255)},
	{"val" : "(", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : ")", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "^", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "/", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	
	{"val" : "sqrt", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "7", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "8", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "9", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "*", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	
	{"val" : "pow(x,y)", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "4", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "5", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "6", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "-", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	
	{"val" : "log(x, y)", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "1", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "2", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "3", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "+", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	
	{"val" : "ln", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "+/-", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "0", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : ".", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200)},
	{"val" : "=", "normalColor" : wx.Colour(108, 166, 205), "enterColor" : wx.Colour(79, 148, 205)},
];

class ScientificCalculatorViewUI(wx.Panel):
	"""docstring for ScientificCalculatorViewUI"""
	def __init__(self, parent, id = -1, curPath = "", viewCtr = None, params = {}):
		self.initParams(params);
		super(ScientificCalculatorViewUI, self).__init__(parent, id, pos = self.__params["pos"], size = self.__params["size"], style = self.__params["style"]);
		self._className_ = ScientificCalculatorViewUI.__name__;
		self._curPath = curPath;
		self.__viewCtr = viewCtr;
		self.__enterItem = None;

	def initParams(self, params):
		# 初始化参数
		self.__params = {
			"pos" : (0,0),
			"size" : (-1,-1),
			"style" : wx.BORDER_THEME,
		};
		for k,v in params.items():
			self.__params[k] = v;

	def getCtr(self):
		return self.__viewCtr;

	def initView(self):
		self.createControls(); # 创建控件
		self.initViewLayout(); # 初始化布局

	def createControls(self):
		# self.getCtr().createCtrByKey("key", self._curPath + "***View"); # , parent = self, params = {}
		self.createResultView();
		self.createInputView();
		pass;
		
	def initViewLayout(self):
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(self.__resultPanel, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		box.Add(self.__inputPanel, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		self.SetSizer(box);
		pass;

	def updateView(self, data):
		pass;

	def createResultView(self):
		self.__resultPanel = wx.Panel(self, size = (self.GetSize().x, -1));
		processTC = wx.TextCtrl(self.__resultPanel, size = (self.GetSize().x, -1), style = wx.TE_READONLY);
		resultTC = wx.TextCtrl(self.__resultPanel, size = (self.GetSize().x, 120), style = wx.TE_READONLY|wx.TE_RIGHT|wx.TE_MULTILINE);
		# 设置布局
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(processTC, flag = wx.ALIGN_CENTER);
		box.Add(resultTC, flag = wx.ALIGN_CENTER);
		self.__resultPanel.SetSizerAndFit(box);
	
	def createInputView(self):
		self.__inputPanel = wx.Panel(self, size = (self.GetSize().x, -1));
		items = [];
		for cfg in itemConfig:
			item = self.createItemView(self.__inputPanel, cfg["val"], cfg["normalColor"], cfg["enterColor"]);
			items.append(item);
			pass;
		cols = 5; # 默认5行
		rows = math.ceil(len(items) / 5);
		gridSizer = wx.GridSizer(rows, cols, 0, 0);
		for item in items:
			gridSizer.Add(item);
		self.__inputPanel.SetSizerAndFit(gridSizer);
		pass;
	
	def createItemView(self, parent, label = "", normalColor = "white", enterColor = "gray"):
		p = wx.Panel(parent, size = (80, 40), style = wx.BORDER_THEME);
		p._normalColor = normalColor;
		p._enterColor = enterColor;
		ctx = wx.StaticText(p, label = label);
		# 设置布局
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(ctx, flag = wx.ALIGN_CENTER|wx.TOP, border = 10);
		p.SetSizer(box);
		# 绑定事件
		def onEnterItem(event):
			if self.__enterItem != p:
				self.updateItemBgColor();
				# 更新enterItem
				self.__enterItem = p;
				self.updateItemBgColor(True);
		p.Bind(wx.EVT_ENTER_WINDOW, onEnterItem);
		ctx.Bind(wx.EVT_ENTER_WINDOW, onEnterItem);
		# 更新背景色
		if p.SetBackgroundColour(normalColor):
			p.Refresh();
		return p;

	def updateItemBgColor(self, isEnter = False):
		if self.__enterItem:
			color = isEnter and self.__enterItem._enterColor or self.__enterItem._normalColor;
			if self.__enterItem.SetBackgroundColour(color):
				self.__enterItem.Refresh();
		pass;

	def isPointInItemRect(self, pos):
		if not self.__enterItem:
			return False;
		item = self.__enterItem;
		# 转换位置
		convertPos = item.ScreenToClient(*pos);
		# 判断位置
		if convertPos[0] >= 0 and convertPos[0] <= item.GetSize()[0] and convertPos[1] >= 0 and convertPos[1] <= item.GetSize()[1]:
			return True;
		return False;
	
	def resetEnterItem(self):
		self.updateItemBgColor();
		self.__enterItem = None;
		pass;