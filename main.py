# -*- coding: utf-8 -*-

import sys
# якщо freecad 64 біт, то python повинен бути 2.7 64 !
FREECADPATH = "e:\\FreeCAD 0.17x64\\bin"
sys.path.append(FREECADPATH) # шлях до бібліотек FreeCAD
import FreeCAD as App # модуль для роботи з програмою
import FreeCADGui as Gui # модуль для роботи з GUI
import Part # workbench-модуль для створення і керування BRep об'єктами
import numpy as np
from dims import d

##
def show(name): # показує форму
    doc.addObject("Part::Feature",name).Shape=globals()[name]

def helixPoints(r,h,p,fi,n): # конічна гвинтова лінія
    "r-менший радіус, h-висота, p-крок, fi - кут (рад), n-кількість точок на витку"
    a=np.tan(fi)*p/(2*pi)
    b=p/(2*pi)
    k=h/p # кількість витків
    N=int(n*k) # загальна кількість точок
    t=np.linspace(0,h/b,N)
    x=(r+a*t)*np.cos(-t)
    z=(r+a*t)*np.sin(-t)
    y=b*t
    # y - вісь !
    return zip(t,x,y,z)
    
def perror(points):
    epoints=[]
    d=0.2
    for t,x,y,z in points:
        x=x#+np.random.triangular(-d,0,d)
        y=y#+np.random.triangular(-d,0,d)
        z=z#+np.random.triangular(-d,0,d)
        epoints.append((t,x,y,z))
    return epoints

def rebuildSketch(dim, sk):
    "Перебудовує ескіз і повертає грань. dim - розміри ескізу sk"
    doc=App.getDocument("Sketches")
    sketch=doc.__getattribute__(sk) #або doc.<назва ескізу>
    for k,v in dim.iteritems():
        sketch.setDatum(k,v)
    doc.recompute()
    w=sketch.Shape.Wires[0]
    f=Part.Face(w) # грань
    return f
    
def revolve(f):
    """Створює тіло шляхом обертання грані f навколо осі Y"""
    return f.revolve(App.Vector(0,0,0), App.Vector(0,1,0)) # тіло

def helix(r,h,p,fi):
    "Гвинтова лінія. r-радіус, h-висота, p-крок, fi-кут конуса (рад.)"
    w=Part.makeLongHelix(p,h,r,np.degrees(fi)) # !!! але не makeHelix
    #FreeCAD-master\src\Mod\Part\App\TopoShape.cpp
    w.rotate(App.Vector(0,0,0),App.Vector(1,0,0),-90)
    return w

def makeThread(f,h,s): # різьба ніпеля/муфти
    s2=h.makePipeShell(f.Wires,True,True) # дозволяє кілька профілів!
    s=s.cut(s2)
    return s
    
def helix2(points): # гвинтова лінія з відхиленнями
    pts=[(x,y,z) for t,x,y,z in points]
    h=Part.makePolygon(pts)
    return h
    
def makeThread2(f,h,s): # різьба з відхиленнями
    w=f.Wires[0]
    points=[(v.X,v.Y,v.Z) for v in h.Vertexes]
    W=[] # профілі в різних положеннях спіралі
    for x,y,z in points: 
        w_=w.copy()
        t=np.arctan2(-z,x)
        w_.rotate(App.Vector(0,0,0),App.Vector(0,1,0),np.degrees(t))
        w_.translate(App.Vector(x,y,z))
        W.append(w_.copy())
        if len(W)>1:
            st=Part.makeLoft([W[-2],W[-1]],True)
            s=s.cut(st) # віріз в заготовці
    
    return s,W

#S={} # форми
print "OCC", Part.OCC_VERSION
pi=np.pi
App.open(u"D:/3/Sketches.FCStd")

## ніпель
fA0=rebuildSketch(dim={6:d.fi, 9:d.H}, sk='Sketch') # tool
fA0.translate(d._v2)
sA0=revolve(rebuildSketch(dim={20:d.fi, 16:d.d3/2}, sk='Sketch001'))
hA0=helix(r=d._r, h=d.l4-12, p=d.P, fi=d.fi)
hA0.translate((0,d.l3-d.l4,0))
sA1=makeThread(fA0, hA0, sA0)

## муфта
fB2=rebuildSketch(dim={10:(pi-d.fi), 9:d.H}, sk='Sketch002') # tool
fB2.translate(d._v2)
#f2.rotate(App.Vector(0,0,0),App.Vector(0,1,0),1)
sB2=revolve(rebuildSketch(dim={28:d.fi, 17:d.d3/2}, sk='Sketch003'))
hB2=helix(r=d._r, h=d.l4, p=d.P, fi=d.fi)
hB2.translate((0,d.l3-d.l4,0))
sB3=makeThread(fB2, hB2, sB2)

## ніпель без відхилень
fA3=rebuildSketch(dim={6:d.fi, 9:d.H}, sk='Sketch') # tool
fA3.translate((-d.H/2+np.tan(d.fi)*d.P/2, d.P/2, 0))
points=helixPoints(r=d._r, h=d.l4-12, p=d.P, fi=d.fi, n=50)
hA3=helix2(points)
hA3.translate((0,d.l3-d.l4,0))
sA3,W=makeThread2(fA3, hA3, sA0)

## ніпель з відхиленнями
fA3.rotate(App.Vector(0,0,0),App.Vector(0,1,0),-10) # ненульовий передній кут 
points=perror(points)
hA3=helix2(points)
hA3.translate((0,d.l3-d.l4,0))
sA4,W=makeThread2(fA3, hA3, sA0)

# булеві операції над плоскими перерізами
f=Part.makePlane(400,400,App.Vector(-200,-200,0),App.Vector(0,0,1)) # площина XY
f1=sA3.common(f).Faces[0] # поздовжній перетин
f2=sA4.common(f).Faces[0]
f3=f1.cut(f2).fuse(f2.cut(f1)) # булеве XOR
print f3.Area # площа

##
# Наступні команди потрібні тільки для візуалізації створених форм
Gui.showMainWindow() # показати головне вікно
Gui.activateWorkbench("PartWorkbench")
doc=App.newDocument() # створити новий документ
# показати форми
show('fA0')
show('sA1')
show('sB3')
show('fA3')
show('hA3')
show('sA3')
show('sA4')
show('f1')
show('f2')
show('f3')
for w in W[:10]:
    Part.show(w)

doc.recompute() # перебудувати
Gui.exec_loop() # головний цикл програми