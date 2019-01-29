# -*- coding: utf-8 -*-
execfile("tools.py")
from dimsZamok import d
App.open(u"SketchesZamok.FCStd")

## ніпель
alfa0=8.0 #4..8
gamma0=-10 #0..-10
n=2 #2 13 19 номер витка (положення різця)
insertS=6.1 # товщина пластинки
omega=np.degrees(np.arctan(d.P/(2*pi*d.dsr))) # кут нахилу гвинтової лінії на dsr
print omega #np.arctan(d.P/(2*pi(Rmin+L*np.tan(d.fi))) 

dim={'fi':d.fi, 'H':d.H, 'r':d.r}
fA0=rebuildSketch(dim=dim, sk='Sketch') # tool
e0=Part.makeLine((0,0,0),(insertS*np.tan(np.radians(alfa0+gamma0)),0,insertS))
s_tl=Part.Wire([e0]).makePipe(fA0) # різець в нульовому положенні
for x in fA0,s_tl:
    x.rotate(App.Vector(0,0,0),App.Vector(0,1,0),-gamma0) # утв. передній кут
    x.rotate(App.Vector(0,0,0),App.Vector(1,0,0), omega) # повернути на omega

s_tl0=s_tl.copy()

for x in fA0,s_tl:
    x.translate(d._v1) # початкове положення (усюди d._v1 або усюди d._v2)

s_tl.translate(App.Vector(n*d.P*d.tanFi, n*d.P, 0)) # задане положення різця
fA0.translate(App.Vector(n*d.P*d.tanFi, n*d.P, 0)) # ?? потрібно ??

dim={'fi':d.fi, 'D':d.D, 'd3':d.d3, 'D1':d.D1, 'd6':d.d6, 'l3':d.l3}
sA0=revolve(rebuildSketch(dim=dim, sk='Sketch001'))
hA0=helix(r=d._r, h=d.l4-12, p=d.P, fi=d.fi)#h=n*d.P
hA0.translate((0,d.l3-d.l4,0)) # змістити вниз по осі, щоб нарізати внизу муфти - гвинт починається з d._r гвинта муфти
z=(d.H/2)*np.sin(np.radians(gamma0))
hgamma0=np.degrees(np.arctan(z/d._r))
print z,hgamma0
hA0.rotate(App.Vector(0,0,0),App.Vector(0,1,0),-hgamma0) # щоб почин. з пер. пов.
sA1=makeThread(fA0, hA0, sA0)

s_common=sA1.common(s_tl) # спільне тіло (якщо є)
print "CommonVolume=", s_common.Volume

## муфта
dim={'fi':pi-d.fi, 'H':d.H, 'r':d.r}
fB2=rebuildSketch(dim=dim, sk='Sketch002') # tool
fB2.translate(d._v1) # усюди d._v1 або усюди d._v2
#f2.rotate(App.Vector(0,0,0),App.Vector(0,1,0),1)
dim={'fi':d.fi, 'd4':d.d4, 'd7':d.d7, 'd8':d.d8, 'D':d.D, 'D1':d.D1, 'L2':d.L2, 'l4':d.l4, 'l3':d.l3} #'l4':d.l4+10
sB2=revolve(rebuildSketch(dim=dim, sk='Sketch003'))
hB2=helix(r=d._r, h=d.l4, p=d.P, fi=d.fi)
hB2.translate((0,d.l3-d.l4,0))
sB3=makeThread(fB2, hB2, sB2)

##
# Наступні команди потрібні тільки для візуалізації створених форм
Gui.showMainWindow() # показати головне вікно
Gui.activateWorkbench("PartWorkbench")
doc=App.newDocument() # створити новий документ
# показати форми

show('fA0')
show('e0')
#show('fA3')
show('hA0')
show('sA1')
show('s_tl0')
show('s_tl')
show('sB3')

doc.recompute() # перебудувати
Gui.exec_loop() # головний цикл програми