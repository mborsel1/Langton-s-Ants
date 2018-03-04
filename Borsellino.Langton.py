#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:58:05 2018

@author: Michael Borsellino
"""

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import scipy as SP

width = 100
height = 100

def init():
    global time, x1, y1, config, state, lastx, lasty

    time = 0
    lastx, lasty = 1, 0
    x1, y1 = width/2, height/2
        
    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
            state = 0
        config[x, y] = state

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, x1, y1, state, config, lastx, lasty
    
    time += 1
    state = config[x1, y1]

    if state == 0: #if white
        state = 1 #change to black
        if lastx == 0: #if did not move horizontal
            if lasty == 1: #and moved up
                lastx, lasty = -1, 0 #move left
            else: #and moved down
                lastx, lasty = 1, 0  #move right
        elif lastx == 1: #if moved right
            lastx, lasty = 0, 1 #move up
        else: #if moved left
            lastx, lasty = 0, -1  #move down 
    else: #if black
        state = 0 #change to white
        if lastx == 0: #if did not move horization
            if lasty == 1: #and moved up
                lastx, lasty = 1, 0 #move right
            else: #and moved down
                lastx, lasty = -1, 0 #move left 
        elif lastx == 1: #if moved right
            lastx, lasty = 0, -1 #move down
        else: #if moved left
            lastx, lasty = 0, 1 #move up
    config[x1, y1] = state
    x1, y1 = x1 + lastx, y1 + lasty        

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])