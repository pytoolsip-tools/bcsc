# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-27 00:35:29
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-27 00:35:29

import wx;

from _Global import _GG;
from function.base import *;

ruleDescList = [
	"CL : 清空",
	"< : 删除",
	"asin : 反正弦",
	"acos : 反余弦",
	"atan : 反正切",
	"sin : 正弦",
	"cos : 余弦",
	"tan : 正切",
	"e : 自然数e",
	"Pi : 圆周率",
	"C(x,y) : 从y取x的组合",
	"A(x,y) : 从y取x的排列",
	"deg : 弧度转角度",
	"rad : 角度转弧度",
	"n! : 阶乘",
	"% : 取余",
	"^ : 幂",
	"/ : 除",
	"* : 乘",
	"|x| : 绝对值",
	"sqrt : 平方根",
	"log(x,y) : 底为y的x对数",
];

class RuleDescViewUI(wx.Panel):
	"""docstring for RuleDescViewUI"""
	def __init__(self, parent, id = -1, curPath = "", viewCtr = None, params = {}):
		self.initParams(params);
		super(RuleDescViewUI, self).__init__(parent, id, pos = self.__params["pos"], size = self.__params["size"], style = self.__params["style"]);
		self._className_ = RuleDescViewUI.__name__;
		self._curPath = curPath;
		self.__viewCtr = viewCtr;

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
		self.createTitle();
		self.createRuleView();
		pass;
		
	def initViewLayout(self):
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(self.__title, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		box.Add(self.__ruleView, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		self.SetSizer(box);
		pass;

	def updateView(self, data):
		pass;

	def createTitle(self):
		self.__title = wx.StaticText(self, label = "计算器规则说明");
		self.__title.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD));
		pass;
	
	def createRuleView(self):
		self.__ruleView = wx.Panel(self, size = (self.GetSize().x, -1), style = wx.BORDER_THEME);
		self.__ruleView.SetBackgroundColour(wx.Colour(230, 230, 230));
		textList = [];
		for ruleDeac in ruleDescList:
			textList.append(wx.StaticText(self.__ruleView, label = ruleDeac));
		box = wx.BoxSizer(wx.VERTICAL);
		for text in textList:
			box.Add(text, flag = wx.ALIGN_LEFT|wx.TOP|wx.BOTTOM, border = 2);
		self.__ruleView.SetSizer(box);
		pass;