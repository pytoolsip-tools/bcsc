# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-24 18:35:57
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-24 18:35:57
import math;

import wx;

from _Global import _GG;
from function.base import *;


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
		resultTC = wx.TextCtrl(self.__resultPanel, size = (self.GetSize().x, -1), style = wx.TE_READONLY|wx.TE_RIGHT);
		processTC = wx.TextCtrl(self.__resultPanel, size = (self.GetSize().x, 120), value = "0", style = wx.TE_READONLY|wx.TE_RIGHT|wx.TE_MULTILINE);
		processTC.SetFont(wx.Font(28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD));
		# 设置布局
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(resultTC, flag = wx.ALIGN_CENTER);
		box.Add(processTC, flag = wx.ALIGN_CENTER);
		self.__resultPanel.SetSizerAndFit(box);
		self.__resultPanel._result = resultTC;
		self.__resultPanel._process = processTC;
		self.__resultPanel._temp = ["0"]; # 中间值
	
	def createInputView(self):
		self.__inputPanel = wx.Panel(self, size = (self.GetSize().x, -1));
		items = [];
		for cfg in self.getCtr().getItemConfig():
			item = self.createItemView(self.__inputPanel, cfg);
			items.append(item);
			pass;
		cols = 5; # 默认5行
		rows = math.ceil(len(items) / 5);
		gridSizer = wx.GridSizer(rows, cols, 0, 0);
		for item in items:
			gridSizer.Add(item);
		self.__inputPanel.SetSizerAndFit(gridSizer);
		pass;
	
	def createItemView(self, parent, cfg = {}):
		label, normalColor, enterColor = cfg.get("val", ""), cfg.get("normalColor", "white"), cfg.get("enterColor", "gray");
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
				self.__enterItem._onClick = False;
				self.updateItemBgColor(True);
		p.Bind(wx.EVT_ENTER_WINDOW, onEnterItem);
		ctx.Bind(wx.EVT_ENTER_WINDOW, onEnterItem);
		def onClickItem(event):
			if self.__enterItem.SetBackgroundColour("gray"):
				self.__enterItem.Refresh();
				self.__enterItem._onClick = True;
			if hasattr(self.getCtr(), "onCalculate") and callable(getattr(self.getCtr(), "onCalculate")):
				result, process, temp = getattr(self.getCtr(), "onCalculate")(self.__resultPanel._result.GetValue(), self.__resultPanel._process.GetValue(), self.__resultPanel._temp, cfg = cfg);
				self.__resultPanel._result.SetValue(result);
				self.__resultPanel._process.SetValue(process);
				self.__resultPanel._temp = temp;
		p.Bind(wx.EVT_LEFT_DOWN, onClickItem);
		ctx.Bind(wx.EVT_LEFT_DOWN, onClickItem);
		# 更新背景色
		p._onClick = False;
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
	
	def checkEnterItemOnClick(self):
		if self.__enterItem and self.__enterItem._onClick:
			self.__enterItem._onClick = False;
			self.updateItemBgColor(True);
		pass;
	
	def resetEnterItem(self):
		self.updateItemBgColor();
		self.__enterItem = None;
		pass;