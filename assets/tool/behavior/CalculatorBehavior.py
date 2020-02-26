# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-25 12:18:05
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-25 12:18:05

import math;

import wx;

from _Global import _GG;
from function.base import *;

from enum import Enum, unique;

@unique
class CalcType(Enum):
	CalcOp	= 0; # 计算操作
	Const	= 1; # 常数
	Single	= 2; # 单参数运算
	Double	= 3; # 双参数运算
	Operate	= 4; # 双参数运算
	BkLeft	= 5; # 括号（左）
	BkRight	= 6; # 括号（右）
	Comma	= 7; # 逗号
	Dot		= 8; # 句号


# 阶乘
def factorial(val):
	return math.factorial(int(val));

# 组合
def combine(m, n):
	if m < 0 or n < 0:
		raise ValueError("C(x,y) only accepts non negative numbers!");
	if m > n:
		raise ValueError("C(x,y) only allow x < y!");
	return factorial(n) / (factorial(m) * factorial(n-m));

# 排列
def arrange(m, n):
	if m < 0 or n < 0:
		raise ValueError("C(x,y) only accepts non negative numbers!");
	if m > n:
		raise ValueError("C(x,y) only allow x < y!");
	return factorial(n) / factorial(n-m);

itemConfig = [
	{"val" : "CL", "normalColor" : wx.Colour(205, 155, 155), "enterColor" : wx.Colour(205, 96, 96), "func" : "clear", "type" : CalcType.CalcOp},
	{"val" : "asin", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.asin(", "fmt" : "asin(", "type" : CalcType.Single},
	{"val" : "acos", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.acos(", "fmt" : "acos(", "type" : CalcType.Single},
	{"val" : "atan", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.atan(", "fmt" : "atan(", "type" : CalcType.Single},
	{"val" : "<", "normalColor" : wx.Colour(205, 186, 150), "enterColor" : wx.Colour(205, 149, 12), "func" : "delete", "type" : CalcType.CalcOp},
	
	{"val" : "e", "normalColor" : wx.Colour(210, 250, 210), "enterColor" : wx.Colour(156, 250, 156), "func" : "math.e", "fmt" : "e", "type" : CalcType.Const},
	{"val" : "sin", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.sin(", "fmt" : "sin(", "type" : CalcType.Single},
	{"val" : "cos", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.cos(", "fmt" : "cos(", "type" : CalcType.Single},
	{"val" : "tan", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.tan(", "fmt" : "tan(", "type" : CalcType.Single},
	{"val" : "Pi", "normalColor" : wx.Colour(210, 250, 210), "enterColor" : wx.Colour(156, 250, 156), "func" : "math.pi", "fmt" : "Pi", "type" : CalcType.Const},
	
	{"val" : "C(x, y)", "normalColor" : wx.Colour(210, 210, 250), "enterColor" : wx.Colour(181, 160, 255), "func" : "combine(", "fmt" : "C(", "type" : CalcType.Double},
	{"val" : "deg", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.degrees(", "fmt" : "deg(", "type" : CalcType.Single},
	{"val" : "rad", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.radians(", "fmt" : "rad(", "type" : CalcType.Single},
	{"val" : "n!", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "factorial(", "fmt" : "fact(", "type" : CalcType.Single},
	{"val" : "%", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "%", "fmt" : "%", "type" : CalcType.Operate},
	
	{"val" : "A(x, y)", "normalColor" : wx.Colour(210, 210, 250), "enterColor" : wx.Colour(181, 160, 255), "func" : "arrange(", "fmt" : "A(", "type" : CalcType.Double},
	{"val" : "(", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "(", "fmt" : "(", "type" : CalcType.BkLeft},
	{"val" : ")", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : ")", "fmt" : ")", "type" : CalcType.BkRight},
	{"val" : "|x|", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.fabs(", "fmt" : "abs(", "type" : CalcType.Single},
	{"val" : "/", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "/", "fmt" : "/", "type" : CalcType.Operate},
	
	{"val" : "sqrt", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.sqrt(", "fmt" : "sqrt(", "type" : CalcType.Single},
	{"val" : "7", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "7", "fmt" : "7", "type" : CalcType.Const},
	{"val" : "8", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "8", "fmt" : "8", "type" : CalcType.Const},
	{"val" : "9", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "9", "fmt" : "9", "type" : CalcType.Const},
	{"val" : "*", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "*", "fmt" : "*", "type" : CalcType.Operate},
	
	{"val" : "pow(x,y)", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.pow(", "fmt" : "pow(", "type" : CalcType.Double},
	{"val" : "4", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "4", "fmt" : "4", "type" : CalcType.Const},
	{"val" : "5", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "5", "fmt" : "5", "type" : CalcType.Const},
	{"val" : "6", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "6", "fmt" : "6", "type" : CalcType.Const},
	{"val" : "-", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "-", "fmt" : "-", "type" : CalcType.Operate},
	
	{"val" : "log(x, y)", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.log(", "fmt" : "log(", "type" : CalcType.Double},
	{"val" : "1", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "1", "fmt" : "1", "type" : CalcType.Const},
	{"val" : "2", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "2", "fmt" : "2", "type" : CalcType.Const},
	{"val" : "3", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "3", "fmt" : "3", "type" : CalcType.Const},
	{"val" : "+", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "+", "fmt" : "+", "type" : CalcType.Operate},
	
	{"val" : "ln", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "math.log(", "fmt" : "ln(", "type" : CalcType.Single},
	{"val" : ",", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : ",", "fmt" : ",", "type" : CalcType.Comma},
	{"val" : "0", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "0", "fmt" : "0", "type" : CalcType.Const},
	{"val" : ".", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : ".", "fmt" : ".", "type" : CalcType.Dot},
	{"val" : "=", "normalColor" : wx.Colour(108, 166, 205), "enterColor" : wx.Colour(79, 148, 205), "func" : "equal", "type" : CalcType.CalcOp},
];

def __getExposeData__():
	return {
		# "exposeDataName" : {},
	};

def __getExposeMethod__(DoType):
	return {
		"getItemConfig" : DoType.Override,
		"onInputCalc" : DoType.Override,
		"isBkRightItem" : DoType.Override,
		"isCommaItem" : DoType.Override,
		"getBkRightLackCnt" : DoType.Override,
		"getCommaLackCnt" : DoType.Override,
	};

def __getDepends__():
	return [
		# {
		# 	"path" : "tempBehavior", 
		# 	"basePath" : _GG("g_CommonPath") + "behavior/",
		# },
	];

class CalculatorBehavior(_GG("BaseBehavior")):
	def __init__(self):
		super(CalculatorBehavior, self).__init__(__getDepends__(), __getExposeData__(), __getExposeMethod__, __file__);
		self._className_ = CalculatorBehavior.__name__;
		self.__result = "";
		self.__process = "0";
		self.__processList = [];
		pass;

	# 默认方法【obj为绑定该组件的对象，argList和argDict为可变参数，_retTuple为该组件的前个函数返回值】
	# def defaultFun(self, obj, *argList, _retTuple = None, **argDict):
	# 	_GG("Log").i(obj._className_);
	# 	pass;

	def getItemConfig(self, obj):
		return itemConfig;
	
	def onInputCalc(self, obj, cfg = {}):
		if cfg["type"] == CalcType.CalcOp:
			getattr(self, cfg["func"])(obj, cfg);
		else:
			if len(self.__processList) == 0:
				self.__process = cfg["fmt"];
			else:
				self.__process += cfg["fmt"];
			self.__processList.append(cfg);
		return self.__result, self.__process;

	def getProcess(self):
		return "".join([p["fmt"] for p in self.__processList]);

	def calcProcess(self):
		try:
			return eval("".join([p["func"] for p in self.__processList]));
		except Exception as e:
			_GG("Log").d(f"Failed to calc process! Err[{e}].");
		return None;

	def clear(self, obj, cfg = []):
		self.__processList.clear();
		self.__result, self.__process, = "", "0";
		pass;

	def delete(self, obj, cfg = []):
		if len(self.__processList) > 0:
			self.__processList.pop();
		if len(self.__processList) == 0:
			self.__process = "0";
		else:
			self.__process = self.getProcess();
		pass;
	
	def equal(self, obj, cfg = []):
		# 补足右括号
		bkRightLackCnt = self.getBkRightLackCnt(obj);
		if bkRightLackCnt > 0:
			self.__processList.append(")" * bkRightLackCnt);
		# 计算结果
		ret = self.calcProcess();
		if ret == None:
			self.__process = "计算失败，请检查输入！";
			self.__processList.clear();
		else:
			val = str(ret);
			self.__result = self.getProcess() + "=" + val;
			self.__process = val;
			self.__processList = [{"func" : val, "fmt" : val, "type" : CalcType.Const}];
		pass;

	def isBkRightItem(self, obj, cfg = {}):
		return cfg.get("type", None) == CalcType.BkRight;

	def isCommaItem(self, obj, cfg = {}):
		return cfg.get("type", None) == CalcType.Comma;

	def getBkRightLackCnt(self, obj):
		return self.__process.count("(") - self.__process.count(")");
	
	def getCommaLackCnt(self, obj):
		cnt = 0;
		for p in self.__processList:
			if p["type"] == CalcType.Double:
				cnt += 1;
		return cnt - self.__process.count(",");