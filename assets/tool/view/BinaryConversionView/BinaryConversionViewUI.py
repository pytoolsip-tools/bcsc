# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-24 13:05:13
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-24 13:05:13

import wx;

from _Global import _GG;
from function.base import *;

defaultBinaryIdx = 2;
defaultBinaryList = ["二进制", "八进制", "十进制", "十六进制"];
defaultBinaryCfgList = [
	{"k" : 2, "v" : "0b", "f" : bin},
	{"k" : 8, "v" : "0", "f" : oct},
	{"k" : 10, "v" : "", "f" : int},
	{"k" : 16, "v" : "0x", "f" : hex},
];

class BinaryConversionViewUI(wx.Panel):
	"""docstring for BinaryConversionViewUI"""
	def __init__(self, parent, id = -1, curPath = "", viewCtr = None, params = {}):
		self.initParams(params);
		super(BinaryConversionViewUI, self).__init__(parent, id, pos = self.__params["pos"], size = self.__params["size"], style = self.__params["style"]);
		self._className_ = BinaryConversionViewUI.__name__;
		self._curPath = curPath;
		self.__viewCtr = viewCtr;
		self.__inputBinary = defaultBinaryIdx;
		self.__outputBinary = defaultBinaryIdx;
		self.__inputVal = "";

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
		self.createBinaryView();
		self.createResultView();
		pass;
		
	def initViewLayout(self):
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(self.__binaryPanel, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		box.Add(self.__resultPanel, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		self.SetSizer(box);
		pass;

	def updateView(self, data):
		pass;

	# 创建进制选择
	def createBinaryRadioBox(self, parent = None, label = "进制选择", choices = defaultBinaryList, onSelectRadio = None):
		if not parent:
			parent = self;
		rb = wx.RadioBox(parent, label = label, choices = choices, majorDimension = 1, style = wx.RA_SPECIFY_ROWS);
		rb.SetSelection(defaultBinaryIdx);
		def onRadioBox(event):
			if callable(onSelectRadio):
				onSelectRadio(rb.GetSelection(), rb.GetStringSelection());
			pass;
		rb.Bind(wx.EVT_RADIOBOX, onRadioBox);
		return rb;
	
	# 创建文本视图
	def createTextPanel(self, parent = None, label = "进制选择", size = (-1, -1), style = wx.TE_LEFT):
		if not parent:
			parent = self;
		textPanel = wx.Panel(parent, size = size);
		textTitle = wx.StaticText(textPanel, label = label);
		textVal = wx.TextCtrl(textPanel, size = (textPanel.GetSize().x - textTitle.GetSize().x, -1), style = style);
		# 设置布局
		box = wx.BoxSizer(wx.HORIZONTAL);
		box.Add(textTitle, flag = wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, border = 5);
		box.Add(textVal, flag = wx.ALIGN_CENTER|wx.EXPAND|wx.RIGHT, border = 5);
		textPanel.SetSizerAndFit(box);
		# 设置子节点
		textPanel._title = textTitle;
		textPanel._val = textVal;
		return textPanel;
	
	# 创建进制视图
	def createBinaryView(self):
		self.__binaryPanel = wx.Panel(self, size = (self.GetSize().x, -1), style = wx.BORDER_THEME);
		# 标题
		title = wx.StaticText(self.__binaryPanel, label = "进制转换");
		title.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD));
		# 源进制
		def onInputRadio(idx, selection):
			self.__inputBinary = idx;
			self.onUpdateOutput();
		srcBin = self.createBinaryRadioBox(self.__binaryPanel, label = "输入进制", onSelectRadio = onInputRadio);
		# 目标进制
		def onOutputRadio(idx, selection):
			self.__outputBinary = idx;
			self.onUpdateOutput();
		tgtBin = self.createBinaryRadioBox(self.__binaryPanel, label = "目标进制", onSelectRadio = onOutputRadio);
		# 设置布局
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(title, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		box.Add(srcBin, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		box.Add(tgtBin, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		self.__binaryPanel.SetSizer(box);
	
	# 创建转换结果
	def createResultView(self):
		self.__resultPanel = wx.Panel(self, size = (self.GetSize().x, -1), style = wx.BORDER_THEME);
		self.__inputPanel = self.createTextPanel(self.__resultPanel, label = "输入：", size = (self.GetSize().x, -1));
		self.__outputPanel = self.createTextPanel(self.__resultPanel, label = "输出：", size = (self.GetSize().x, -1), style = wx.TE_READONLY);
		# 绑定输入事件
		self.__inputPanel._val.Bind(wx.EVT_TEXT, self.onUpdateOutput);
		# 设置布局
		box = wx.BoxSizer(wx.VERTICAL);
		box.Add(self.__inputPanel, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		box.Add(self.__outputPanel, flag = wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border = 5);
		self.__resultPanel.SetSizerAndFit(box);
		pass;
	
	# 根据输入进行输出
	def onUpdateOutput(self, event = None):
		color, result = "blue", "";
		try:
			inputVal = self.__inputPanel._val.GetValue();
			if inputVal:
				cfg = defaultBinaryCfgList[self.__inputBinary];
				val = cfg["v"] + inputVal;
				tgtCfg = defaultBinaryCfgList[self.__outputBinary];
				result = str(tgtCfg["f"](int(val, cfg["k"])));
		except Exception as e:
			_GG("Log").d(f"Failed to conver binary! Err[{e}].");
			color, result = "red", f"输入内容不符合【{defaultBinaryList[self.__inputBinary]}】格式！";
		self.__outputPanel._val.SetValue(result);
		self.__outputPanel._val.SetForegroundColour(color);
		self.__outputPanel.Refresh();
		pass;
