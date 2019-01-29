# -*- coding: utf-8 -*-
execfile("tools.py")
from dimsNKT import d
App.open(u"SketchesNKT.FCStd")

## ніпель
alfa0=8.0 # статичний задній кут 4..8
gamma0=0 #-10.0 # статичний передній кут 0..-10
n=9 #9 13 номер витка (положення різця)
insertS=6.1 # товщина різальної пластинки
omega=np.degrees(np.arctan(d.P/(pi*d.dsr))) # кут нахилу гвинтової лінії на dsr
print omega #np.arctan(d.P/(2*pi(Rmin+L*np.tan(d.fi))) 

#dim={'fi':d.fi,'P':d.P, 'r1':d.r1}
#fA0=rebuildSketch(dim=dim, sk='Sketch004') # tool
dim={'fi':d.fi,'P':d.P, 'r':d.r, 'r1':d.r1}
fA0=rebuildSketch(dim=dim, sk='Sketch006') #sk='Sketch' tool
e0=Part.makeLine((0,0,0),(insertS*np.tan(np.radians(alfa0+gamma0)), 0, insertS))
s_tl=Part.Wire([e0]).makePipe(fA0) # різець в нульовому положенні
for x in fA0,s_tl:
    x.rotate(App.Vector(0,0,0),App.Vector(0,1,0),-gamma0) # утв. передній кут
    #x.rotate(App.Vector(0,0,0),App.Vector(1,0,0), omega) # повернути на omega

s_tl0=s_tl.copy()

for x in fA0,s_tl:
    x.translate(d._v2) # початкове положення (усюди d._v1 або усюди d._v2)

s_tl.translate(App.Vector(n*d.P*np.tan(d.fi), n*d.P, 0)) # задане положення різця
#fA0.translate(App.Vector(n*d.P*np.tan(d.fi), n*d.P, 0))

dim={'fi':d.fi, 'D':d.D, 'd':d.d, 'l':d.l, 'd2':d.d2, 'Ln':d.l+30}
sA0=revolve(rebuildSketch(dim=dim, sk='Sketch002'))
hA0=helix(r=d._r, h=d._l2+d.L, p=d.P, fi=d.fi)#h=n*d.P
hA0.translate((0,-d._l2,0)) # змістити вниз по осі, щоб нарізати внизу муфти - гвинт починається з d._r гвинта муфти
z=(d.H/2)*np.sin(np.radians(gamma0))
hgamma0=np.degrees(np.arctan(z/d._r))
print z,hgamma0
hA0.rotate(App.Vector(0,0,0),App.Vector(0,1,0),-hgamma0) # щоб почин. з пер. пов.
#sA1=makeThread(fA0, hA0, sA0)
sA1=makeQuasiThread(fA0, sA0, d.P, d.tanFi, d._l2+d.L)

s_common=sA1.common(s_tl) # спільне тіло (якщо є)
#print "CommonVolume=", s_common.Volume

## муфта
#dim={'fi':d.fi, 'P':d.P, 'r1':d.r1}
#fB2=rebuildSketch(dim=dim, sk='Sketch005') # tool
dim={'fi':d.fi, 'P':d.P, 'r':d.r, 'r1':d.r1}
fB2=rebuildSketch(dim=dim, sk='Sketch001') # tool
fB2.translate(d._v2) # усюди d._v1 або усюди d._v2
#f2.rotate(App.Vector(0,0,0),App.Vector(0,1,0),1)
dim={'fi':d.fi, 'Dm':d.Dm, 'd0':d.d0, 'd3':d.d3, 'Lm':d.Lm, '_l':d._l}
sB2=revolve(rebuildSketch(dim=dim, sk='Sketch003'))
hB2=helix(r=d._r, h=d.Lm, p=d.P, fi=d.fi)
hB2.translate((0,d._l2,0))
#sB3=makeThread(fB2, hB2, sB2)
sB3=makeQuasiThread(fB2, sB2, d.P, d.tanFi, d.Lm)

f1,f2=section(sA1,sB3)
#f2.translate((0,d.P,0)) # утворити натяг
f1.exportStep("f1.step")
f2.exportStep("f2.step")

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
show('f1')
show('f2')

doc.recompute() # перебудувати
Gui.exec_loop() # головний цикл програми