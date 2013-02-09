#!/usr/bin/python
#
# C++ version Copyright (c) 2006-2007 Erin Catto http://www.gphysics.com
# Python version Copyright (c) 2008 kne / sirkne at gmail dot com
# 
# Implemented using the pybox2d SWIG interface for Box2D (pybox2d.googlecode.com)
# 
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

class fwSettings(object):
    hz=60.0
    velocityIterations=10
    positionIterations=8
    drawStats=False
    drawShapes=True
    drawJoints=True
    drawControllers=True
    drawCoreShapes=False
    drawAABBs=False
    drawOBBs=False
    drawPairs=False
    drawContactPoints=False
    drawContactNormals=False
    drawContactForces=False
    drawFrictionForces=False
    drawCOMs=False
    enableWarmStarting=True
    enablePositionCorrection=True
    enableTOI=True
    pause=False
    singleStep=False
    drawFPS=True # python version
    pointSize=5 # python version (pixel radius for drawing points)
    drawMenu=True #toggle by pressing F1
