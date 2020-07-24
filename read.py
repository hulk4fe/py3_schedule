#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ReadRes(object):
     def __init__(self):
         fo = open("/root/myProject/py_schedule/result.txt", "r+")
         # print("file name is: ", fo.name)
         self.__line = fo.read()
         fo.close()
     def getRes(self):
         return self.__line

