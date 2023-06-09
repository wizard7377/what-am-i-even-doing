# Generated by Haxe 4.3.0
# coding: utf-8
import sys

import math as python_lib_Math
import math as Math
import random as python_lib_Random


class Main:
    __slots__ = ()

    @staticmethod
    def generateRandom(_hx_len = None):
        if (_hx_len is None):
            _hx_len = 100
        rVec = ([None]*_hx_len)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            v = _g
            _g = (_g + 1)
            val = Math.floor(((python_lib_Random.random() * 100000) + 0.5))
            rVec[v] = val
        return rVec

    @staticmethod
    def main():
        i = 0
        rVec = Main.generateRandom(Main.totalLen)
        print(str(rVec))
        while (i < ((Main.totalLen - 1))):
            if (rVec[i] > rVec[(i + 1)]):
                tVar = rVec[i]
                val = rVec[(i + 1)]
                rVec[i] = val
                rVec[(i + 1)] = tVar
                i = (i - 1)
            else:
                i = (i + 1)
            if (i < 0):
                i = 0
        print(str(rVec))


class haxe_iterators_ArrayIterator:
    __slots__ = ("array", "current")

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()



class python_internal_ArrayImpl:
    __slots__ = ()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None


class python_internal_MethodClosure:
    __slots__ = ("obj", "func")

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)


Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

Main.totalLen = 10

Main.main()
