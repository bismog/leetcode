#!/usr/bin/env python
#-*- coding:utf-8 -*-

def func(a):
    a.append(1)
    a.append(2)
    a.append(3)

L = []
func(L)
print L


def func2(a):
    a = a + 1

I = 0
func2(I)
print I

def func3(il):
    il[0] = il[0] + 1

IL = [0,]
func3(IL)
print IL


def func4(nl):
    nl = [1,7,9]

NL = [0]
func4(NL)
print NL

def func5(dd):
    dd['aa'] = 127

DD = {'aa': 1}
func5(DD)
print DD


# def func6(ss):
#     ss[4] = 'O'
# 
# SS = 'HIHIHI'
# func6(SS)
# print SS
