#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:38:30 2019

@author: zelord
"""

def solution(answers):
    answer = []
    case1 = [1,2,3,4,5]
    case2 = [2,1,2,3,2,4,2,5]
    case3 = [3,3,1,1,2,2,4,4,5,5,]
    for i in [case1,case2,case3]:
        temp = 0
        for j in range(len(answers)):
            if (answers[j] == i[j% len(i)]):
                temp += 1
        print(temp)
        answer.append(temp)
    result = []
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            result.append(i+1)
    return result