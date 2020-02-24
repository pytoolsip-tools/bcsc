# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-24 18:35:57
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-24 18:35:57
import os;
import wx;

from _Global import _GG;

from ScientificCalculatorViewUI import *;

def getRegisterEventMap(G_EVENT):
	return {
		# G_EVENT.TO_UPDATE_VIEW : "updateView",
	};

class ScientificCalculatorViewCtr(object):
	"""docstring for ScientificCalculatorViewCtr"""
	def __init__(self, parent, params = {}):
		super(ScientificCalculatorViewCtr, self).__init__();
		self._className_ = ScientificCalculatorViewCtr.__name__;
		self._curPath = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "/";
		self.__CtrMap = {}; # 所创建的控制器
		self.initUI(parent, params); # 初始化视图UI
		self.registerEventMap(); # 注册事件
		self.bindBehaviors(); # 绑定组件
		self.createTimers();

	def __del__(self):
		self.__dest__();

	def __dest__(self):
		if not hasattr(self, "_unloaded_"):
			self._unloaded_ = True;
			self.__unload__();

	def __unload__(self):
		self.unregisterEventMap(); # 注销事件
		self.unbindBehaviors(); # 解绑组件
		self.delCtrMap(); # 銷毀控制器列表
		self.stopAllTimer(isDestroy = True); # 停止所有定时器

	def delCtrMap(self):
		for key in self.__CtrMap:
			DelCtr(self.__CtrMap[key]);
		self.__CtrMap.clear();

	def initUI(self, parent, params):
		# 创建视图UI类
		self.__ui = ScientificCalculatorViewUI(parent, curPath = self._curPath, viewCtr = self, params = params);
		self.__ui.initView();

	def getUI(self):
		return self.__ui;

	"""
		key : 索引所创建控制类的key值
		path : 所创建控制类的路径
		parent : 所创建控制类的UI的父节点，默认为本UI
		params : 扩展参数
	"""
	def createCtrByKey(self, key, path, parent = None, params = {}):
		if not parent:
			parent = self.getUI();
		self.__CtrMap[key] = CreateCtr(path, parent, params = params);

	def getCtrByKey(self, key):
		return self.__CtrMap.get(key, None);

	def getUIByKey(self, key):
		ctr = self.getCtrByKey(key);
		if ctr:
			return ctr.getUI();
		return None;
		
	def registerEventMap(self):
		eventMap = getRegisterEventMap(_GG("EVENT_ID"));
		for eventId, callbackName in eventMap.items():
			_GG("EventDispatcher").register(eventId, self, callbackName);

	def unregisterEventMap(self):
		eventMap = getRegisterEventMap(_GG("EVENT_ID"));
		for eventId, callbackName in eventMap.items():
			_GG("EventDispatcher").unregister(eventId, self, callbackName);

	def bindBehaviors(self):
		pass;
		
	def unbindBehaviors(self):
		pass;
			
	def updateView(self, data):
		self.__ui.updateView(data);

	def createTimers(self):
		self.__Timer = wx.Timer(self.getUI());
		self.getUI().Bind(wx.EVT_TIMER, self.onTimer, self.__Timer);
		# 启动定时器
		self.__Timer.Start(100);

	def stopAllTimer(self, isDestroy = False):
		if self.__Timer.IsRunning():
			self.__Timer.Stop();
			if isDestroy:
				del self.__Timer;
		pass;
	
	def onTimer(self, event = None):
		if not self.getUI().isPointInItemRect(wx.GetMousePosition()): # 判断鼠标位置是否在节点内
			self.getUI().resetEnterItem();
		pass;