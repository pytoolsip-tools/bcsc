# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-25 12:18:05
# @Last Modified by:   Administrator
# @Last Modified time: 2020-02-25 12:18:05

import math;

import wx;

from _Global import _GG;
from function.base import *;

# 倒数
def reciprocal(val):
	return 1/val;

# 阶乘
def factorial(val):
	return math.factorial(int(val));

# 相反
def opposite(val):
	if val == 0:
		return val;
	return -val;

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
	{"val" : "CL", "normalColor" : wx.Colour(205, 155, 155), "enterColor" : wx.Colour(205, 96, 96), "func" : "clear"},
	{"val" : "asin", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.asin, "asin(%s)", "无效输入"]},
	{"val" : "acos", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.acos, "acos(%s)", "无效输入"]},
	{"val" : "atan", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.atan, "atan(%s)", "无效输入"]},
	{"val" : "<", "normalColor" : wx.Colour(205, 186, 150), "enterColor" : wx.Colour(205, 149, 12), "func" : "delete"},
	
	{"val" : "e", "normalColor" : wx.Colour(210, 250, 210), "enterColor" : wx.Colour(156, 250, 156), "func" : "const", "args" : [math.e]},
	{"val" : "sin", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.sin, "sin(%s)"]},
	{"val" : "cos", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.cos, "cos(%s)"]},
	{"val" : "tan", "normalColor" : wx.Colour(240, 240, 240), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.tan, "tan(%s)", "无效输入"]},
	{"val" : "Pi", "normalColor" : wx.Colour(210, 250, 210), "enterColor" : wx.Colour(156, 250, 156), "func" : "const", "args" : [math.pi]},
	
	{"val" : "C(x, y)", "normalColor" : wx.Colour(210, 210, 250), "enterColor" : wx.Colour(181, 160, 255), "func" : "operate", "args" : [combine]},
	{"val" : "1/x", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [reciprocal, "1/(%s)", "除数不能为零"]},
	{"val" : "|x|", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.fabs, "abs(%s)"]},
	{"val" : "n!", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [factorial, "fact(%s)", "负数不能阶乘"]},
	{"val" : "mod", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : ["%"]},
	
	{"val" : "A(x, y)", "normalColor" : wx.Colour(210, 210, 250), "enterColor" : wx.Colour(181, 160, 255), "func" : "operate", "args" : [arrange]},
	{"val" : "(", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "brackets"},
	{"val" : ")", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "brackets"},
	{"val" : "^", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : ["^"]},
	{"val" : "/", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : ["/"]},
	
	{"val" : "sqrt", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.sqrt, "sqrt(%s)", "无效输入"]},
	{"val" : "7", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [7]},
	{"val" : "8", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [8]},
	{"val" : "9", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [9]},
	{"val" : "*", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : ["*"]},
	
	{"val" : "pow(x,y)", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : [math.pow]},
	{"val" : "4", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [4]},
	{"val" : "5", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [5]},
	{"val" : "6", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [6]},
	{"val" : "-", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : ["-"]},
	
	{"val" : "log(x, y)", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : [math.log]},
	{"val" : "1", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [1]},
	{"val" : "2", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [2]},
	{"val" : "3", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [3]},
	{"val" : "+", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "operate", "args" : ["+"]},
	
	{"val" : "ln", "normalColor" : wx.Colour(230, 230, 230), "enterColor" : wx.Colour(200, 200, 200), "func" : "result", "args" : [math.log, "ln(%s)"]},
	{"val" : "+/-", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "change", "args" : [opposite]},
	{"val" : "0", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "number", "args" : [0]},
	{"val" : ".", "normalColor" : "white", "enterColor" : wx.Colour(200, 200, 200), "func" : "dot"},
	{"val" : "=", "normalColor" : wx.Colour(108, 166, 205), "enterColor" : wx.Colour(79, 148, 205), "func" : "equal"},
];

def __getExposeData__():
	return {
		# "exposeDataName" : {},
	};

def __getExposeMethod__(DoType):
	return {
		"getItemConfig" : DoType.Override,
		"onCalculate" : DoType.Override,
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
		pass;

	# 默认方法【obj为绑定该组件的对象，argList和argDict为可变参数，_retTuple为该组件的前个函数返回值】
	# def defaultFun(self, obj, *argList, _retTuple = None, **argDict):
	# 	_GG("Log").i(obj._className_);
	# 	pass;

	def getItemConfig(self, obj):
		return itemConfig;
	
	def onCalculate(self, obj, result, process, temp, cfg = {}):
		if "func" in cfg and hasattr(self, cfg["func"]):
			return getattr(self, cfg["func"])(obj, result, process, temp, args = cfg.get("args", []));
		return result, process, temp;

	def splitResult(self, result):
		if result:
			ret = result.split("=");
			if len(ret) > 1:
				return ret[0], float(ret[1]);
		return result, 0;

	def combTemp(self, temp):
		ret, opFmtList = [], [];
		for item in temp:
			isop = False;
			if isinstance(item, dict):
				if item.type == "result":
					ret[-1] = item.fmt % ret[-1];
				elif item.type == "operate":
					opFmtList.append(item.fmt);
					isop = True;
			else:
				ret.append(item);
			if not isop and len(opFmtList) > 0:
				fmt = opFmtList.pop();
				ret[-2] = fmt % (ret[-2], ret[-1]);
		return "".join(ret);

	def calcTemp(self, temp):
		ret, opFuncList = [], [];
		for item in temp:
			isop = False;
			if isinstance(item, dict):
				if item.type == "result":
					ret[-1] = item.func(ret[-1]);
				elif item.type == "operate":
					opFuncList.append(item.func);
					isop = True;
			else:
				ret.append(float(item));
			if not isop and len(opFuncList) > 0:
				func = opFuncList.pop();
				ret[-2] = func(ret[-2], ret[-1]);
				ret.pop();
		return sum(ret);

	def clear(self, obj, result, temp, args = []):
		return "", "0", ["0"];

	def delete(self, obj, result, process, temp, args = []):
		if len(temp) > 0:
			temp.pop();
		if len(temp) == 0:
			return result, "0", ["0"];
		return result, self.combTemp(temp), temp;

	def result(self, obj, result, process, temp, args = []):
		if len(temp) > 0:
			val = temp[-1];
			if val.isdigit():
				process += args[1] % val;
				temp.append(args);
			return result, process, temp;
		return result, process, temp;
	
	def number(self, obj, result, process, temp, args = []):
		pass;
